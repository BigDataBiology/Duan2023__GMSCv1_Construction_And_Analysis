#!/usr/bin/env bash

# Concept: 
# Test the recovery of smORFs by different sensitivity of Diamond and MMseqs2 with different length (30,40,60,80,all)

for n in {1..7}
  do
    for m in 30 40 60 80
      do
        /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${m}.faa --dbdir ~/mapper_index  -t 20 -s ${n} --cov 0 -e 0.01 -o ~/mapper/benchmark/sensitivity/result/${m}_diamond_${n}
        /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${m}.faa --tool mmseqs --dbdir ~/mapper_index  -t 20 -s ${n} --cov 0 -e 0.01 -o ~/mapper/benchmark/sensitivity/result/${m}_mmseqs_${n}
      done
    /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select.faa  --dbdir ~/mapper_index  -t 20 -s ${n} --cov 0 -e 0.01 -o ~/mapper/benchmark/sensitivity/result/all_diamond_${n} 
    /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select.faa --tool mmseqs --dbdir ~/mapper_index  -t 20 -s ${n} --cov 0 -e 0.01 -o ~/mapper/benchmark/sensitivity/result/all_mmseqs_${n}
  done