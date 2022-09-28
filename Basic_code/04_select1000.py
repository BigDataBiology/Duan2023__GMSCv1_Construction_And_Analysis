'''
Concept:
Extract non-singletons and singletons of 90% and 50% identity representative sequences in each cluster.
Randomly select 1000 singletons.
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

INPUT_FILE_1 = "./clust_result/0.9_result/0.9clu_singleton_name"
INPUT_FILE_2 = "./clust_result/0.9_result/metag_ProG_nonsingleton_0.9_clu_rep.faa"
INPUT_FILE_3 = "./clust_result/0.5_result/0.5clu_singleton_name"
INPUT_FILE_4 = "./clust_result/0.5_result/metag_ProG_nonsingleton_0.5_clu_rep.faa"
OUT_FILE_1 = "./clust_result/0.9_result/0.9clu_singleton.faa"
OUT_FILE_2 = "./clust_result/0.9_result/0.9clu_nonsingleton.faa"
OUT_FILE_3 = "./clust_result/0.5_result/0.5clu_singleton.faa"
OUT_FILE_4 = "./clust_result/0.5_result/0.5clu_nonsingleton.faa"
OUT_FILE_5 = "./clust_result/0.9_result/0.9clu_singleton_1000.faa"
OUT_FILE_6 = "./clust_result/0.5_result/0.5clu_singleton_1000.faa"

extract(INPUT_FILE_1,INPUT_FILE_2,OUT_FILE_1,OUT_FILE_2)
extract(INPUT_FILE_3,INPUT_FILE_4,OUT_FILE_3,OUT_FILE_4)

NR_SINGLETONS_90 = 232027144
NR_SINGLETONS_50 = 171242722

select(OUT_FILE_1,OUT_FILE_5,NR_SINGLETONS_90)
select(OUT_FILE_3,OUT_FILE_6,NR_SINGLETONS_50)