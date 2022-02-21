'''
Concept:
Filter 90% identity clusters which contain >= 8 sequences.
Add fna for RNAcode.
Split every clusters into a single .fna file.
'''

import lzma

'''
Filter 90% identity clusters which contain >= 8 sequences.
'''
def filter_eight(infile,outfile):    
    allname = {}
    out = open(outfile, "w")
    with open (infile) as f1:
        for line in f1 :
            line = line.strip("\n")
            linelist = line.split("\t")
            if linelist[2] != "":
                if linelist[2] in allname.keys():
                    allname[linelist[2]][1] += 1
                    allname[linelist[2]][0].append(linelist[0])
                else:
                    allname[linelist[2]] = [[linelist[0]], 1]
    
    for key,(namelist,count) in sorted(allname.items(), key=lambda item:item[1][1]):
        if count >= 8:
            for i in range(len(namelist)):
                out.write(key+"\t"+namelist[i]+"\n")
    out.close() 

'''
Add fna for RNAcode.
'''
def addfna(infile1,infile2,outfile):
    name = {}
    out = open(outfile, "w")
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")    
            name[linelist[1]] = linelist[0]
            
    with lzma.open(infile2, 'rt') as f2:
        for line in f2:
            line = line.strip()
            if line.startswith(">"):
                index = line.strip(">")
            else:
                if index in name.keys():
                    out.write(name[index]+"\t"+index+"\t"+line+"\n")
    out.close()    

'''
Reorder the name.
'''
def order(infile1,infile2,outfile):
    namedict = {}
    out = open(outfile, "w")
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")   
            name = linelist[0]+"\t"+linelist[1]
            namedict[name] = linelist[2]
    with open (infile2) as f1:
        for line in f1 :
            line = line.strip()
            if line in namedict.keys():
                out.write(line+"\t"+namedict[line]+"\n")    
    out.close() 

'''
Split every clusters into a single .fna file.
The number of clusters (>=8 sequences) is 25,744,932.
We move all the .fna files into a hierarchical file structure(300*300*300) for the limitation of the file system.
'''
def split(infile,outfile):
    name = set()
    n = 1
    m = 1
    x = 1
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t") 
            if linelist[0] not in name:
                name.add(linelist[0])
                if x > 300:
                    m += 1
                    x = 1
                if m > 300:
                    n += 1
                    m = 1
                    x = 1
                out = open(outfile+"first"+str(n)+"/second"+str(m)+"/"+linelist[0]+".fna", "w")
                out.write(">"+linelist[1]+"\n"+linelist[2]+"\n")
                x += 1
            else:
                out.write(">"+linelist[1]+"\n"+linelist[2]+"\n")
    out.close()   

INPUT_FILE_1 = "/clust_result/result/all_0.5_0.9.tsv"
INPUT_FILE_2 = "/data/metag_ProG_smorfs.fna.xz"
OUT_FILE_1 = "/clust_result/result/all_0.5_0.9_filter.tsv"
OUT_FILE_2 = "/RNAcode_result/all_0.5_0.9_filter_fna.tsv"
OUT_FILE_3 = "/RNAcode_result/all_0.5_0.9_filter_fna_order.tsv"
SPLIT_FILE_PAT = "/RNAcode_result/split/"

filter_eight(INPUT_FILE_1,OUT_FILE_1)
addfna(OUT_FILE_1,INPUT_FILE_2,OUT_FILE_2)
order(OUT_FILE_2,OUT_FILE_1,OUT_FILE_3)
split(OUT_FILE_3,SPLIT_FILE_PAT)