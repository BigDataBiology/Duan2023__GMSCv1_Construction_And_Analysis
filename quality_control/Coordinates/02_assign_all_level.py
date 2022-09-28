'''
Generate coordinate checking results of 100AA,90AA and 50AA smORFs.
If the true rate in the family > 0.5,then the family will be true.
'''

'''
Assign 100AA
'''
def assign_100(infile1,infile2,outfile):
    import gzip
    import lzma

    tfdict = {}
    out = gzip.open(outfile, "wt", compresslevel=1)

    with gzip.open (infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            metag,tf = line.split("\t")
            tfdict[metag] = tf
  
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in tfdict.keys():
                out.write(linelist[1]+"\t"+tfdict[linelist[0]]+"\n")
            else:
                out.write(linelist[1]+"\t"+linelist[0]+"\n")

    out.close()

def assign_90_50(infile1,infile2,outfile1,outfile2,outfile3,outfile4):
    import lzma
    import gzip

    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
    out3 = gzip.open(outfile3, "wt", compresslevel=1)
    out4 = gzip.open(outfile4, "wt", compresslevel=1)
 
    tf = {}
    cluster_90 = {}
    cluster_50 = {}

    with gzip.open (infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            tf[linelist[0]] = linelist[1]
            
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[1] != "":
                if linelist[1] in cluster_90.keys():
                    if tf[linelist[0]] == "T":
                        cluster_90[linelist[1]][0] += 1
                    elif tf[linelist[0]] == "F":
                        cluster_90[linelist[1]][1] += 1
                    else:
                        cluster_90[linelist[1]][2] += 1        
                else:
                    cluster_90[linelist[1]] = [0,0,0]
                    if tf[linelist[0]] == "T":
                        cluster_90[linelist[1]][0] += 1
                    elif tf[linelist[0]] == "F":
                        cluster_90[linelist[1]][1] += 1
                    else:
                        cluster_90[linelist[1]][2] += 1
                    
    for key,value in cluster_90.items():
        out1.write(key+"\t"+str(value[0])+"\t"+str(value[1])+"\t"+str(value[2])+"\t"+str(value[0]/(value[0]+value[1]+value[2]))+"\n")
    out1.close()

    with gzip.open (outfile1,"rt") as f3:
        for line in f3:
            line = line.strip()
            linelist = line.split("\t",)
            if float(linelist[4]) > 0.5:
                out2.write(linelist[0]+"\t"+"T"+"\n")
            else:
                out2.write(linelist[0]+"\t"+"F"+"\n")           
    out2.close()

    with lzma.open(infile2,"rt") as f4:
        for line in f4:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) > 2:
                if linelist[2] in cluster_50.keys():
                    if tf[linelist[0]] == "T":
                        cluster_50[linelist[2]][0] += 1
                    elif tf[linelist[0]] == "F":
                        cluster_50[linelist[2]][1] += 1
                    else:
                        cluster_50[linelist[2]][2] += 1        
                else:
                    cluster_50[linelist[2]] = [0,0,0]
                    if tf[linelist[0]] == "T":
                        cluster_50[linelist[2]][0] += 1
                    elif tf[linelist[0]] == "F":
                        cluster_50[linelist[2]][1] += 1
                    else:
                        cluster_50[linelist[2]][2] += 1
                    
    for key,value in cluster_50.items():
        out3.write(key+"\t"+str(value[0])+"\t"+str(value[1])+"\t"+str(value[2])+"\t"+str(value[0]/(value[0]+value[1]+value[2]))+"\n")
    out3.close()  

    with gzip.open (outfile3,"rt") as f5:
        for line in f5:
            line = line.strip()
            linelist = line.split("\t",)
            if float(linelist[4]) > 0.5:
                out4.write(linelist[0]+"\t"+"T"+"\n")
            else:
                out4.write(linelist[0]+"\t"+"F"+"\n")           
    out4.close()

INPUT_FILE_1 = "./coordinate/all/result.tsv.gz"
INPUT_FILE_2 = "./data/frozen/100AA_rename.tsv.xz"
INPUT_FILE_3 = "./data/frozen/all_0.9_0.5_family.tsv.xz"
OUTPUT_FILE_1 = "./coordinate/all/100AA_coordinate.tsv.gz"
OUTPUT_FILE_2 = "./coordinate/all/90AA_T_F_iso_rate.tsv.gz"
OUTPUT_FILE_3 = "./coordinate/all/90AA_coordinate.tsv.gz"
OUTPUT_FILE_4 = "./coordinate/all/50AA_T_F_iso_rate.tsv.gz"
OUTPUT_FILE_5 = "./coordinate/all/50AA_coordinate.tsv.gz"

assign_100(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
assign_90_50(OUTPUT_FILE_1,INPUT_FILE_3,OUTPUT_FILE_2,OUTPUT_FILE_3,OUTPUT_FILE_4,OUTPUT_FILE_5)