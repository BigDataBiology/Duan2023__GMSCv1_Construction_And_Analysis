'''
Concept:
Generate rename and sequence of 100AA faa and fna.
'''

def getseq(infile1,infile2,outfile):   
    from fasta import fasta_iter
    import lzma
    name = {}
    out1 = lzma.open(outfile, "wt")
    
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            name[linelist[0]] = linelist[1] 
  
    for ID,seq in fasta_iter(infile2):
        if ID in name.keys():
            out1.write(f'>{name[ID]}\n{seq}\n')           
    out1.close()        

INPUT_FILE_1 = "./data/100AA_rename.tsv.xz"  
INPUT_FILE_2 = "./data/metag_ProG_dedup.faa.gz"
INPUT_FILE_3 = "GMSC10.metag_smorfs.fna.xz"
INPUT_FILE_4 = "GMSC.ProGenomes2.smorfs.fna.xz"
OUTPUT_FILE_1 = "./data/frozen/100AA_GMSC.faa.xz"
OUTPUT_FILE_2 = "./data/frozen/100AA_metag.fna.xz"
OUTPUT_FILE_3 = "./data/frozen/100AA_prog.fna.xz"

getseq(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
getseq(INPUT_FILE_1,INPUT_FILE_3,OUTPUT_FILE_2)
getseq(INPUT_FILE_1,INPUT_FILE_4,OUTPUT_FILE_3)