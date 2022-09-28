'''
Concept:
Sort 100AA fna.
'''

import hashlib 
import lzma
from fasta import fasta_iter
import heapq
from glob import glob

'''
Split 100 fna file into 256 subfiles.
'''
def splitseq(infile):
    print("start splitseq")
    outputlist = [
        f'/data/frozen/split/sub_{ix:03}.fna.xz'
        for ix in range(256)]
    outputfiles = [
        lzma.open(f'/data/frozen/split/sub_{ix:03}.fna.xz',"wt")
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
De duplicate and sort each subfiles.
'''
def dedup_fasta(infile):
    print("start dedup")
    fasta = {}
    for ID,seq in fasta_iter(infile):
        fasta[ID] = seq
    outfile = infile.replace('.fna.xz', '.sort.fna.xz')
    out = lzma.open(outfile, "wt")
    print("start sort")
    for ID,seq in sorted(fasta.items()):
        out.write(f">{ID}\n{seq}\n")
    out.close()

def merge(outfile):
    with lzma.open(outfile, "wt") as output:
        inputs = [fasta_iter(f) for f in glob(f'/data/frozen/split/*.sort.fna.xz')]
        merged = heapq.merge(*inputs, key=lambda h_seq: (h_seq[0], h_seq[1]))
        for h,seq in merged:
            output.write(f'>{h}\n{seq}\n')

INPUT_FILE = "./data/frozen/100AA_GMSC.fna.xz"
OUTPUT_FILE="./data/frozen/sort/100AA_GMSC_sort.fna.xz"

splits = splitseq(INPUT_FILE)

for sp in splits:
    dedup_fasta(sp)

merge(OUTPUT_FILE)