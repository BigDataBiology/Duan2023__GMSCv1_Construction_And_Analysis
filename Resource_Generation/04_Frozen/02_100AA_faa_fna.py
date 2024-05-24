'''
Concept:
Generate rename and sequence of 100AA faa and fna.
'''

def getseq(infile1,infile2,outfile):   
    from fasta import fasta_iter
    import lzma
    
    name = {}
    out = lzma.open(outfile, "wt")
    
    with open(infile1,"rt") as f1:
        for line in f1:
            old,new = line.strip().split("\t")
            name[old] = new
  
    for ID,seq in fasta_iter(infile2):
        if ID in name.keys():
            out.write(f'>{name[ID]}\n{seq}\n')           
    out.close()        

INPUT_FILE_1 = "100AA_rename.tsv"  
INPUT_FILE_2 = "metag_ProG_dedup.faa.gz"
INPUT_FILE_3 = "GMSC10.metag_smorfs.fna.xz"
INPUT_FILE_4 = "GMSC.ProGenomes2.smorfs.fna.xz"
OUTPUT_FILE_1 = "100AA_GMSC.faa.xz"
OUTPUT_FILE_2 = "100AA_metag.fna.xz"
OUTPUT_FILE_3 = "100AA_prog.fna.xz"

getseq(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
getseq(INPUT_FILE_1,INPUT_FILE_3,OUTPUT_FILE_2)
getseq(INPUT_FILE_1,INPUT_FILE_4,OUTPUT_FILE_3)