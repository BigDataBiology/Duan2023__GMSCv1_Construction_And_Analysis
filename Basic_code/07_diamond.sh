#!/usr/bin/env bash

#Concept: 
#Align all the singletons of raw data against non-singletons using Diamond (evalue:0.00001, identity:90).

set -e
set -o pipefail

#make db
diamond makedb --in ../clust_result/0.5_result/metag_ProG_nonsingleton_0.5_clu_rep.faa -d metag_ProG_ns_0.5
diamond makedb --in ../clust_result/0.9_result/metag_ProG_nonsingleton_0.9_clu_rep.faa -d metag_ProG_ns_0.9

mkdir result_0.5
mkdir result_0.9

#align 
DIR="./split"
for file in $(ls $DIR)
  do
    diamond blastp -q ./split/$file -d metag_ProG_ns_0.5 -o ./result_0.5/$file.tsv -e 0.00001 --id 90 -b 12 -c 1
    diamond blastp -q ./split/$file -d metag_ProG_ns_0.9 -o ./result_0.9/$file.tsv -e 0.00001 --id 90 -b 12 -c 1
  done
