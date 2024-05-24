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
            member,cluster = line.strip().split("\t")
            smorf.add(member)

    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            linelist = line.strip().split("\t",2)
            if linelist[1] in smorf:
                if len(linelist) == 3:
                    out.write(f'{linelist[1]}\t{linelist[2]}\n')
                else:
                    out.write(f'{linelist[1]}\n')
            else:
                continue
    out.close()

INPUT_FILE_1 = "metag_cluster_taxonomy.tsv.xz"
INPUT_FILE_2 = "GMSC.cluster.tsv.gz"
OUTPUT_FILE_1 = "metag_cluster_tax_all_dlca.tsv.xz"
OUTPUT_FILE_2 = "100AA_taxonomy.tsv.xz" 
deep_lca(INPUT_FILE_1,OUTPUT_FILE_1)
extract(INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_2)