'''
Generate RNAcode results for 100AA,90AA.
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

INPUT_FILE_1  = "./RNAcode_result/filter/result/smORF_0.9_RNAcode.tsv"
INPUT_FILE_2 = "./clust_result/result/all_0.5_0.9_filter.tsv"
INPUT_FILE_3 = "./data/frozen/100AA_rename.tsv.xz"
INPUT_FILE_4 = "./data/frozen/90AA_rename.tsv.xz"
INPUT_FILE_5 = "./data/frozen/all_0.9_0.5_family.tsv.xz"

OUTPUT_FILE_1 = "./RNAcode_result/filter/result/rnacode_true_100AA.tsv.xz"
OUTPUT_FILE_2 = "./RNAcode_result/filter/result/rnacode_false_100AA.tsv.xz"
OUTPUT_FILE_3 = "./RNAcode_result/filter/result/rnacode_true_90AA.tsv.xz"
OUTPUT_FILE_4 = "./RNAcode_result/filter/result/rnacode_false_90AA.tsv.xz"

true_false_100AA_90AA(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,INPUT_FILE_4,OUTPUT_FILE_1,OUTPUT_FILE_2,OUTPUT_FILE_3,OUTPUT_FILE_4)