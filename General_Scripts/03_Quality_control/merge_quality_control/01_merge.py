'''
Merge all the quality control results.
If it pass all the computational checking(Antifam,RNAcode,coordinate),
and has at least 1 experimental evidence(Metaproteomes,metatranstomes,riboseq),then it will be high quality.
'''

def merge(infile1,infile2,infile3,infile4,infile5,infile6,infile7,infile8,outfile):
    import lzma
    import gzip

    out = lzma.open(outfile, "wt")
    smorf = {}

    with lzma.open (infile1,"rt") as f1:
        for line in f1:
            linelist = line.strip().split("\t")
            smorf[linelist[0]] = ["NA","T","F","F","NA","F"]
            
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
            linelist = line.strip().split("\t")
            smorf[linelist[0]][2] = "T"        
            
    with open(infile6,"rt") as f6:
        for line in f6:
            line = line.strip()
            smorf[line][3] = "T"         
            
    with gzip.open(infile7,"rt") as f7:
        for line in f7:
            linelist = line.strip().split("\t")
            if linelist[1] == "T" or linelist[1] == "F":
                smorf[linelist[0]][4] = linelist[1]        
            else:
                smorf[linelist[0]][4] = "NA"

    with open(infile8,"rt") as f8:
        for line in f6:
            line = line.strip()
            smorf[line][5] = "T" 

    for key,value in smorf.items():
        out.write(f'{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\t{value[4]}\t{value[5]}\n')
    out.close()

def allpass(infile,outfile):
    import lzma
    with open(outfile,'wt') as out:
        with lzma.open(infile,"rt") as f1:
            for line in f1:
                smorf,rnacode,antifam,metap,riboseq,terminal,metat = line.strip().split("\t")
                if rnacode == "T" and antifam == "T" and terminal == "T" and (metap == "T" or riboseq == "T" or metat == "T"):
                    out.write(f'{smorf}\n') 
#100AA
INPUT_FILE_1 = "GMSC.cluster.tsv.gz"
INPUT_FILE_2 = "rnacode_true_100AA.tsv"
INPUT_FILE_3 = "rnacode_false_100AA.tsv"
INPUT_FILE_4 = "antifam_result.tsv"
INPUT_FILE_5 = "coverage_analysis.tsv.gz"
INPUT_FILE_6 = "riboseq_100AA.tsv"
INPUT_FILE_7 = "100AA_coordinate.tsv.gz"
INPUT_FILE_8 = "metaT_100AA.tsv"
OUTPUT_FILE_1 = "GMSC10.100AA.quality.tsv.xz"
OUTPUT_FILE_2 = "allpass_100AA.txt"

merge(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,INPUT_FILE_4,INPUT_FILE_5,INPUT_FILE_6,INPUT_FILE_7,INPUT_FILE_8,OUTPUT_FILE_1)
allpass(OUTPUT_FILE_1,OUTPUT_FILE_2)

INPUT_FILE_1 = "GMSC.cluster.tsv.gz"
INPUT_FILE_2 = "rnacode_true_90AA.tsv"
INPUT_FILE_3 = "rnacode_false_90AA.tsv"
INPUT_FILE_4 = "antifam_90AA.tsv.gz"
INPUT_FILE_5 = "metaP_90AA.tsv.gz"
INPUT_FILE_6 = "riboseq_90AA.tsv"
INPUT_FILE_7 = "90AA_coordinate.tsv.gz"
INPUT_FILE_8 = "metaT_90AA.tsv"
OUTPUT_FILE_1 = "GMSC10.90AA.quality.tsv.xz"
OUTPUT_FILE_2 = "allpass_90AA.txt"

merge(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,INPUT_FILE_4,INPUT_FILE_5,INPUT_FILE_6,INPUT_FILE_7,INPUT_FILE_8,OUTPUT_FILE_1)
allpass(OUTPUT_FILE_1,OUTPUT_FILE_2)