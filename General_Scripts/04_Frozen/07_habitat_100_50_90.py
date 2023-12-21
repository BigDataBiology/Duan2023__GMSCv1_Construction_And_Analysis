'''
Generate habitat mapping 100AA/90AA file.
'''

import lzma

def gethabitat_100(infile1,infile2,outfile):
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

    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")             
            if linelist[0] in habitat.keys():
                out.write(linelist[1]+"\t"+habitat[linelist[0]]+"\n")
            else:
                out.write(linelist[1]+"\n")
    out.close()

def gethabitat_90(infile1,infile2,outfile):
    habitat = {}
    out = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) == 3:
                habitat[linelist[0]] = linelist[2]
            else:
                continue

    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")             
            if linelist[0] in habitat.keys():
                out.write(linelist[1]+"\t"+habitat[linelist[0]]+"\n")
            else:
                out.write(linelist[1]+"\n")
    out.close()

       
INPUT_FILE_1 = "./habitat/id100/100AA_multi_general_habitat.tsv.xz"   
INPUT_FILE_2 = "./data/frozen/100AA_rename.tsv.xz"
INPUT_FILE_3 = "./habitat/id90/90AA_multi_general_habitat.tsv.xz"   
INPUT_FILE_4 = "./data/frozen/90AA_rename.tsv.xz"
OUTPUT_FILE_1 = "./data/frozen/100AA_ref_multi_habitat.tsv.xz"
OUTPUT_FILE_2 = "./data/frozen/90AA_ref_multi_habitat.tsv.xz" 

gethabitat_100(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
gethabitat_90(INPUT_FILE_3,INPUT_FILE_4,OUTPUT_FILE_2)