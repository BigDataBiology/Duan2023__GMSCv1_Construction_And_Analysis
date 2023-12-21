#!/usr/bin/env bash

# Concept: 
# Map to CDD database

rpsblast -query 90AA_GMSC.faa -out 90AA_cdd.tsv -db ~/Cdd -num_threads 20 -evalue 0.01 -outfmt "6 qseqid sseqid qlen score length pident evalue"