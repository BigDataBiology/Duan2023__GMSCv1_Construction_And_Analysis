'''
Sort faa files and family table.
'''

import lzma
from fasta import fasta_iter

'''
Sort faa files.
'''
def sort_faa(infile1,outfile):   
    fasta = {}
    out1 = lzma.open(outfile, "wt")

    for ID,seq in fasta_iter(infile1):
        fasta[ID] = seq
    for ID,seq in sorted(fasta.items()):
        out1.write(f">{ID}\n{seq}\n")    
    out1.close() 

'''
Sort family table.
'''
def sort_table(infile1,outfile):   
    table = {}
    out1 = lzma.open(outfile, "wt")
    
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t",1)
            table[linelist[0]] = linelist[1]

    for ID,family in sorted(table.items()):
        out1.write(f"{ID}\t{family}\n")    
    out1.close() 

INPUT_FILE_1 = "./data/frozen/90AA_GMSC.faa.xz"  
INPUT_FILE_2 = "./data/frozen/100AA_GMSC.faa.xz"  
INPUT_FILE_3 = "./data/frozen/all_0.9_0.5_family.tsv.xz" 

OUTPUT_FILE_1 = "./data/frozen/90AA_GMSC_sort.faa.xz"
OUTPUT_FILE_2 = "./data/frozen/100AA_GMSC_sort.faa.xz"
OUTPUT_FILE_3 = "./data/frozen/all_0.9_0.5_family_sort.tsv.xz"

sort_faa(INPUT_FILE_1,OUTPUT_FILE_1)
sort_faa(INPUT_FILE_2,OUTPUT_FILE_2)
sort_faa(INPUT_FILE_3,OUTPUT_FILE_3)