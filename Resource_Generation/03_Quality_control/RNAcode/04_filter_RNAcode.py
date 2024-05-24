'''
Concept:
Filter RNAcode results for 100AA,90AA.
'''

def filter(file_dir,outfile):
    import os
    out = open(outfile, "wt")
    for n in range(1,288):
        first_dir = f'{file_dir}/first{n}'
        for m in range(1,301):
            second_dir = f'{first_dir}/second{m}'
            if os.listdir(second_dir):
                for infile in os.listdir(second_dir):
                    file_path = f'{second_dir}/{infile}'
                    with open(file_path) as f:
                        for line in f:
                            linelist = line.strip().split("\t")
                            if float(linelist[-1]) < 0.05:
                                filesplit = infile.split(".")
                                name = filesplit[0]+"."+filesplit[1]+"."+filesplit[2]
                                out.write(f'{name}\n')
                                break
            else:
                break
    out.close()

def true_false_100AA_90AA(infile1,infile2,outfile1,outfile2,outfile3):
    out1 = open(outfile1,"wt")
    out2 = open(outfile2,"wt")
    out3 = open(outfile3,"wt")

    true_90AA = set()

    with open(infile1,"rt") as f1:
        for line in f1:
            true_90AA.add(line.strip())
         
    with open(infile2,"rt") as f2:
        for line in f2:
            cluster,member = line.strip().split("\t")
            if cluster in true_90AA:
                out1.write(f'{member}\n')
            else:
                out2.write(f'{member}\n')
                out3.write(f'{cluster}\n')
    out1.close() 
    out2.close()
    out3.close()

def file_name(file_dir,outfile):
    import os

    out = open(outfile, "w")
    for n in range(1,288):
        first_dir = f'{file_dir}/first{n}'
        for m in range(1,301):
            second_dir = f'{first_dir}/second{m}'
            for infile in os.listdir(second_dir):
                file_path = f'{second_dir}/{infile}'
                name = infile.replace('.fna.aln.tsv','')
                with open(file_path) as f:
                    linelist = f.readline().strip().split('\t')
                    if len(linelist) >1:
                        out.write(f'{name}\t{linelist[10]}\n')
    out.close()

def full_90(infile,outfile):
    metaT = {}
    with open(infile,'rt') as f:
        for line in f:
            cluster,number = line.strip().split('\t')
            metaT[cluster] = number

    with open(outfile,'wt') as out:
        for i in range(287926875):
            nf = f'{i:09}'
            name = f'GMSC10.90AA.{nf[:3]}_{nf[3:6]}_{nf[6:9]}'
            if name in metaT.keys():
                out.write(f'{name}\t{metaT[name]}\n')
            else:
                out.write(f'{name}\tNA\n')

def full_100(infile1,infile2,outfile):
    import gzip

    rnacode = {}
    with open(infile1,'rt') as f:
        for line in f:
            cluster,number = line.strip().split('\t')
            rnacode[cluster] = number

    with open(outfile,'wt') as out:
        with gzip.open(infile2,'rt') as f:
            for line in f:
                member,cluster = line.strip().split('\t')
                if cluster in rnacode.keys():
                    out.write(f'{member}\t{rnacode[cluster]}\n')
                else:
                    out.write(f'{member}\tNA\n')

INPUT_DIR = "./rnacode"
INPUT_FILE_1 = "GMSC.cluster_filter.tsv"
OUTPUT_FILE_1 = "rnacode_true_90AA.tsv"
OUTPUT_FILE_2 = "rnacode_true_100AA.tsv"
OUTPUT_FILE_3 = "rnacode_false_100AA.tsv"
OUTPUT_FILE_4 = "rnacode_false_90AA.tsv"

filter(INPUT_DIR,OUTPUT_FILE_1)
true_false_100AA_90AA(OUTPUT_FILE_1,INPUT_FILE_1,OUTPUT_FILE_2,OUTPUT_FILE_3,OUTPUT_FILE_4)

OUTPUT_FILE_5 = "90AA_RNAcode_p.tsv"
file_name(INPUT_DIR,OUTPUT_FILE_5)

OUTPUT_FILE_6 = '90AA_RNAcode.tsv'
full_90(OUTPUT_FILE_5,OUTPUT_FILE_6)

INPUT_FILE_3 = 'GMSC.cluster.tsv.gz'
OUTPUT_FILE_7 = '100AA_RNAcode.tsv'
full_100(INPUT_FILE_2,INPUT_FILE_3,OUTPUT_FILE_7)