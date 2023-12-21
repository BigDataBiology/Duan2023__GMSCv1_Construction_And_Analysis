'''
Concept:
Generate original name - 100AA rename list.
Peptides are named: >GMSC10.100AA.XXX_XXX_XXX
Numbers were assigned in order of increasing number of copies. 
So that the lower the number, the lower the number of copies of that peptide was present in the input data. 
And if the number of copies is same, numbers were assigned in order of letters of peptides.
'''

def sort(infile,outfile,n,prefix):
    from operator import itemgetter   
    import gzip
    seqnumber_list=[]
    with gzip.open(infile,"rt") as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] != "1":
                seqnumber_tup = (int(linelist[0]),linelist[1])
                seqnumber_list.append(seqnumber_tup)
    sortseqnumber_list=sorted(seqnumber_list,key=itemgetter(0,1))
    with open(outfile,"wt") as out:
        for i in range (len(seqnumber_list)):
            nf = f'{n:09}'
            out.write(f'{sortseqnumber_list[i][0]}\t{sortseqnumber_list[i][1]}\t{prefix}.{nf[:3]}_{nf[3:6]}_{nf[6:9]}\n')
            n += 1

def rename_nonsingleton(infile1,infile2,outfile):
    from fasta import fasta_iter
    fastadict={}
    for ID,seq in fasta_iter(infile1):
        fastadict[seq] = ID
    out = open(outfile, "w")
    with open (infile2) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")
            name = fastadict[linelist[1]]
            newname = linelist[2]
            out.write(f'{name}\t{newname}\n')
    out.close()   

def rename_singleton(infile1,infile2,outfile,n,prefix):
    from fasta import fasta_iter
    name=set()
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")
            name.add(linelist[0])
    out = open(outfile, "w")
    for ID,seq in fasta_iter(infile2):
        if ID in name:
            nf = f'{n:09}'
            out.write(f'{ID}\t{prefix}.{nf[:3]}_{nf[3:6]}_{nf[6:9]}\n')
            n += 1
    out.close()          

INPUT_FILE_1 = "metag_ProG.raw_number.tsv.gz"
INPUT_FILE_2 = "metag_ProG_nonsingleton.faa.gz"
INPUT_FILE_3 = "singleton_0.5_0.9.tsv"
INPUT_FILE_4 = "metag_ProG_singleton.faa.gz"
OUTPUT_FILE_1 = "nonsingleton_rename_seq.tsv"
OUTPUT_FILE_2 = "nonsingleton_rename.tsv"
OUTPUT_FILE_3 = "singleton_rename.tsv"

sort(INPUT_FILE_1,OUTPUT_FILE_1,547356980,'GMSC10.100AA')
rename_nonsingleton(INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_2)
rename_singleton(INPUT_FILE_3,INPUT_FILE_4,OUTPUT_FILE_3,0,'GMSC10.100AA')