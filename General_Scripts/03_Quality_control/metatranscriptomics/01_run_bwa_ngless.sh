#!/usr/bin/env bash

# Concept: 
# Map metatranscriptome reads to smORFs separately by bwa and count reads by ngless. 

set -e
set -o pipefail

bwa index -a bwtsw -p GMSC90AA.fna 90AA_GMSC.fna

# Run commonds below separately. * represents different SRR number
bwa mem -t 20 GMSC90AA.fna SRR*_1.fastq.gz SRR*_2.fastq.gz  > SRR*.sam

ngless SRR.ngl