'''
Concept:
Map taxonomy for all the smORFs from metaG.
We split all the smORFs into 8 subfiles because of its large number.
Map taxonomy to raw data non-redundant cluster.
'''

import gzip
import lzma

'''
Map taxonomy for all the smORFs from metaG.
Split all the smORFs into 8 subfiles.
'''
def metag_full(infile1,infile2,outpath):
    n = 0
    tax = {}
    f = {}
    for i in range(1,9):
        outfile = outpath+"_"+str(i)+".tsv.xz"
        f["out{0}".format(i)] = lzma.open(outfile, "wt")     
    out = lzma.open(outfile, "wt")
    with open(infile1,"rt") as f1:
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
            if n < 600000000:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out1"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out1"].write(linelist[0]+"\n")
                else:
                    f["out1"].write(linelist[0]+"\n")          
            elif n >= 600000000 and n < 1200000000:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out2"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out2"].write(linelist[0]+"\n")
                else:
                    f["out2"].write(linelist[0]+"\n") 
            elif n >= 1200000000 and n < 1800000000:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out3"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out3"].write(linelist[0]+"\n")
                else:
                    f["out3"].write(linelist[0]+"\n") 
            elif n >= 1800000000 and n < 2400000000:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out4"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out4"].write(linelist[0]+"\n")
                else:
                    f["out4"].write(linelist[0]+"\n") 
            elif n >= 2400000000 and n < 3000000000:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out5"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out5"].write(linelist[0]+"\n")
                else:
                    f["out5"].write(linelist[0]+"\n") 
            elif n >= 3000000000 and n < 3600000000:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out6"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out6"].write(linelist[0]+"\n")
                else:
                    f["out6"].write(linelist[0]+"\n") 
            elif n >= 3600000000 and n < 4200000000:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out7"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out7"].write(linelist[0]+"\n")
                else:
                    f["out7"].write(linelist[0]+"\n")               
            else:
                if len(linelist) == 2:
                    if linelist[1] in tax.keys():
                        f["out8"].write(linelist[0]+"\t"+tax[linelist[1]]+"\n")
                    else:
                        f["out8"].write(linelist[0]+"\n")
                else:
                    f["out8"].write(linelist[0]+"\n") 
            n += 1            
    for i in range(1,9):
        f["out{0}".format(i)].close()

'''
Map taxonomy to raw data non-redundant cluster.
'''
def map_cluster(infile1,infile2,infile3,outfile):
    tax = {}
    n = 0
    out = lzma.open(outfile, "wt")
    with gzip.open(infile1,"rt") as f1:
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
            linelist = line.split("\t",1)
            if len(linelist) == 2:
                tax[linelist[0]] = linelist[1]
            else:
                continue    

    with gzip.open(infile3,"rt") as f4:
        for line in f4:
            line = line.strip()
            linelist = line.split("\t") 
            if linelist[1] in tax.keys():
                out.write(linelist[0]+"\t"+linelist[1]+"\t"+tax[linelist[1]]+"\n")
            else:
                out.write(linelist[0]+"\t"+linelist[1]+"\n")           
    out.close()

INPUT_FILE_1 = "/taxa/metag/taxid_fullname_gtdb.tsv"   
INPUT_FILE_2 = "/taxa/metag/metag_taxid.tsv.xz"
INPUT_FILE_3 = "dedup_cluster.tsv.gz"
INPUT_FILE_4 = "/taxa/progenome/prog_taxonomy_change.tsv.gz"  
OUT_PATH_1 = "/taxa/metag/metag_taxonomy" 
OUT_PATH_2 = "/taxa/metag/metag_cluster_taxonomy" 

metag_full(INPUT_FILE_1,INPUT_FILE_2,OUT_PATH_1)
for i in range(1,9):
    INPUT_FILE_5 = OUT_PATH_1+"_"+str(i)+".tsv.xz"
    INPUT_FILE_6 = OUT_PATH_2+"_"+str(i-1)+".tsv.xz"
    OUTPUT_FILE = OUT_PATH_2+"_"+str(i)+".tsv.xz"
    if i ==1:
        map_cluster(INPUT_FILE_5,INPUT_FILE_4,INPUT_FILE_3,OUTPUT_FILE)
    else:
        map_cluster(INPUT_FILE_5,INPUT_FILE_4,INPUT_FILE_6,OUTPUT_FILE)