'''
Concept:
If the habitat of smORFs in a cluster is different, the minority is subordinate to the majority.
Extract 100% identity smORFs with habitat.
'''

import gzip
import lzma

'''
The minority is subordinate to the majority.
'''
def less_more(infile1,outfile):
    cluster = {}
    habitat = {}
    count = {}   
    out = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")   
            if cluster:
                if linelist[0] in cluster.keys():
                    cluster[linelist[0]].append(linelist[1])
                else:
                    for key,value in cluster.items():
                        for i in range(len(value)):
                            hab = habitat[value[i]]
                            if hab in count.keys():
                                count[hab] += 1
                            else:
                                count[hab] = 1
                        change = max(count, key=lambda x: count[x])
                        for j in range(len(value)):
                            out.write(key+"\t"+value[j]+"\t"+change+"\n")                     
                    cluster = {}
                    habitat = {}
                    count = {}
                    cluster[linelist[0]] = [linelist[1]]
            else:
                cluster[linelist[0]] = [linelist[1]]              
            habitat[linelist[1]] = linelist[2]              
    for key,value in cluster.items():
        for i in range(len(value)):
            hab = habitat[value[i]]
            if hab in count.keys():
                count[hab] += 1
            else:
                count[hab] = 1         
        change = max(count, key=lambda x: count[x])
        for j in range(len(value)):
            out.write(key+"\t"+value[j]+"\t"+change+"\n")        
    out.close()

'''
Extract 100% identity smORFs with habitat.
'''
def extract(infile1,infile2,outfile):
    smorf = set()
    n = 0
    out = lzma.open(outfile, "wt")
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            smorf.add(linelist[0])
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t",2)
            if linelist[1] in smorf:
                if len(linelist) == 3:
                    out.write(linelist[1]+"\t"+linelist[2]+"\n")
                else:
                    out.write(linelist[1]+"\n")
            else:
                continue
    out.close()
    
INPUT_FILE_1 = "/habitat/metag_cluster_habitat.tsv.xz"
INPUT_FILE_2 = "/clust_result/result/all_0.5_0.9.tsv.gz" 
OUTPUT_FILE_1 = "/habitat/less_more/metag_cluster_all_habitat.tsv.xz"
OUTPUT_FILE_2 = "/habitat/id100/100AA_habitat.tsv.xz" 
less_more(INPUT_FILE_1,OUTPUT_FILE_1)
extract(INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_2)