'''
Concept:
Get non-redundant clusters of raw data.
'''

import hashlib
import gzip 
from fasta import fasta_iter

'''
Split all smORFs into 256 subfiles.
'''
def splitseq(infile):
    print("start splitseq")
    outputlist = [
        f'/taxa/metag/dedup_cluster/split/sub_{ix:03}.faa.gz'
        for ix in range(256)]
    outputfiles = [
        gzip.open(f'/taxa/metag/dedup_cluster/split/sub_{ix:03}.faa.gz',compresslevel=1,  mode='wt')
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
Get non-redundant clusters of all smORFs.
'''   
def dedup_fasta(infile):
    from fasta import fasta_iter
    import gzip
    print("start dedup")
    fasta = {}
    for ID,seq in fasta_iter(infile):
        if seq in fasta.keys():
            fasta[seq].append(ID)
        else:
            fasta[seq] = [ID]
    outfile1 = infile.replace('.faa.gz', '.dedup_cluster.tsv.gz')
    out_1 = gzip.open(outfile1, "wt", compresslevel=1)
    for key,value in fasta.items():
        for i in range(len(value)):
            out_1.write(value[0]+"\t"+value[i]+"\n")
    out_1.close()

INPUT_FILE = "GMSC10.metag_ProG_smorfs.faa.gz"
splits = splitseq(INPUT_FILE)
for sp in splits:
    dedup_fasta(sp)