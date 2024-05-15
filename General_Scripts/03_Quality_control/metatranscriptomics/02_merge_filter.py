'''
Concept:
Merge all the results in a .tsv file.
Filter 90AA families that can be mapped in at least 2 samples.
If 90AA family representive sequence has metatranscriptome evidence, all the 100AA smORFs in the family will be true.
'''

import glob
import pandas as pd

def read_and_set_index(n_f):
    n, f = n_f[0], n_f[1]
    return pd.read_table(f, skiprows=2, names=['smORF', str(n)+'_reads'], sep='\t').set_index('smORF')

def filter(infile,outfile):
    with open(outfile,'wt') as out:
        with open(infile,"rt") as f:
            for line in f:
                linelist = line.strip().split("\t")
                n = 0
                for i in linelist:
                    if i != "":
                        n += 1
                if n > 2:
                    out.write(f'{line}')

def assign_100(infile1,infile2,outfile1):
    import gzip
    
    out1 = open(outfile1, "wt")
    metaT = set()
    new = set()
    
    with open(infile1,"rt") as f1:
        for line in f1:
            linelist = line.strip().split("\t")
            if line.startswith("smORF"):
                continue
            else:
                metaT.add(linelist[0])
            
    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            member,cluster = line.strip().split("\t")
            if cluster in metaT:
                out1.write(f'{member}\n')
    out1.close() 

INPUT_FILE = glob.glob('./*.tsv') 
INPUT_FILE_1 = "GMSC.cluster.tsv.gz"
OUTPUT_FILE_1 = "metaT_result.tsv"
OUTPUT_FILE_2 = "metaT_90AA.tsv"
OUTPUT_FILE_3 = "metaT_100AA.tsv"

dfs = map(read_and_set_index, enumerate(INPUT_FILE))
pd.concat(dfs, axis=1, sort=True, join='outer').to_csv(OUTPUT_FILE_1, sep='\t')
filter(OUTPUT_FILE_1,OUTPUT_FILE_2)
assign_100(OUTPUT_FILE_2,INPUT_FILE_1,OUTPUT_FILE_1)