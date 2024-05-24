'''
Concept:
Rescue singletons
Split singletons into subfiles for running diamond, because of its large number.
'''

import gzip
from fasta import fasta_iter

'''
split inputfile according to max number of sequences X
'''
def splitseq(infile,X,outfile):
    ix = 0
    n = 0
    oname = outfile.format(ix=ix)
    out =  gzip.open(oname, "wt", compresslevel=1)
    for ID,seq in fasta_iter(infile):
        if n < X:
            n += 1
            out.write(f'>{ID}\n{seq}\n')
        else:
            n = 1
            ix += 1
            oname = outfile.format(ix=ix)
            out =  gzip.open(oname, "wt", compresslevel=1)
            out.write(f'>{ID}\n{seq}\n')
        if not ID:
            break
    out.close()
    
INPUT_FILE = "metag_ProG_singleton.faa.gz"
SPLIT_FILE_PAT = "./split/sub{ix}.faa.gz"

splitseq(INPUT_FILE, 100000000, SPLIT_FILE_PAT)