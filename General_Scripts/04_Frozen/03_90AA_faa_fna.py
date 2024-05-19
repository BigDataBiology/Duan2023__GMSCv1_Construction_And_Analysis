'''
Concept:
Generate rename and sequence of 90AA faa and fna.
'''

from operator import itemgetter   
from fasta import fasta_iter
import gzip
import lzma

'''
Generate original name - 90AA rename list.
Peptides are named: >GMSC10.90AA.XXX_XXX_XXX
'''
def rename(infile1,infile2,outfile,n,prefix):   
    number = {}
    seqnumber_list = []
    
    with gzip.open(infile2,"rt") as f2:
        for line in f2 :
            cluster,member = line.strip().split("\t")
            if cluster in number.keys():
                number[cluster] += 1
            else:
                number[cluster] = 1
            
    for ID,seq in fasta_iter(infile1):
        seqnumber_tup = (int(number[ID]),seq,ID) 
        seqnumber_list.append(seqnumber_tup)
             
    sortseqnumber_list = sorted(seqnumber_list,key=itemgetter(0,1))
    with lzma.open(outfile,"wt") as out:
        for item in sortseqnumber_list:
            nf = f'{n:09}'
            out.write(f'{item[2]}\t{prefix}.{nf[:3]}_{nf[3:6]}_{nf[6:9]}\n')
            n += 1 

'''
Generate original name - 100AA - 90AA rename list.
'''
def rename_all(infile1,infile2,outfile):   
    name = {}
    out1 = lzma.open(outfile, "wt")
    
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            old,new = line.strip().split("\t")
            name[old] = new
            
    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            old,new = line.strip().split("\t")
            if old in name.keys():
                out1.write(f'{old}\t{new}\t{name[new]}\n')         
    out1.close()

'''
Generate rename and sequence of 90AA faa.
'''
def getfaa(infile1,infile2,outfile):   
    name = {}
    out = lzma.open(outfile, "wt")
    
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            old,new = line.strip().split("\t")
            name[old] = new
                
    for ID,seq in fasta_iter(infile2):
        out.write(f'>{name[ID]}\n{seq}\n')            
    out.close()  

'''
Generate rename and sequence of 90AA fna.
'''
def getfna(infile1,infile2,outfile):       
    fasta = {}
    table = {}

    out = lzma.open(outfile, "wt")

    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            old,name100,name90 = line.strip().split("\t")
            table[name100] = name90
        
    for ID,seq in fasta_iter(infile2):
        if ID in table.keys():           
            fasta[table[ID]] = seq

    for ID,seq in sorted(fasta.items()):
        out.write(f">{ID}\n{seq}\n")               
    out.close()  

INPUT_FILE_1 = "metag_ProG_nonsingleton_0.9_clu_rep.faa.gz"
INPUT_FILE_2 = "metag_ProG_nonsingleton_0.9_clu.tsv.gz"
INPUT_FILE_3 = "100AA_rename.tsv.xz"
INPUT_FILE_4 = "100AA_GMSC.fna.xz"

OUTPUT_FILE_1 = "90AA_rename.tsv.xz"
OUTPUT_FILE_2 = "90AA_rename_all.tsv.xz"
OUTPUT_FILE_3 = "90AA_GMSC.faa.xz"
OUTPUT_FILE_4 = "90AA_GMSC.fna.xz"

rename(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1,0,'GMSC10.90AA')
rename_all(OUTPUT_FILE_1,INPUT_FILE_3,OUTPUT_FILE_2)
getfaa(OUTPUT_FILE_1,INPUT_FILE_1,OUTPUT_FILE_3)
getfna(OUTPUT_FILE_2,INPUT_FILE_4,OUTPUT_FILE_4)