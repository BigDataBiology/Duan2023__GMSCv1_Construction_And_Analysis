'''
Concept:
Generate the table including the name of smORFs, and the clusters they belong to at 90% identity.
'''

def generate_family(infile1,infile2,infile3,outfile):   
    import lzma
    import gzip
    name50 = {}
    name90 = {}
    out1 = lzma.open(outfile, "wt")
    
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            name50[linelist[1]] = linelist[2] 
            
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            name90[linelist[1]] = linelist[2]   
            
    with gzip.open(infile3,"rt") as f3:
        for line in f3:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) == 2:
                out1.write(linelist[0]+"\t"+""+"\t"+name50[linelist[1]]+"\n")
            elif len(linelist) == 3 and linelist[1] != "":
                out1.write(linelist[0]+"\t"+name90[linelist[2]]+"\t"+name50[linelist[1]]+"\n")
            else:
                out1.write(linelist[0]+"\t"+name90[linelist[2]]+"\n")           
    out1.close()        

INPUT_FILE_1 = "./data/frozen/50AA_rename_all.tsv.xz"  
INPUT_FILE_2 = "./data/frozen/90AA_rename_all.tsv.xz"
INPUT_FILE_3 = "./clust_result/result/all_0.5_0.9_rename.tsv.gz"
OUTPUT_FILE = "./data/frozen/all_0.9_0.5_family.tsv.xz"

generate_family(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,OUTPUT_FILE)

