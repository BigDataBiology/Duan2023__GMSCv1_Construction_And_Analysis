'''
Concept:
100AA smORFs are too many to process.Split them in 20 sub files to speed up.
'''

from fasta import fasta_iter
import gzip

def split(infile,outpath):
    n = 0
    m = 0
    outfile = outpath+"/sub"+str(m)+".faa.gz"
    out = gzip.open(outfile,compresslevel=1, mode='wt')
    for ID,seq in fasta_iter(infile):
        if n < 50000000:
            out.write(f">{ID}\n{seq}\n")
            n += 1
        else:
            out.close()                        
            m += 1
            outfile = outpath+"/sub"+str(m)+".faa.gz"
            out = gzip.open(outfile,compresslevel=1, mode='wt')
            out.write(f">{ID}\n{seq}\n")
            n = 1
    out.close()    
        
INPUT_FILE_1 = "./data/frozen/100AA_GMSC.faa.xz"
OUT_PATH = "./metaproteomes/data/split_all"

split(INPUT_FILE_1,OUT_PATH)