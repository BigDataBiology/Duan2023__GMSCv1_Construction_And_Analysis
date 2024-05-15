'''
Concept:
Map taxid for smORFs from metaG based on contigs.
Get fullname of taxonomy of taxid according to GTDB files.
'''

import lzma

'''
Map taxid for smORFs from metaG according to contig.
'''
def maptax(infile1,infile2,outfile):   
    lastsample = ""
    taxa = {}
    out = lzma.open(outfile, "wt") 

    f2 = lzma.open(infile2,"rt")
    metag = f2.readline().strip().split("\t")

    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            linelist = line.strip().split("\t")
            if line.startswith("sample"):
                continue
            else:
                sample = linelist[0]
                contig1 = linelist[0]+linelist[1]
                taxid = linelist[2]
                if sample == lastsample:
                    taxa[contig1] = taxid
                else:
                    if taxa:
                        while metag[1] == lastsample:
                            contig2 = metag[1]+metag[2].split(" # ")[0].split("_")[0]+"_"+metag[2].split(" # ")[0].split("_")[1]
                            if contig2 in taxa.keys():
                                out.write(f'{metag[0]}\t{taxa[contig2]}\n')   
                            else:
                                out.write(f'{metag[0]}\n')
                            metag = f2.readline().strip().split("\t")
                            if metag == [""]:
                                break
                            else:
                                continue
                        taxa = {}
                        taxa[contig1] = taxid                        
                        lastsample = sample
                    else:
                        taxa[contig1] = taxid
                        lastsample = sample
    if taxa:
        while metag[1] == lastsample:
            contig2 = metag[1]+metag[2].split(" # ")[0].split("_")[0]+"_"+metag[2].split(" # ")[0].split("_")[1]
            if contig2 in taxa.keys():
                out.write(f'{metag[0]}\t{taxa[contig2]}\n')   
            else:
                out.write(f'{metag[0]}\n')
            metag = f2.readline().strip().split("\t")
            if metag == [""]:
                break
            else:
                continue                    
    out.close()        
    f2.close()

'''
Get fullname of taxonomy of taxid according to GTDB files.
'''
def fulltax(infile1,infile2,outfile):   
    outf = open(outfile, "wt")
    taxid = set()
    taxonomy = []

    with open(infile1,"rt") as f1:
        for line in f1:
            linelist = line.strip().split("\t")
            taxonomy.append(linelist[1])
            
    with lzma.open(infile2,"rt") as f2:      
        for line in f2:
            linelist = line.strip().split("\t")
            if line.startswith("sample"):
                continue
            else:
                if linelist[2] in taxid:
                    continue
                else:
                    taxid.add(linelist[2])
                    flag = 0
                    if linelist[3] == "superkingdom":
                        tax = "d__"+linelist[4]
                        outf.write(f'{linelist[2]}\t{tax}\n')
                    else:
                        tax = linelist[3][0]+"__"+linelist[4]
                        for i in range(len(taxonomy)):
                            if tax in taxonomy[i]:
                                outf.write(linelist[2]+"\t")
                                fulltax = taxonomy[i].split(";")
                                if tax.startswith("p"):
                                    rank = 1
                                elif tax.startswith("c"):
                                    rank = 2
                                elif tax.startswith("o"):
                                    rank = 3
                                elif tax.startswith("f"):
                                    rank = 4
                                elif tax.startswith("g"):
                                    rank = 5
                                else:
                                    rank = 6
                                for i in range(rank):
                                    outf.write(fulltax[i]+"\t")
                                outf.write(fulltax[i+1]+"\n")
                                flag = 1
                                break
                        if flag == 0:
                            outf.write(f'{linelist[2]}\n')

    outf.close()

INPUT_FILE_1 = "mmseqs2.lca_taxonomy.full.tsv.xz"  
INPUT_FILE_2 = "GMSC10.metag_smorfs.rename.txt.xz"
INPUT_FILE_3 = "gtdb_taxonomy.tsv"
OUTPUT_FILE_1 = "metag_taxid.tsv.xz"
OUTPUT_FILE_2 = "taxid_fullname_gtdb.tsv"

maptax(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
fulltax(INPUT_FILE_3,INPUT_FILE_1,OUTPUT_FILE_2)