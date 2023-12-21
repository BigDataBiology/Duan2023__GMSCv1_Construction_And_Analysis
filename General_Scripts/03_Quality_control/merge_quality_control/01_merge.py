'''
Merge all the quality control results.
If it pass all the computational checking(Antifam,RNAcode,coordinate),
and has at least 1 experimental evidence(Metaproteomes,metatranstomes,(meta)riboseq),then it will be high quality.
'''

def merge(infile1,infile2,infile3,infile4,infile5,infile6,infile7,infile8,outfile):
    import lzma
    import gzip

    out = gzip.open(outfile, "wt", compresslevel=1)
    smorf = {}

    with lzma.open (infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            smorf[linelist[1]] = ["NA","T","F","F","NA","F"]
            
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            smorf[line][0] = "T"

    with lzma.open(infile3,"rt") as f3:
        for line in f3:
            line = line.strip()
            smorf[line][0] = "F"
            
    with open(infile4,"rt") as f4:
        for line in f4:
            line = line.strip()
            smorf[line][1] = "F"  

    with gzip.open(infile5,"rt") as f5:
        for line in f5:
            line = line.strip()
            linelist = line.split("\t")
            smorf[linelist[0]][2] = "T"        
            
    with gzip.open(infile6,"rt") as f6:
        for line in f6:
            line = line.strip()
            smorf[line][3] = "T"         
            
    with gzip.open(infile7,"rt") as f7:
        for line in f7:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[1] == "T" or linelist[1] == "F":
                smorf[linelist[0]][4] = linelist[1]        
            else:
                smorf[linelist[0]][4] = "NA"

    with gzip.open(infile8,"rt") as f8:
        for line in f6:
            line = line.strip()
            smorf[line][5] = "T" 

    for key,value in smorf.items():
        out.write(key+"\t"+value[0]+"\t"+value[1]+"\t"+value[2]+"\t"+value[3]+"\t"+value[4]+"\t"+value[5]+"\n")

    out.close()

def allpass(infile,outfile):
    import gzip

    out = open(outfile,"wt")
    with gzip.open (infile,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t",)
            if linelist[1] == "T" and linelist[2] == "T" and linelist[5] == "T" and (linelist[3] == "T" or linelist[4] == "T" or linelist[6] == "T"):
                out.write(linelist[0]+"\n")
            
    out.close()

INPUT_FILE_1 = "./data/frozen/100AA_rename.tsv.xz"
INPUT_FILE_2 = "./RNAcode_result/filter/result/rnacode_true_100AA.tsv.xz"
INPUT_FILE_3 = "./RNAcode_result/filter/result/rnacode_false_100AA.tsv.xz"
INPUT_FILE_4 = "./antifam/antifam_result.tsv"
INPUT_FILE_5 = "./metaproteomes/merge_result/coverage_analysis.tsv.gz"
INPUT_FILE_6 = "./riboseq/result/merge/riboseq_100AA.tsv.gz"
INPUT_FILE_7 = "./coordinate/all/100AA_coordinate.tsv.gz"
INPUT_FILE_8 = "./metaT/result/merge/metaT_100AA.tsv.gz"
OUTPUT_FILE_1 = "./quality/allquality_100AA.tsv.gz"
OUTPUT_FILE_2 = "./quality/allpass_100AA.txt"

merge(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,INPUT_FILE_4,INPUT_FILE_5,INPUT_FILE_6,INPUT_FILE_7,INPUT_FILE_8,OUTPUT_FILE_1)
allpass(OUTPUT_FILE_1,OUTPUT_FILE_2)