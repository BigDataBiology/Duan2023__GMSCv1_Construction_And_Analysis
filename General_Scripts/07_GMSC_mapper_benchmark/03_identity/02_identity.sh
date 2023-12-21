#!/usr/bin/env bash

# Concept: 
# Test the recovery of smORFs between Blast,Diamond,MMseqs with different length (20,30,40,60,80,all) and different identity.

for m in 20 30 40 60 80 
  do
    for n in 0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1
      do
        /usr/bin/time -v blastp -query GMSC_90_select_${m}_${n}.faa -out ~/benchmark/identity/result/blast/${m}_blast_${n}.tsv -db ~/blastdb/90AA_GMSC_new -evalue 0.01 -outfmt "6 qseqid sseqid qlen slen pident length evalue qcovs" -num_threads 20
        /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${m}_${n}.faa --dbdir ~/mapper_index -t 20 -s 4 --cov 0 -e 0.01 -o ~/benchmark/identity/result/${m}_diamond_${n}
        /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${m}_${n}.faa --dbdir ~/mapper_index -t 20 --cov 0 -e 0.01 -o ~/benchmark/identity/result/${m}_mmseqs_${n} --tool mmseqs
      done
    /usr/bin/time -v blastp -query GMSC_90_select_${m}.faa -out ~/benchmark/identity/result/blast/${m}_blast_1.tsv -db ~/blastdb/90AA_GMSC_new -evalue 0.01 -outfmt "6 qseqid sseqid qlen slen pident length evalue qcovs" -num_threads 20
    /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${m}.faa --dbdir ~/mapper_index -t 20 -s 4 --cov 0 -e 0.01 -o ~/benchmark/identity/result/${m}_diamond_1
    /usr/bin/time -v gmsc-mapper --aa-genes GMSC_90_select_${m}.faa --dbdir ~/mapper_index -t 20 --cov 0 -e 0.01 -o ~/benchmark/identity/result/${m}_mmseqs_1 --tool mmseqs
  done 