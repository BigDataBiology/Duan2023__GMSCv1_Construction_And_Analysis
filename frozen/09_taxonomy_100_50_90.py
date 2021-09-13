'''
Generate taxonomy mapping file.
'''

import lzma

def gettaxa_100(infile1,infile2,outfile):
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
            if linelist[0] in tax.keys():
                out.write(linelist[1]+"\t"+tax[linelist[0]]+"\n")
            else:
                out.write(linelist[1]+"\n")
    out.close()

def gettaxa_50_90(infile1,infile2,outfile):
    import lzma
    tax = {}
    out = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t",2)
            if len(linelist) == 3:
                tax[linelist[0]] = linelist[2]
            else:
                continue

    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")             
            if linelist[0] in tax.keys():
                out.write(linelist[1]+"\t"+tax[linelist[0]]+"\n")
            else:
                out.write(linelist[1]+"\n")
    out.close()

INPUT_FILE_1 = "/taxa/metag/id100/100AA_tax.tsv.xz"   
INPUT_FILE_2 = "/data/frozen/100AA_rename.tsv.xz"
INPUT_FILE_3 = "/taxa/metag/id50/50AA_tax.tsv.xz" 
INPUT_FILE_4 = "/data/frozen/50AA_rename.tsv.xz"
INPUT_FILE_5 = "/taxa/metag/id90/90AA_tax.tsv.xz"
INPUT_FILE_6 = "/data/frozen/90AA_rename.tsv.xz" 
OUTPUT_FILE_1 = "/data/frozen/100AA_taxonomy.tsv.xz" 
OUTPUT_FILE_2 = "/data/frozen/50AA_ref_taxonomy.tsv.xz" 
OUTPUT_FILE_3 = "/data/frozen/90AA_ref_taxonomy.tsv.xz"

gettaxa_100(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
gettaxa_50_90(INPUT_FILE_3,INPUT_FILE_4,OUTPUT_FILE_2)
gettaxa_50_90(INPUT_FILE_5,INPUT_FILE_6,OUTPUT_FILE_3)