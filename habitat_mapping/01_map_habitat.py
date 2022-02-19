'''
Concept:
Map habitat for all the smORFs from metaG.
We split all the smORFs into 8 subfiles because of its large number.
Map habitat to raw data non-redundant cluster.
'''

import gzip
import lzma

'''
Map habitat for all the smORFs from metaG.
Split all the smORFs into 8 subfiles.
'''
def habitat(infile1,infile2,outpath):
    micro_host = {}
    f = {}
    for i in range(1,9):
        outfile = outpath+"_"+str(i)+".tsv.xz"
        f["out{0}".format(i)] = lzma.open(outfile, "wt") 
    n = 0
    with open(infile1,'r',encoding = 'utf-8') as f1:
        for line in f1:
            line = line.strip()
            if line.startswith("sample"):
                continue
            else:
                linelist = line.split("\t")
                if len(linelist) > 20:
                    if linelist[20] != "":
                        micro_host[linelist[0]] = linelist[9]+" # "+linelist[20]
                else:
                    micro_host[linelist[0]] = linelist[9]
    with lzma.open(infile2,'rt') as f2:
        for line in f2:
            line = line.strip()
            if line.startswith("#GMSC"):
                continue
            else:
                linelist = line.split("\t")
                if n < 600000000:
                    f["out1"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")
                elif n >= 600000000 and n < 1200000000:
                    f["out2"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")
                elif n >= 1200000000 and n < 1800000000:
                    f["out3"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")
                elif n >= 1800000000 and n < 2400000000:
                    f["out4"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")
                elif n >= 2400000000 and n < 3000000000:
                    f["out5"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")
                elif n >= 3000000000 and n < 3600000000:
                    f["out6"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")
                elif n >= 3600000000 and n < 4200000000:
                    f["out7"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")                
                else:
                    f["out8"].write(linelist[0]+"\t"+micro_host[linelist[1]]+"\n")
                n += 1
    for i in range(1,9):
        f["out{0}".format(i)].close()

'''
Map habitat to raw data non-redundant cluster.
'''
def map_cluster(infile1,infile2,outfile):
    habitat = {}
    out = lzma.open(outfile, "wt")
            
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t",1)
            if len(linelist) == 2:
                habitat[linelist[0]] = linelist[1]
            else:
                continue           

    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t") 
            number = int(''.join(linelist[1].split(".")[2].split("_")))
            if number < 34617405: #The habitat of smORFs from Progenome is named isolate.
                out.write(linelist[0]+"\t"+linelist[1]+"\t"+"isolate"+"\n")
            else:
                if linelist[1] in habitat.keys():
                    out.write(linelist[0]+"\t"+linelist[1]+"\t"+habitat[linelist[1]]+"\n")
                else:
                    out.write(line+"\n")           
    out.close()


INPUT_FILE_1 = "/habitat/metadata.tsv"
INPUT_FILE_2 = "GMSC10.metag_smorfs.rename.txt.xz"
INPUT_FILE_3 = "dedup_cluster.tsv.gz"
OUT_PATH_1 = "/habitat/metag_habitat"
OUT_PATH_2 = "/habitat/metag_cluster_habitat" 

habitat(INPUT_FILE_1,INPUT_FILE_2,OUT_PATH_1)
for i in range(1,9):
    INPUT_FILE_4 = OUT_PATH_1+"_"+str(i)+".tsv.xz"
    INPUT_FILE_5 = OUT_PATH_2+"_"+str(i-1)+".tsv.xz"
    OUTPUT_FILE = OUT_PATH_2+"_"+str(i)+".tsv.xz"
    if i == 1:
        map_cluster(INPUT_FILE_4,INPUT_FILE_3,OUTPUT_FILE)
    else:
        map_cluster(INPUT_FILE_4,INPUT_FILE_5,OUTPUT_FILE)