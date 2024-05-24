'''
Concept:
Randomly selected and mutated 10,000 sequences from 90AA smORFs with different length (20,30,40,60,80,all) at different identity.
'''
from fasta import fasta_iter
import random

def select(infile,outfile,GMSC):
    selected = frozenset(random.sample(range(GMSC),10000))
    with open(outfile,'wt') as out:
        n=0
        for ID,seq in fasta_iter(infile):
           n+=1
           if n in selected:
               out.write(f'>{ID}\n{seq}\n')

def store(infile,l):
    lengthset = {l:[]}
    for ID,seq in fasta_iter(infile):
        if len(seq) == l:
            lengthset[len(seq)].append(f'{ID}\n{seq}')
    return(lengthset)

def select_length(lengthset,outfile,l):
    count = len(lengthset[l])
    selected = frozenset(random.sample(range(count),10000))
    with open(outfile,'wt') as out:
        n=0
        for sequence in lengthset[l]:
           n+=1
           if n in selected:
               out.write(f'>{sequence}\n')

def mutation(infile,outfile,number,length):
    aminoacid = ["A","R","N","D","C","Q","E","G","H","I","L","K","F","M","P","S","T","W","Y","V","X"]
    with open(outfile,'wt') as out:
        for ID,seq in fasta_iter(infile):
            selected = frozenset(random.sample(range(length),int(length-length*number)))
            for i in selected:
                seq = list(seq)
                loc = aminoacid.index(seq[i])
                if  loc != 20:
                    seq[i] = aminoacid[loc+1]
                else:
                    seq[i] = aminoacid[0]
                seq = ''.join(seq)
            out.write(f'>{ID}\n{seq}\n')

INPUT_FILE_1 = "90AA_GMSC.faa"
OUT_FILE_1 = "GMSC_90_select.faa"
GMSC_90 = 287926875
identity = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
length = [20,30,40,60,80]

select(INPUT_FILE_1,OUT_FILE_1,GMSC_90)

for l in length:
    OUT_FILE_2 = f'GMSC_90_select_{str(l)}.faa'
    lengthset = store(INPUT_FILE_1,l)
    select_length(lengthset,OUT_FILE_2,l)

for i in identity:
    for l in length:
        input = f'GMSC_90_select_{str(l)}.faa'
        output = f'GMSC_90_select_{str(l)}_{str(i)}.faa'
        mutation(input,output,i,l)
