#!/usr/bin/env bash

# Concept: 
# Use Diamond to align sequences to GMSC

diamond blastp -q database_dedup.faa -d 100AA_GMSC.dmnd -o database.tsv --more-sensitive -e 0.00001 --outfmt 6 qseqid sseqid full_qseq full_sseq qlen slen pident length evalue qcovhsp scovhsp -p 64