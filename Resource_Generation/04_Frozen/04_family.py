'''
Concept:
Generate the table including the 100AA smORFs and 90AA families.
'''

def generate_family(infile1,infile2,infile3,outfile):   
    import lzma
    import gzip

    name90 = {}
    out = open(outfile, "wt")
            
    with lzma.open(infile1,"rt") as f:
        for line in f:
            old,new100,new90 = line.strip().split("\t")
            name90[new100] = new90
    
    name100 = {}
    with open(infile2,'rt') as f:
        for line in f:
            old,new = line.strip().split("\t")
            name100[old] = new

    with gzip.open(infile3,"rt") as f:
        for line in f:
            cluster,member = line.strip().split("\t")
            out.write(f'{name100[member]}\t{name90[cluster]}\n')
    out.close()        

INPUT_FILE_1 = "90AA_rename_all.tsv.xz"
INPUT_FILE_2 = "100AA_rename.tsv"  
INPUT_FILE_3 = "all_0.9.tsv.gz"
OUTPUT_FILE = "GMSC.cluster.tsv"

generate_family(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,OUTPUT_FILE)

