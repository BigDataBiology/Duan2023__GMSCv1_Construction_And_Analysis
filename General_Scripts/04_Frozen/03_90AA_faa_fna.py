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
Numbers were assigned in order of increasing number of copies. 
So that the lower the number, the lower the number of copies of that peptide was present in the input data. 
And if the number of copies is same, numbers were assigned in order of letters of peptides.
'''
def rename(infile1,infile2,outfile,n,prefix):   
    number = {}
    seqnumber_list=[]
    
    with gzip.open(infile2,"rt") as f2:
        for line in f2 :
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in number.keys():
                number[linelist[0]] += 1
            else:
                number[linelist[0]] = 1
            
    for ID,seq in fasta_iter(infile1):
        seqnumber_tup = (int(number[ID]),seq,ID) 
        seqnumber_list.append(seqnumber_tup)
             
    sortseqnumber_list=sorted(seqnumber_list,key=itemgetter(0,1))
    with lzma.open(outfile,"wt") as out:
        for i in range (len(sortseqnumber_list)):
            nf = f'{n:09}'
            out.write(f'{sortseqnumber_list[i][2]}\t{prefix}.{nf[:3]}_{nf[3:6]}_{nf[6:9]}\n')
            n += 1

'''
Generate originalname - 100AA - 90AA rename list.
'''
def rename_all(infile1,infile2,outfile):   
    name = {}
    out1 = lzma.open(outfile, "wt")
    
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            name[linelist[0]] = linelist[1] 
            
    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip().strip(">")
            linelist = line.split("\t")
            if linelist[0] in name.keys():
                out1.write(linelist[0]+"\t"+linelist[1]+"\t"+name[linelist[0]]+"\n")         
    out1.close()   

'''
Generate rename and sequence of 90AA faa.
'''
def getfaa(infile1,infile2,outfile):   
    name = {}
    out1 = lzma.open(outfile, "wt")
    
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            name[linelist[0]] = linelist[1] 
            
    
    for ID,seq in fasta_iter(infile2):
        out1.write(f'>{name[ID]}\n{seq}\n')            
    out1.close()  

'''
Generate rename and sequence of 90AA fna.
'''
def getfna(infile1,infile2,outfile):       
    fasta = {}
    table = {}
    out1 = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            table[linelist[1]] = linelist[2]
        
    for ID,seq in fasta_iter(infile2):
        if ID in table.keys():           
            fasta[table[ID]] = seq
    table = {}
    for ID,seq in sorted(fasta.items()):
        out1.write(f">{ID}\n{seq}\n")               
    out1.close()  

INPUT_FILE_1 = "./clust_result/0.5_result/metag_ProG_nonsingleton_0.9_clu_rep.faa.gz"
INPUT_FILE_2 = "./clust_result/0.5_result/metag_ProG_nonsingleton_0.9_clu.tsv.gz"
INPUT_FILE_3 = "./data/100AA_rename.tsv.xz"
INPUT_FILE_4 = "./data/frozen/100AA_GMSC.fna.xz"

OUTPUT_FILE_1 = "./data/frozen/90AA_rename.tsv.xz"
OUTPUT_FILE_2 = "./data/frozen/90AA_rename_all.tsv.xz"
OUTPUT_FILE_3 = "./data/frozen/90AA_GMSC.faa.xz"
OUTPUT_FILE_4 = "./data/frozen/90AA_GMSC.fna.xz"

rename(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1,0,'GMSC10.90AA')
rename_all(OUTPUT_FILE_1,INPUT_FILE_3,OUTPUT_FILE_2)
getfaa(OUTPUT_FILE_1,INPUT_FILE_1,OUTPUT_FILE_3)
getfna(OUTPUT_FILE_2,INPUT_FILE_4,OUTPUT_FILE_4 )