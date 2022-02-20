'''
Generate metatranscriptome mapping results for 100AA,90AA and 50AA smORFs.
'''
def metaT(infile1,infile2,outfile1):
    import gzip
    import lzma
    
    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    
    metaT = set()
    new = set()
    
    with open (infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith("smORF"):
                continue
            else:
                linelist = line.split("\t")
                metaT.add(linelist[0])
            
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[1] in metaT:
                new.add(linelist[0])
                out1.write(linelist[0]+"\n")
                
    out1.close() 


    
INPUT_FILE_1 = "/metaT/result/merge/metaT_result_filter.tsv"
INPUT_FILE_2 = "/data/frozen/all_0.9_0.5_family.tsv.xz"
OUTPUT_FILE = "/home1/duanyq/GMSC/metaT/result/merge/metaT_100AA.tsv.gz"

metaT(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE)