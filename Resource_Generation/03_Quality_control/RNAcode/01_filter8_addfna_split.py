'''
Concept:
Filter 90% identity clusters which contain >= 8 sequences.
Select fna for RNAcode.
Split every clusters into a single .fna file.
'''

import lzma
import gzip

'''
Filter 90% identity clusters which contain >= 8 sequences.
'''
def filter_eight(infile,outfile):    
    allname = {}
    out = open(outfile, "wt")
    with gzip.open(infile,'rt') as f1:
        for line in f1:
            member,cluster = line.strip("\n").split("\t")
            if cluster in allname.keys():
                allname[cluster][1] += 1
                allname[cluster][0].append(member)
            else:
                allname[cluster] = [[member], 1]
    
    for key,(namelist,count) in sorted(allname.items(), key=lambda item:item[1][1]):
        if count >= 8:
            for item in namelist:
                out.write(f'{key}\t{item}\n')
    out.close() 

'''
Add fna for RNAcode.
'''
def addfna(infile1,infile2,outfile):
    from fasta import fasta_iter

    name = {}
    out = open(outfile, "wt")
    with open(infile1,'rt') as f1:
        for line in f1:
            member,cluster = line.strip().line.split("\t") 
            name[member] = cluster

    for h,seq in fasta_iter(infile2):
        if h in name.keys():
            out.write(f'{name[h]}\t{h}\t{seq}\n')
    out.close()    

'''
Reorder the name.
'''
def order(infile,outfile):
    namedict = {}
    with open(infile) as f:
        for line in f:
            cluster,seq = line.strip().split("\t",1)
            if cluster not in namedict.keys():
                namedict[cluster] = []
            namedict[cluster].append(seq)

    with open(outfile,'wt') as out:
        for key,value in namedict.items():
            for item in value:
                out.write(f'{key}\t{item}\n')
 
'''
Split each cluster into a single .fna file.
We move all the .fna files into a hierarchical file structure(300*300*300) for the limitation of the file system.
'''
def split(infile,outpath):
    name = set()
    n = 1
    m = 1
    x = 1
    with open (infile) as f1:
        for line in f1 :
            cluster,member,seq = line.strip().split("\t")
            if cluster not in name:
                name.add(cluster)
                if x > 300:
                    m += 1
                    x = 1
                if m > 300:
                    n += 1
                    m = 1
                    x = 1
                out = open(f'{outpath}/first{n}/second{m}/{cluster}.fna', "wt")
                out.write(f'>{member}\n{seq}\n')
                x += 1
            else:
                out.write(f'>{member}\n{seq}\n')
    out.close()   

INPUT_FILE_1 = "GMSC.cluster.tsv.gz"
INPUT_FILE_2 = "metag_ProG_smorfs.fna.xz"
OUT_FILE_1 = "GMSC.cluster_filter.tsv"
OUT_FILE_2 = "GMSC.cluster_filter_fna.tsv"
OUT_FILE_3 = "GMSC.cluster_fna_order.tsv"
SPLIT_FILE_PAT = "./split/"

filter_eight(INPUT_FILE_1,OUT_FILE_1)
addfna(OUT_FILE_1,INPUT_FILE_2,OUT_FILE_2)
order(OUT_FILE_2,OUT_FILE_3)
split(OUT_FILE_3,SPLIT_FILE_PAT)