'''
Generate metaproteomics quality results of 90AA. 
If at least 1 smORF has metaproteomics evidence in 90AA family, the family will be true.
'''

def assign(infile1,infile2,outfile1,outfile2):
    import lzma
    import gzip

    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)

    smorf = set()
    cluster_90 = {}

    with open(infile1,"rt") as f1:
        for line in f1:
            linelist = line.strip().split("\t")
            smorf.add(linelist[0])
                
    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            member,cluster = line.strip().split("\t")
            if cluster not in cluster_90.keys():
                cluster_90[cluster] = [0,0]
            if member in smorf: 
                cluster_90[cluster][0] += 1
            else:
                cluster_90[cluster][1] += 1        
    
    for key,value in cluster_90.items():
        out1.write(f'{key}\t{value[0]}\t{value[1]}\t{value[0]/(value[0]+value[1])}\n')
    out1.close()

    with gzip.open (outfile1,"rt") as f3:
        for line in f3:
            linelist = line.strip().split("\t")
            if float(linelist[3]) > 0:
                out2.write(f'{linelist[0]}\n')
    out2.close()

INPUT_FILE_1 = "coverage_analysis.tsv.gz"
INPUT_FILE_2 = "GMSC.cluster.tsv.gz"
OUTPUT_FILE_1 = "90AA_F_T_rate.tsv.gz"
OUTPUT_FILE_2 = "metaP_90AA.tsv.gz"

assign(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_2)