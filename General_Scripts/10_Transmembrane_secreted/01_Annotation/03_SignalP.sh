#!/usr/bin/env bash

# Concept: 
# Run SisnalP 5.0 on 90AA smORF families
for n in {0..2399}
  do
    signalp -fasta sub_${n}.faa -org gram+ -batch 100000
    signalp -fasta sub_${n}.faa -org gram- -batch 100000
  done

for n in {0..62}
  do
signalp -fasta sub_${n}.faa -org arch -batch 100000
  done