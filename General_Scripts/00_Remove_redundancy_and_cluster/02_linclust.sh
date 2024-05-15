#!/usr/bin/env bash

#Concept: 
#Cluster non-singletons at 90% amino acid identity by Linclust

set -e
set -o pipefail

mkdir clust_result
cd clust_result

#make db
mmseqs createdb metag_ProG_nonsingleton.faa.gz metag_ProG_nonsingleton.DB

#clust with -c 0.9,--min-seq-id:0.9
mmseqs linclust metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.9_clu tmp -c 0.9 --min-seq-id 0.9 

#Extract representative sequence
mmseqs createsubdb metag_ProG_nonsingleton_0.9_clu metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.9_clu_rep 

mmseqs convert2fasta metag_ProG_nonsingleton_0.9_clu_rep  metag_ProG_nonsingleton_0.9_clu_rep.faa

#generate tsv
mmseqs createtsv metag_ProG_nonsingleton.DB metag_ProG_nonsingleton.DB metag_ProG_nonsingleton_0.9_clu metag_ProG_nonsingleton_0.9_clu.tsv

#select singleton sequence name
cut -f 1 metag_ProG_nonsingleton_0.9_clu.tsv|uniq -u >0.9clu_singleton_name