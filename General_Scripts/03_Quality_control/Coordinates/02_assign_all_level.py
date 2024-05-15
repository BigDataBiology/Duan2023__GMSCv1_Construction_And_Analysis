'''
Generate coordinate checking results of 100AA,90AA smORFs.
If the true rate in the family > 0.5,then the family will be true.
'''

def assign_100(infile1,infile2,outfile):
    import gzip
    import lzma

    tfdict = {}
    out = gzip.open(outfile, "wt", compresslevel=1)

    with gzip.open (infile1,"rt") as f1:
        for line in f1:
            metag,tf = line.strip().split("\t")
            tfdict[metag] = tf
  
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            member,cluster = line.strip().split("\t")
            if member in tfdict.keys():
                out.write(f'{member}\t{tfdict[member]}\n')
            else:
                out.write(f'{member}\tNA\n')
    out.close()

def assign_90(infile1,infile2,outfile1,outfile2):
    import lzma
    import gzip

    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
 
    tf = {}
    cluster_90 = {}

    with gzip.open (infile1,"rt") as f1:
        for line in f1:
            smorf,terminal = line.strip().split("\t")
            tf[smorf] = terminal
            
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            member,cluster = line.strip().split("\t")
            if cluster not in cluster_90.keys():
                cluster_90[cluster] = [0,0,0]
            if tf[member] == "T":
                cluster_90[cluster][0] += 1
            elif tf[member] == "F":
                cluster_90[cluster][1] += 1
            else:
                cluster_90[cluster][2] += 1        
                    
    for key,value in cluster_90.items():
        out1.write(f'{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[0]/(value[0]+value[1]+value[2])}\n')
    out1.close()

    with gzip.open (outfile1,"rt") as f3:
        for line in f3:
            linelist = line.strip().split("\t")
            if float(linelist[4]) > 0.5:
                out2.write(f'{linelist[0]}\tT\n')
            else:
                out2.write(f'{linelist[0]}\tF\n')           
    out2.close()

INPUT_FILE_1 = "result.tsv.gz"
INPUT_FILE_2 = "GMSC.cluster.tsv.gz"
OUTPUT_FILE_1 = "100AA_coordinate.tsv.gz"
OUTPUT_FILE_2 = "90AA_T_F_iso_rate.tsv.gz"
OUTPUT_FILE_3 = "90AA_coordinate.tsv.gz"

assign_100(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
assign_90(OUTPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_2,OUTPUT_FILE_3)