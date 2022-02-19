def true_false(infile1,infile2,outfile1,outfile2):
    import lzma
    
    out1 = lzma.open(outfile1,"wt")
    out2 = lzma.open(outfile2,"wt")
    family = set()
    
    with open (infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            family.add(line)
            
    with open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in family:
                out1.write(linelist[1]+"\n")
            else:
                out2.write(linelist[1]+"\n")
           
    out1.close() 
    out2.close()
    
INPUT_FILE_1  = "/RNAcode_result/filter/result/smORF_0.9_RNAcode.tsv"
INPUT_FILE_2 = "/clust_result/result/all_0.5_0.9_filter.tsv"
OUTPUT_FILE_1 = "/RNAcode_result/filter/result/rnacode_seq.tsv.xz"
OUTPUT_FILE_2 = "/RNAcode_result/filter/result/rnacode_seq_false.tsv.xz"

true_false(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_2)