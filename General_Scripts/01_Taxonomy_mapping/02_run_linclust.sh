#!/usr/bin/env bash

#Cluster smORFs from Progenome by Linclust

set -e
set -o pipefail

mkdir clust_result
cd clust_result

#make db
mmseqs createdb prog_dedup.faa.gz prog_dedup.DB

#clust with kmer:21,-c 0.9,--min-seq-id:0.9
mmseqs linclust prog_dedup.DB prog_dedup_0.9_clu tmp -c 0.9 --min-seq-id 0.9 

#generate tsv
mmseqs createtsv prog_dedup.DB prog_dedup.DB prog_dedup_0.9_clu prog_dedup_0.9_clu.tsv
