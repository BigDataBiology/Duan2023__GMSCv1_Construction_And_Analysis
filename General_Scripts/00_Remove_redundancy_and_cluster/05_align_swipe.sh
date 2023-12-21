#!/usr/bin/env bash

#Concept: 
#Align randomly selected 1,000 singletons against non-singletons using swipe.(identity >= 90,evalue <= 1e-5,coverage rate >= 0.9)

set -e
set -o pipefail

#make db
makeblastdb -in 0.9clu_nonsingleton.faa -dbtype prot -blastdb_version 4 -parse_seqids -out 90AA_nonsingleton_db

#align
swipe -d 90AA_nonsingleton_db -i selected_singleton.faa -a 128 -m '8 std qcovs' -o result_singleton.tsv -p 1 -e 0.00001

#Concept: 
#Randomly select 1,000 sequences and align them to the representive sequences of the cluster(>1 member) they are from. using swipe.(identity >= 90,evalue <= 1e-5,coverage rate >= 0.9)

#make db
makeblastdb -in selected_90AA.faa -dbtype prot -blastdb_version 4 -parse_seqids -out 90AA_1000_db

#align
swipe -d 90AA_1000_db -i selected_100AA.faa -a 128 -m '8 std qcovs' -o result_100AA.tsv -p 1 -e 0.00001