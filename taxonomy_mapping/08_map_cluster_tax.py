'''
Concept:
Map taxonomy to 90% and 50% identity clusters.
If the taxonomy of smORFs in a cluster is different, we annotated taxonomy using LCA. 
But we ignored the blank to make it more specific.
'''

import lzma

'''
Map taxonomy to 90% and 50% identity clusters.
'''
def metag_full(infile1,infile2,outfile):
    tax = {}
    out = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t",1)
            if len(linelist) == 2:
                tax[linelist[0]] = linelist[1]
            else:
                continue

    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t") 
            if linelist[1] in tax.keys():
                out.write(linelist[0]+"\t"+linelist[1]+"\t"+tax[linelist[1]]+"\n")
            else:
                out.write(line+"\n")
    out.close()
    
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

INPUT_FILE_1 = "./taxa/metag/id100/100AA_taxonomy.tsv.xz"   
INPUT_FILE_2 = "all_cluster_0.9.tsv.xz"  
INPUT_FILE_3 = "all_cluster_0.5.tsv.xz"
OUTPUT_FILE_1 = "./taxa/metag/id90/metag_cluster_tax_90.tsv.xz" 
OUTPUT_FILE_2 = "./taxa/metag/id50/metag_cluster_tax_50.tsv.xz" 
OUTPUT_FILE_3 = "./taxa/metag/id90/90AA_tax.tsv.xz"
OUTPUT_FILE_4 = "./taxa/metag/id50/50AA_tax.tsv.xz"

metag_full(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
metag_full(INPUT_FILE_1,INPUT_FILE_3,OUTPUT_FILE_2)
deep_lca(OUTPUT_FILE_1,OUTPUT_FILE_3)
deep_lca(OUTPUT_FILE_2,OUTPUT_FILE_4)