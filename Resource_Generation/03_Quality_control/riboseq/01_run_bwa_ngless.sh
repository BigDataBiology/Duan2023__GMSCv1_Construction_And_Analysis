#!/usr/bin/env bash

# Concept: 
# Map riboseq reads to smORFs separately by bwa and count reads by ngless. 

set -e
set -o pipefail

bwa index -a bwtsw -p GMSC90AA.fna 90AA_GMSC.fna

# Run commonds below separately. * represents different SRR number
bwa mem -t 10 -k 14 -w 20 -r 10 -A 1 -B 1 -O 1 -E 1 -L 0 GMSC90AA.fna SRR*.fastq.gz > SRR*.sam

ngless SRR.ngl