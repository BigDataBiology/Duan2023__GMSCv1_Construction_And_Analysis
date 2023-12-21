'''
Concept:
Map taxonomy of smORFs from Progenomes.
De duplicate of smORFs from Progenomes.
'''

import pandas as pd
from fasta import fasta_iter
import gzip

'''
Map taxonomy according to genome and specI.
'''
def maptaxa_tsv(prog,taxa,prog_taxa):
    prog_tsv= pd.read_table(prog,sep='\t',header=None)
    prog_tsv.columns=['genome','smORF'] 
    taxonomy=pd.read_table(taxa,sep='\t')
    taxa_tsv=pd.merge(prog_tsv,taxonomy,on=['genome'],how='left')
    taxa_tsv.to_csv(path_or_buf=prog_taxa, sep='\t', index=False)

'''
De duplicate of smORFs from Progenomes.
'''
def dedup_fasta(infile,outfile1,outfile2):
    print("start dedup")
    fasta = {}
    for ID,seq in fasta_iter(infile):
        if seq in fasta:
            fasta[seq].append(ID)
        else:
            fasta[seq] = []
            fasta[seq].append(ID)

    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
    print("start sort")
    for seq,IDlist in sorted(fasta.items()):
        for i in range(len(IDlist)):
            out1.write(f"{IDlist[0]}\t{IDlist[i]}\n")
        out2.write(f">{IDlist[0]}\n{seq}\n")
    out1.close()
    out2.close()
    print("finish dedup and sort")

prog = "./taxa/progenome/genome_prog.tsv"
taxa = "./taxa/progenome/specI_genome_taxa.txt"
prog_taxa = "./taxa/progenome/prog_specI_genome_taxa.tsv"
maptaxa_tsv(prog,taxa,prog_taxa)

INPUT_FILE = "GMSC10.ProG_smorfs.faa.gz"  
OUTPUT_FILE_1 = "./taxa/progenome/prog_dedup_sort.faa.gz"
OUTPUT_FILE_2 = "./taxa/progenome/prog_redundant.tsv.gz"    
dedup_fasta(INPUT_FILE,OUTPUT_FILE_1,OUTPUT_FILE_2)