'''
Merge the redundancy of smORFs into clusters for LCA.
'''

import gzip

def mergeall(infile1,infile2,outfile):   
    name = {}
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in name.keys():
                name[linelist[0]].append(linelist[1])
            else:
                name[linelist[0]] = [linelist[1]]
         
    out1 = gzip.open(outfile, "wt", compresslevel=1)         
    
    with open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            for i in range (len(name[linelist[1]])):
                out1.write(linelist[0]+"\t"+name[linelist[1]][i]+"\n")
    out1.close()             

def LCA(infile1,infile2,outfile):   
    import gzip
    name = {}
    cluster = {}
    change = {}
    taxa = set()
    flag = 1
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) == 11:
                kindom = linelist[4]
                phylum = linelist[5]
                cla = linelist[6] 
                order =  linelist[7]
                family = linelist[8]
                genus = linelist[9]
                species = linelist[10]
                name[linelist[1]] = [kindom,phylum,cla,order,family,genus,species]
            else:
                name[linelist[1]] = []           
    out1 = gzip.open(outfile, "wt", compresslevel=1)         
    
    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            rep = linelist[0] 
            smorf = linelist[1]
            if rep in cluster.keys():
                cluster[rep].append(smorf) 
                lastrep = rep
            else:
                if cluster:
                    cluster[rep] = [smorf]
                    for rank in range(7):
                        flag = 1
                        for i in range(len(cluster[lastrep])):
                            if taxa:
                                if name[cluster[lastrep][i]]:
                                    if name[cluster[lastrep][i]][6-rank] in taxa:
                                        continue
                                    else:
                                        flag = 0
                                        taxa = set()
                                        break
                                else:
                                    continue
                            else:
                                if name[cluster[lastrep][i]]:
                                    taxa.add(name[cluster[lastrep][i]][6-rank])
                                else:
                                    continue
                        if flag == 1:
                            taxa = set()
                            break
                    change[lastrep] = []
                    for j in range(7-rank):
                        if len(name[lastrep]) == 0 and len(cluster[lastrep]) == 1:
                            break
                        elif rank == 6 and flag == 0:
                            break
                        else:
                            for x in range(len(cluster[lastrep])):
                                if name[cluster[lastrep][x]]:
                                    change[lastrep].append(name[cluster[lastrep][x]][j])
                                    break
                                else:
                                    continue
                    for n in range(len(cluster[lastrep])):
                        out1.write(lastrep+"\t"+cluster[lastrep][n]+"\t")
                        if len(change[lastrep]) != 0 :
                            if len(change[lastrep]) != 1:
                                for m in range(len(change[lastrep])-1):
                                    out1.write(change[lastrep][m]+"\t")
                                out1.write(change[lastrep][m+1]+"\n")
                            else:
                                out1.write(change[lastrep][0]+"\n")
                        else:
                            out1.write("\n")
                    lastrep = rep
                else:
                    cluster[rep] = [smorf]
                    lastrep = rep
        for rank in range(7):
            flag = 1
            for i in range(len(cluster[lastrep])):
                if taxa:
                    if name[cluster[lastrep][i]]:
                        if name[cluster[lastrep][i]][6-rank] in taxa:
                            continue
                        else:
                            flag = 0
                            print(flag)
                            print(taxa)
                            taxa = set()
                            break
                    else:
                        continue
                else:
                    if name[cluster[lastrep][i]]:
                        taxa.add(name[cluster[lastrep][i]][6-rank])
                    else:
                        continue
            if flag == 1:
                taxa = set()
                break
        change[lastrep] = []
        for j in range(7-rank):
            if len(name[lastrep]) == 0 and len(cluster[lastrep]) == 1:
                break
            elif rank == 6 and flag == 0:
                break
            else:
                for x in range(len(cluster[lastrep])):
                    if name[cluster[lastrep][x]]:
                        change[lastrep].append(name[cluster[lastrep][x]][j])
                        break
                    else:
                        continue
        for n in range(len(cluster[lastrep])):
            out1.write(lastrep+"\t"+cluster[lastrep][n]+"\t")
            if len(change[lastrep]) != 0 :
                if len(change[lastrep]) != 1:
                    for m in range(len(change[lastrep])-1):
                        out1.write(change[lastrep][m]+"\t")
                    out1.write(change[lastrep][m+1]+"\n")
                else:
                    out1.write(change[lastrep][0]+"\n")
            else:
                out1.write("\n")
    out1.close()   

'''
Change the format of Progenome taxonomy to the same format of GTDB.
'''
def change(infile1,outfile):   
    out = gzip.open(outfile, "wt", compresslevel=1)
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            out.write(linelist[1])
            if len(linelist) > 2:
                for i in range(2,len(linelist)):
                    name = linelist[i].split("[")[0].lstrip('0123456789 ').replace("NA ","")
                    if i == 2:
                        fullname = "d__"+name
                        out.write("\t"+fullname)
                    if i == 3:
                        fullname = "p__"+name
                        out.write("\t"+fullname)
                    if i == 4:
                        fullname = "c__"+name
                        out.write("\t"+fullname)
                    if i == 5:
                        fullname = "o__"+name
                        out.write("\t"+fullname)
                    if i == 6:
                        fullname = "f__"+name
                        out.write("\t"+fullname)
                    if i == 7:
                        fullname = "g__"+name
                        out.write("\t"+fullname)
                    if i == 8:
                        fullname = "s__"+name
                        out.write("\t"+fullname)
                out.write("\n")        
            else:
                out.write("\n")
    out.close()       

INPUT_FILE_1 = "./taxa/progenome/prog_redundant.tsv.gz"  
INPUT_FILE_2 = "./taxa/progenome/clust_result/prog_dedup_0.9_clu.tsv"
INPUT_FILE_3 = "./taxa/progenome/prog_specI_genome_taxa.tsv.gz"  
OUTPUT_FILE_1 = "./taxa/progenome/prog_all_0.9_clu.tsv.gz"
OUTPUT_FILE_2 = "./taxa/progenome/all_taxonomy.tsv.gz"
OUTPUT_FILE_3 = "./taxa/progenome/prog_taxonomy_change.tsv.gz"

mergeall(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
LCA(INPUT_FILE_3,OUTPUT_FILE_1,OUTPUT_FILE_2)
change(OUTPUT_FILE_2,OUTPUT_FILE_3)