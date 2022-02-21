'''
Generate metatranscriptome mapping results for 100AA,90AA and 50AA smORFs.
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


def assign_50(infile1,infile2,outfile1,outfile2):
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
            if len(linelist) > 2:
                if linelist[2] in cluster.keys():
                    if linelist[0] in smorf: 
                        cluster[linelist[2]][0] += 1
                    else:
                        cluster[linelist[2]][1] += 1        
                else:
                    cluster[linelist[2]] = [0,0]
                    if linelist[0] in smorf: 
                        cluster[linelist[2]][0] += 1
                    else:
                        cluster[linelist[2]][1] += 1  
                    
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
    
INPUT_FILE_1 = "/metaT/result/merge/metaT_result_filter.tsv"
INPUT_FILE_2 = "/data/frozen/all_0.9_0.5_family.tsv.xz"
OUTPUT_FILE_1 = "/metaT/result/merge/metaT_100AA.tsv.gz"
OUTPUT_FILE_2 = "/metaT/result/merge/50AA_T_F_rate.tsv.gz"

assign_100(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
assign_50(OUTPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_2)