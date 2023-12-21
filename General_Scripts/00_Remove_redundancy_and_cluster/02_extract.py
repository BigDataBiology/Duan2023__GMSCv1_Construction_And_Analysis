'''
Concept:
Extract non-singletons and singletons according to metag_ProG.raw_number.tsv.gz.
'''
from jug import TaskGenerator
from fasta import fasta_iter
import gzip

@TaskGenerator
def extract_seq(infile1,infile2,outfile1,outfile2):
    fastaset = set()
    with gzip.open(infile1,"rt") as f:
        for line in f:
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] != "1":
                fastaset.add(linelist[1])

    with gzip.open(outfile1, "wt", compresslevel=1) as out1, \
        gzip.open(outfile2, "wt", compresslevel=1) as out2:
        for ID,seq in fasta_iter(infile2):
            if seq in fastaset:
                out1.write(f'>{ID}\n{seq}\n')
            else:
                out2.write(f'>{ID}\n{seq}\n')


INPUT_FILE_1 = "metag_ProG.raw_number.tsv.gz"
INPUT_FILE_2 = "metag_ProG_dedup.faa.gz"
OUT_FILE_1 = "metag_ProG_nonsingleton.faa.gz"
OUT_FILE_2 = "metag_ProG_singleton.faa.gz"
extract_seq(INPUT_FILE_1,INPUT_FILE_2,OUT_FILE_1,OUT_FILE_2)
