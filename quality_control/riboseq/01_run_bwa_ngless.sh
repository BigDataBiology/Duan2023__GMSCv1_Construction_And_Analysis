#!/usr/bin/env bash

# Concept: 
# Map riboseq reads to smORFs by bwa and count reads by ngless. 

set -e
set -o pipefail

bwa index -a bwtsw -p GMSC90AA.fna /frozen/90AA_GMSC.fna

bwa mem -t 10 -k 14 -w 20 -r 10 -A 1 -B 1 -O 1 -E 1 -L 0 /riboseq/index/GMSC90AA.fna /riboseq/srr/SRR*.fastq.gz > /riboseq/result/bwa/SRR*.sam

ngless /riboseq/code/SRR.ngl