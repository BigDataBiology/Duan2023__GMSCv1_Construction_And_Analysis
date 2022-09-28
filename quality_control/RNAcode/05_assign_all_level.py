'''
Generate RNAcode results for 100AA,90AA and 50AA.
If the true rate in the family > 0.5,then the family will be true.
If the true rate in the family < 0.5, the minority of F and NA is subordinate to the majority, if the number of F and NA is the same, set it to NA.
'''

'''
Generate true and false coding potential 100AA and 90AA smORFs.
'''
def true_false_100AA_90AA(infile1,infile2,infile3,infile4,outfile1,outfile2,outfile3,outfile4):
    import lzma
    
    out1 = lzma.open(outfile1,"wt")
    out2 = lzma.open(outfile2,"wt")
    out3 = lzma.open(outfile3,"wt")
    out4 = lzma.open(outfile4,"wt")

    true_90AA = set()
    false_90AA = set()
    true_100AA = set()
    false_100AA = set()

# Store true potential 90AA smORFs with old identifier. 
    with open (infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            true_90AA.add(line)

# Get true and false potential 100AA and 90AA smORFs with old identifier.            
    with open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in true_90AA:
                true_100AA.add(linelist[1])
            else:
                false_100AA.add(linelist[1])
                false_90AA.add(linelist[0])

# Generate true and false potential 100AA smORFs with new identifier.    
    with lzma.open(infile3,"rt") as f3:
        for line in f3:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in true_100AA:
                out1.write(linelist[1]+"\n")
            elif linelist[0] in false_100AA:
                out2.write(linelist[1]+"\n")
            else:
                continue

# Generate true and false potential 90AA smORFs with new identifier.    
    with lzma.open(infile4,"rt") as f4:
        for line in f4:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in true_90AA:
                out3.write(linelist[1]+"\n")
            elif linelist[0] in false_90AA:
                out4.write(linelist[1]+"\n")
            else:
                continue

    out1.close() 
    out2.close()
    out3.close()
    out4.close()

'''
Generate true and false coding potential 50AA smORFs.
'''
def true_false_50AA(infile1,infile2,infile3,outfile,outfile1,outfile2):
    import lzma
    import gzip

    out = gzip.open(outfile, "wt", compresslevel=1)
    out1 = lzma.open(outfile1,"wt")
    out2 = lzma.open(outfile2,"wt")

    true = set()
    false = set()
    cluster = {}

    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            true.add(line)
            
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            false.add(line)
            
    with lzma.open(infile3,"rt") as f3:      
        for line in f3:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) > 2:
                if linelist[2] in cluster.keys():
                    if linelist[0] in true: 
                        cluster[linelist[2]][0] += 1
                    elif linelist[0] in false:
                        cluster[linelist[2]][1] += 1                    
                    else:
                        cluster[linelist[2]][2] += 1       
                else:
                    cluster[linelist[2]] = [0,0,0]
                    if linelist[0] in true: 
                        cluster[linelist[2]][0] += 1
                    elif linelist[0] in false:
                        cluster[linelist[2]][1] += 1                    
                    else:
                        cluster[linelist[2]][2] += 1  
                    
    for key,value in cluster.items():
        out.write(key+"\t"+str(value[0])+"\t"+str(value[1])+"\t"+str(value[2])+"\t"+str(value[0]/(value[0]+value[1]+value[2]))+"\n")
    out.close()

    with gzip.open (outfile,"rt") as f4:
        for line in f4:
            line = line.strip()
            linelist = line.split("\t")
            if float(linelist[4]) > 0.5:
                out1.write(linelist[0]+"\n")
            else:
                if float(linelist[2]) > float(linelist[3]):
                    out2.write(linelist[0]+"\n")
    out1.close()
    out2.close()    
        
INPUT_FILE_1  = "./RNAcode_result/filter/result/smORF_0.9_RNAcode.tsv"
INPUT_FILE_2 = "./clust_result/result/all_0.5_0.9_filter.tsv"
INPUT_FILE_3 = "./data/frozen/100AA_rename.tsv.xz"
INPUT_FILE_4 = "./data/frozen/90AA_rename.tsv.xz"
INPUT_FILE_5 = "./data/frozen/all_0.9_0.5_family.tsv.xz"

OUTPUT_FILE_1 = "./RNAcode_result/filter/result/rnacode_true_100AA.tsv.xz"
OUTPUT_FILE_2 = "./RNAcode_result/filter/result/rnacode_false_100AA.tsv.xz"
OUTPUT_FILE_3 = "./RNAcode_result/filter/result/rnacode_true_90AA.tsv.xz"
OUTPUT_FILE_4 = "./RNAcode_result/filter/result/rnacode_false_90AA.tsv.xz"
OUTPUT_FILE_5 = "./RNAcode_result/filter/result/50AA_T_F_rate.tsv.gz"
OUTPUT_FILE_6 = "./RNAcode_result/filter/result/rnacode_true_50AA.tsv.xz"
OUTPUT_FILE_7 = "./RNAcode_result/filter/result/rnacode_false_50AA.tsv.xz"

true_false_100AA_90AA(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,INPUT_FILE_4,OUTPUT_FILE_1,OUTPUT_FILE_2,OUTPUT_FILE_3,OUTPUT_FILE_4)
true_false_50AA(OUTPUT_FILE_1,OUTPUT_FILE_2,INPUT_FILE_5,OUTPUT_FILE_5,OUTPUT_FILE_6,OUTPUT_FILE_7)