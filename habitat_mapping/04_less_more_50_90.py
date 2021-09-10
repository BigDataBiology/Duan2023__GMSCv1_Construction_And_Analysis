'''
Concept:
If the habitat of smORFs in a cluster is different, the minority is subordinate to the majority.
'''

import lzma

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

INPUT_FILE_1 = "/habitat/id50/metag_cluster_habitat_50.tsv.xz"
INPUT_FILE_2 = "/habitat/id90/metag_cluster_habitat_90.tsv.xz"
OUTPUT_FILE_1 = "/habitat/id50/50AA_habitat.tsv.xz"
OUTPUT_FILE_2 = "/habitat/id90/90AA_habitat.tsv.xz"

less_more(INPUT_FILE_1,OUTPUT_FILE_1)
less_more(INPUT_FILE_2,OUTPUT_FILE_2)