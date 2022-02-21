#!/usr/bin/env bash

# Concept: 
# Map metatranscriptome reads to smORFs by bwa and count reads by ngless. 

set -e
set -o pipefail

bwa index -a bwtsw -p GMSC90AA.fna /frozen/90AA_GMSC.fna

bwa mem -t 20 /metaT/index/GMSC90AA.fna /metaT/fastq/SRR*_1.fastq.gz /metaT/fastq/SRR*_2.fastq.gz  > /metaT/result/bwa/SRR*.sam

ngless /metaT/code/SRR.ngl