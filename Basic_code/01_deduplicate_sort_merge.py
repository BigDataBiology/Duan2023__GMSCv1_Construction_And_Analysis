'''
Concept:
The number of all redundant smORFs from metaG and Progenome is 4,599,187,424
(metaG:424,4,564,570,019,Progenome:34,617,405).
The whole smORFs can't be sorted in memory at one time and need to be splited in 256 subfiles.
Then we can de duplicate and sort every subfiles separately.
Finally,we merge all the subfiles to generate non-redundant sorted smORFs.
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
De duplicate and sort every subfiles according to sequence alphabetical order.
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

INPUT_FILE = "/data/GMSC10.metag_Prog_smorfs.faa.gz"
OUTPUT_FILE = "/data/smorf_dedup.faa.gz"

splits = splitseq(INPUT_FILE)
for sp in bvalue(splits):
    dedup_fasta(sp)
mergeseq(OUTPUT_FILE)