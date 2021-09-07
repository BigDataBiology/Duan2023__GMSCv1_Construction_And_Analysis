#!/usr/bin/env bash

#Concept: 
#Cluster non-singletons by Linclust

set -e
set -o pipefail

mkdir clust_result
cd clust_result

#make db
mmseqs createdb ../data/metag_ProG_nonsingleton.faa.gz metag_ProG_nonsingleton.DB

mkdir 0.9_result
cd 0.9_result

#clust with kmer:21,-c 0.9,--min-seq-id:0.9
mmseqs linclust ../metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.9_clu tmp -c 0.9 --min-seq-id 0.9 

#Extract representative sequence
mmseqs createsubdb metag_ProG_nonsingleton_0.9_clu ../metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.9_clu_rep 

mmseqs convert2fasta metag_ProG_nonsingleton_0.9_clu_rep  metag_ProG_nonsingleton_0.9_clu_rep.faa

#generate tsv
mmseqs createtsv ../metag_ProG_nonsingleton.DB ../metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.9_clu metag_ProG_nonsingleton_0.9_clu.tsv

#select singleton sequence name
cut -f 1 metag_ProG_nonsingleton_0.9_clu.tsv|uniq -u >0.9clu_singleton_name

cd ..
mkdir 0.5_result
cd 0.5_result

#clust with kmer:21,-c 0.9,--min-seq-id:0.5
mmseqs linclust ../metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.5_clu tmp -c 0.9 --min-seq-id 0.5

#Extract representative sequence
mmseqs createsubdb metag_ProG_nonsingleton_0.5_clu ../metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.5_clu_rep 

mmseqs convert2fasta metag_ProG_nonsingleton_0.5_clu_rep  metag_ProG_nonsingleton_0.5_clu_rep.faa

#generate tsv
mmseqs createtsv ../metag_ProG_nonsingleton.DB ../metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.5_clu metag_ProG_nonsingleton_0.5_clu.tsv

#select singleton sequence name
cut -f 1 metag_ProG_nonsingleton_0.5_clu.tsv|uniq -u >0.5clu_singleton_name
