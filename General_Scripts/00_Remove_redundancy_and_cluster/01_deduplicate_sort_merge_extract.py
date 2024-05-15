'''
Concept:
The number of all redundant smORFs from metagenomes and Progenome2 is 4,599,187,424
(metagenomes:4,564,570,019,Progenome2:34,617,405).
The whole smORFs are too large to be sorted in memory. 
1. Split smORFs into 256 subfiles to de duplicate and sort each subfile separately.
2. Merge all the subfiles to generate non-redundant sorted smORFs.
3. Extract non-singletons and singletons.
'''

from jug import TaskGenerator, bvalue
import hashlib
import gzip
from fasta import fasta_iter
import os
import heapq
from glob import glob

'''
Split all smORFs into 256 sub .faa.gz file using hashlib.
'''
@TaskGenerator
def splitseq(infile):
    print("start splitseq")
    outputlist = [
        f'/split/sub_{ix:03}.faa.gz'
        for ix in range(256)]
    outputfiles = [
        gzip.open(f'/split/sub_{ix:03}.faa.gz',compresslevel=1,  mode='wt')
        for ix in range(256)]
    for ID,seq in fasta_iter(infile):
        h = hashlib.sha256()
        h.update(seq.encode('ascii'))
        ix = int(h.hexdigest()[:2], 16)
        outputfiles[ix].write(f'>{ID}\n{seq}\n')
    for ot in outputfiles:
        ot.close()
    print("finish splitseq")
    return (outputlist)

'''
De duplicate and sort subfiles according to sequence alphabetical order.
Calculate the number of occurrences of each sequence.
'''
@TaskGenerator
def dedup_fasta(infile):
    print("start dedup")
    fasta = {}
    for ID,seq in fasta_iter(infile):
        if seq in fasta:
            fasta[seq][1] += 1
        else:
            fasta[seq] = [ID, 1]

    outfile1 = infile.replace('.faa.gz', '.raw_number.tsv.gz')
    outfile2 = infile.replace('.faa.gz', '.dedup.faa.gz')
    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
    print("start sort")
    for seq,(ID,count) in sorted(fasta.items()):
        out1.write(f"{count}\t{seq}\n")
        out2.write(f">{ID}\n{seq}\n")
    out1.close()
    out2.close()
    os.unlink(infile)
    print("finish dedup and sort")
    return (outfile1, outfile2)

'''
Merge(sort and de duplicate) all the sorted subfiles to generate non-redundant sorted smORFs.
'''
@TaskGenerator
def mergeseq(outfile):
    print("start merge")
    with gzip.open(outfile, compresslevel=1, mode='wt') as output:
        inputs = [fasta_iter(f) for f in glob(f'/split/*.dedup.faa.gz')]
        merged = heapq.merge(*inputs, key=lambda h_seq: (h_seq[1], h_seq[0]))
        preseq="x"
        for h,seq in merged:
            if seq != preseq:
                output.write(f'>{h}\n{seq}\n')
                preseq = seq
    print("finish merge")

@TaskGenerator
def extract_seq(infile1,infile2,outfile1,outfile2):
    fastaset = set()
    with gzip.open(infile1,"rt") as f:
        for line in f:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] != "1":
                fastaset.add(linelist[1])

    with gzip.open(outfile1, "wt", compresslevel=1) as out1, \
        gzip.open(outfile2, "wt", compresslevel=1) as out2:
        for ID,seq in fasta_iter(infile2):
            if seq in fastaset:
                out1.write(f'>{ID}\n{seq}\n')
            else:
                out2.write(f'>{ID}\n{seq}\n')

INPUT_FILE = "GMSC10.metag_Prog_smorfs.faa.gz"
OUTPUT_FILE = "metag_ProG_dedup.faa.gz"

splits = splitseq(INPUT_FILE)
for sp in bvalue(splits):
    dedup_fasta(sp)
mergeseq(OUTPUT_FILE)

INPUT_FILE_1 = "metag_ProG.raw_number.tsv.gz"
OUT_FILE_1 = "metag_ProG_nonsingleton.faa.gz"
OUT_FILE_2 = "metag_ProG_singleton.faa.gz"
extract_seq(INPUT_FILE_1,OUTPUT_FILE,OUT_FILE_1,OUT_FILE_2)
