'''
Generate metatranscriptome quality results for 100AA,90AA smORFs.
If 90AA family representive sequence has metatranscriptome evidence,all the 100AA smORFs in the family will be true.
If at least 1 smORF has metatranscriptome evidence in 90AA family,the family will be true.
'''

def assign_100(infile1,infile2,outfile1):
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


def assign(infile1,infile2,outfile1,outfile2):
    import lzma
    import gzip

    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
    smorf = set()
    cluster = {}

    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            smorf.add(line)
               
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[1] != "":
                if linelist[1] in cluster.keys():
                    if linelist[0] in smorf: 
                        cluster[linelist[1]][0] += 1
                    else:
                        cluster[linelist[1]][1] += 1        
                else:
                    cluster[linelist[1]] = [0,0]
                    if linelist[0] in smorf: 
                        cluster[linelist[1]][0] += 1
                    else:
                        cluster[linelist[1]][1] += 1  
                    
    for key,value in cluster.items():
        out1.write(key+"\t"+str(value[0])+"\t"+str(value[1])+"\t"+str(value[0]/(value[0]+value[1]))+"\n")
    out1.close()

    with gzip.open (outfile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            if float(linelist[3]) > 0:
                out2.write(linelist[0]+"\n")
    out2.close()
    
INPUT_FILE_1 = "./metaT/result/merge/metaT_result_filter.tsv"
INPUT_FILE_2 = "./data/frozen/all_0.9_0.5_family.tsv.xz"
OUTPUT_FILE_1 = "./metaT/result/merge/metaT_100AA.tsv.gz"
OUTPUT_FILE_2 = "./metaT/result/merge/90AA_T_F_rate.tsv.gz"
OUTPUT_FILE_3 = "./metaT/result/merge/metaT_90AA.tsv.gz"

assign_100(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
assign(OUTPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_2,OUTPUT_FILE_3)