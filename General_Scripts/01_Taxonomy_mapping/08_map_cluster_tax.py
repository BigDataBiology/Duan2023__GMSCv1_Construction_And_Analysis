'''
Concept:
Map taxonomy to 90% identity clusters.
If the taxonomy of smORFs in a cluster is different, we annotated taxonomy using LCA. 
But we ignored the blank to make it more specific.
'''

import lzma
import gzip

'''
Map taxonomy to 90% identity clusters.
'''
def metag_full(infile1,infile2,outfile):
    tax = {}
    out = lzma.open(outfile, "wt")

    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            linelist = line.strip().split("\t",1)
            if len(linelist) == 2:
                tax[linelist[0]] = linelist[1]
            else:
                continue

    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            member,cluster = line.strip().split("\t") 
            if member in tax.keys():
                out.write(f'{cluster}\t{member}\t{tax[member]}\n')
            else:
                out.write(f'{cluster}\t{member}\n')
    out.close()
    
def deep_lca(infile1,outfile):
    cluster = {}
    taxa = {}
    change = {}
    lastrank = ""

    out = lzma.open(outfile, "wt")

    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            linelist = line.strip().split("\t")     
            if cluster:
                if linelist[0] in cluster.keys():
                    cluster[linelist[0]].append(linelist[1])
                else:
                    for key,value in cluster.items():
                        change[key] = []
                        for rank in range(7):
                            flag = 1
                            for item in value:
                                if taxa[item]:
                                    if len(taxa[item]) >= rank+1:
                                        if lastrank == "":
                                            lastrank = taxa[item][rank]
                                        else:
                                            if taxa[item][rank] != lastrank:
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
                            for item in value:
                                out.write(f'{key}\t{item}\t{taxonomy}\n')
                        else:
                            for item in value:
                                out.write(f'{key}\t{item}\n')                      
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
            for item in value:
                if taxa[item]:
                    if len(taxa[item]) >= rank+1:
                        if lastrank == "":
                            lastrank = taxa[item][rank]
                        else:
                            if taxa[item][rank] != lastrank:
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
            for item in value:
                out.write(f'{key}\t{item}\t{taxonomy}\n')
        else:
            for item in value:
                out.write(f'{key}\t{item}\n')                        
    out.close()

INPUT_FILE_1 = "100AA_taxonomy.tsv.xz"   
INPUT_FILE_2 = "GMSC.cluster.tsv.gz"  
OUTPUT_FILE_1 = "metag_cluster_tax_90.tsv.xz" 
OUTPUT_FILE_2 = "90AA_tax.tsv.xz"

metag_full(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
deep_lca(OUTPUT_FILE_1,OUTPUT_FILE_2)