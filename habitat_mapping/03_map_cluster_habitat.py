'''
Concept:
Map habitat to 90% and 50% identity clusters.
'''

import gzip
import lzma

'''
Change format of 90% identity clusters including two columns(90AA clusters and 100AA name) 
'''
def change_format_90(infile1,outfile):
    cluster = {}
    out = lzma.open(outfile, "wt")
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) == 3:
                if linelist[2] in cluster.keys():
                    cluster[linelist[2]].append(linelist[0])
                else:
                    cluster[linelist[2]] = [linelist[0]]
            else:
                cluster[linelist[0]] = [linelist[0]]
    for key,value in cluster.items():
        for i in range(len(value)):
            out.write(key+"\t"+value[i]+"\n")
    out.close()

'''
Change format of 50% identity clusters including two columns(50AA clusters and 100AA name) 
'''   
def change_format_50(infile1,outfile):
    cluster = {}
    out = lzma.open(outfile, "wt")
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[1]!="":
                if linelist[1] in cluster.keys():
                    cluster[linelist[1]].append(linelist[0])
                else:
                    cluster[linelist[1]] = [linelist[0]]
            else:
                cluster[linelist[0]] = [linelist[0]]
    for key,value in cluster.items():
        for i in range(len(value)):
            out.write(key+"\t"+value[i]+"\n")
    out.close()

'''
Map habitat to 90% and 50% identity clusters.
'''
def mapcluster(infile1,infile2,outfile):
    habitat = {}
    out = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t",1)
            habitat[linelist[0]] = linelist[1]

    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t") 
            out.write(linelist[0]+"\t"+linelist[1]+"\t"+habitat[linelist[1]]+"\n")

    out.close()

INPUT_FILE_1 = "/clust_result/result/all_0.5_0.9.tsv.gz" 
INPUT_FILE_2 = "/habitat/id100/100AA_multi_general_habitat.tsv.xz"   
OUTPUT_FILE_1 = "all_cluster_0.9.tsv.xz"  
OUTPUT_FILE_2 = "all_cluster_0.5.tsv.xz"
OUTPUT_FILE_3 = "/habitat/id90/cluster_multi_habitat_90.tsv.xz" 
OUTPUT_FILE_4 = "/habitat/id50/cluster_multi_habitat_50.tsv.xz" 

change_format_90(INPUT_FILE_1,OUTPUT_FILE_1)
change_format_50(INPUT_FILE_1,OUTPUT_FILE_2)
mapcluster(INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_3)
mapcluster(INPUT_FILE_2,OUTPUT_FILE_2,OUTPUT_FILE_4)