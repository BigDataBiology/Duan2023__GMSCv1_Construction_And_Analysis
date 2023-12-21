#!/usr/bin/env bash

# Concept: 
# Test the time cost by Diamond and MMseqs2

for n in 1000 10000 100000 1000000
  do 
    /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${n}.faa --dbdir ~/mapper_index -o ~/benchmark/diamond_aa_${n} -t 20 -s 4 --cov 0.9 --id 0.9 -e 0.001
    /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${n}.faa --dbdir ~/mapper_index -o ~/benchmark/mmseqs_aa_${n} -t 20 --cov 0.9 --id 0.9 -e 0.001 --tool mmseqs
  done 