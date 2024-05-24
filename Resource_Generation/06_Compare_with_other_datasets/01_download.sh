#!/usr/bin/env bash

# Concept: 
# Download archaeal and bacterial protein from Refseq.

for m in {1..5}
  do
    wget https://ftp.ncbi.nlm.nih.gov/refseq/release/archaea/archaea.nonredundant_protein.${m}.protein.faa.gz
  done

cat ~/refseq/arc/*.faa.gz >refseq_arc.faa.gz

for m in {1..1648}
  do
    wget https://ftp.ncbi.nlm.nih.gov/refseq/release/bacteria/bacteria.nonredundant_protein.${m}.protein.faa.gz
  done

cat ~/refseq/bac/*.faa.gz >refseq_bac.faa.gz