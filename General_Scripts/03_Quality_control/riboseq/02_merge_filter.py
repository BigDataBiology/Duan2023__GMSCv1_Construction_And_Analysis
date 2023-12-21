'''
Merge all the results in one .tsv file.
Filter smORFs that can be mapped in at least 2 samples.
'''

import glob
import pandas as pd

def read_and_set_index(n_f):
    n, f = n_f[0], n_f[1]
    return pd.read_table(f, skiprows=2, names=['smORF', str(n)+'_reads'], sep='\t').set_index('smORF')

def filter_riboseq(infile,outfile):
    out = open(outfile,"wt")
    with open(infile,"rt") as f:
        for line in f:
            line = line.strip()
            linelist = line.split("\t")
            n = 0
            for i in linelist:
                if i != "":
                    n += 1
            if n > 2:
                out.write(line+"\n")

    out.close()

INPUT_FILE = glob.glob('./riboseq/result/ngless/*.tsv') 
OUTPUT_FILE_1 = "./riboseq/result/merge/riboseq_result.tsv"
OUTPUT_FILE_2 = "./riboseq/result/merge/riboseq_result_filter.tsv"

dfs = map(read_and_set_index, enumerate(INPUT_FILE))
pd.concat(dfs, axis=1, sort=True, join='outer').to_csv(OUTPUT_FILE_1, sep='\t')
filter_riboseq(OUTPUT_FILE_1,OUTPUT_FILE_2)