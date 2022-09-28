'''
Concept:
If the taxonomy of smORFs in a cluster is different, we annotated taxonomy using LCA. 
But we ignored the blank to make it more specific.
Extract 100% identity smORFs with taxonomy.
'''

import lzma

def deep_lca(infile1,outfile):
    cluster = {}
    taxa = {}
    change = {}
    lastrank = ""
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
                        change[key] = []
                        for rank in range(7):
                            flag = 1
                            for i in range(len(value)):
                                if taxa[value[i]]:
                                    if len(taxa[value[i]]) >= rank+1:
                                        if lastrank == "":
                                            lastrank = taxa[value[i]][rank]
                                        else:
                                            if taxa[value[i]][rank] != lastrank:
                                                flag = 0
                                                lastrank = ""
                                                break
                                            else:
                                                continue
                                    else:
                                        continue
                                else:                                    
                                    continue
                            if flag == 1:
                                if lastrank != "":
                                    change[key].append(lastrank)
                                    lastrank = ""                                      
                                else:
                                    lastrank = ""
                                    break
                            else:
                                break         
                        if change[key]:       
                            taxonomy = change[key][0]
                            for m in range(1,len(change[key])):
                                taxonomy = taxonomy+"\t"+change[key][m] 
                            for n in range(len(value)):
                                out.write(key+"\t"+value[n]+"\t"+taxonomy+"\n")
                        else:
                            for n in range(len(value)):
                                out.write(key+"\t"+value[n]+"\n")                      
                    cluster = {}
                    taxa = {}
                    change = {}
                    cluster[linelist[0]] = [linelist[1]]
            else:
                cluster[linelist[0]] = [linelist[1]]                
            taxa[linelist[1]] = []
            for i in range(2,len(linelist)):
                taxa[linelist[1]].append(linelist[i])               
    for key,value in cluster.items():
        change[key] = []
        for rank in range(7):
            flag = 1
            for i in range(len(value)):
                if taxa[value[i]]:
                    if len(taxa[value[i]]) >= rank+1:
                        if lastrank == "":
                            lastrank = taxa[value[i]][rank]
                        else:
                            if taxa[value[i]][rank] != lastrank:
                                flag = 0
                                lastrank = ""
                                break
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if flag == 1:
                if lastrank != "":
                    change[key].append(lastrank)
                    lastrank = ""
                else:
                    lastrank = ""
                    break   
            else:
                break 
        if change[key]:              
            taxonomy = change[key][0]
            for m in range(1,len(change[key])):
                taxonomy = taxonomy+"\t"+change[key][m] 
            for n in range(len(value)):
                out.write(key+"\t"+value[n]+"\t"+taxonomy+"\n")
        else:
            for n in range(len(value)):
                out.write(key+"\t"+value[n]+"\n")                     
    out.close()

'''
Extract 100% identity smORFs with taxonomy.
'''
def extract(infile1,infile2,outfile):
    import gzip
    import lzma
    smorf = set()
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

INPUT_FILE_1 = "./taxa/metag/metag_cluster_taxonomy.tsv.xz"
INPUT_FILE_2 = "./clust_result/result/all_0.5_0.9.tsv.gz"
OUTPUT_FILE_1 = "./taxa/metag/deep_lca/metag_cluster_tax_all_dlca.tsv.xz"
OUTPUT_FILE_2 = "./taxa/metag/id100/100AA_taxonomy.tsv.xz" 
deep_lca(INPUT_FILE_1,OUTPUT_FILE_1)
extract(INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_2)