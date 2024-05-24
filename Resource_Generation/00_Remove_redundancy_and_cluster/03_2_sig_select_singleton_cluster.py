'''
Concept:
Extract non-singletons and singletons of each cluster.
Randomly select 1,000 singletons to check cluster significance.
'''

from fasta import fasta_iter
import random

def extract(infile1,infile2,outfile1,outfile2):
    fastaset = set()
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            fastaset.add(line)
    
    with open(outfile1,"w") as out1, \
        open(outfile2,"w") as out2:
        for ID,seq in fasta_iter(infile2):
            if ID in fastaset:
                out1.write(f'>{ID}\n{seq}\n')
            else:
                out2.write(f'>{ID}\n{seq}\n')

def select(infile,outfile,NR_SINGLETONS):
    selected = frozenset(random.sample(range(NR_SINGLETONS),1000))
    with open(outfile,'w') as out:
        n=0
        for ID,seq in fasta_iter(infile):
           n+=1
           if n in selected:
               out.write(f'>{ID}\n{seq}\n')

INPUT_FILE_1 = "0.9clu_singleton_name"
INPUT_FILE_2 = "metag_ProG_nonsingleton_0.9_clu_rep.faa"
OUT_FILE_1 = "0.9clu_singleton.faa"
OUT_FILE_2 = "0.9clu_nonsingleton.faa"
OUT_FILE_3 = "selected_singleton.faa"

extract(INPUT_FILE_1,INPUT_FILE_2,OUT_FILE_1,OUT_FILE_2)

NR_SINGLETONS_90 = 232027144

select(OUT_FILE_1,OUT_FILE_3,NR_SINGLETONS_90)
