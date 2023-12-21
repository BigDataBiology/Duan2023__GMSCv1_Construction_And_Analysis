#!/usr/bin/env bash

# Concept: 
# Use Diamond to align sequences to GMSC

diamond blastp -q refseq_sp_arc_dedup.faa -d 100AA_GMSC.dmnd -o refseq_arc.tsv --more-sensitive -e 0.00001 --outfmt 6 qseqid sseqid full_qseq full_sseq qlen slen pident length evalue qcovhsp scovhsp -p 64

diamond blastp -q refseq_sp_bac_dedup.faa -d 100AA_GMSC.dmnd -o refseq_bac.tsv --more-sensitive -e 0.00001 --outfmt 6 qseqid sseqid full_qseq full_sseq qlen slen pident length evalue qcovhsp scovhsp -p 64

diamond blastp -q cluster.faa -d 100AA_GMSC.dmnd -o cluster.tsv --more-sensitive -e 0.00001 --outfmt 6 qseqid sseqid full_qseq full_sseq qlen slen pident length evalue qcovhsp scovhsp -p 64

diamond blastp -q family.faa -d 100AA_GMSC.dmnd -o family.tsv --more-sensitive -e 0.00001 --outfmt 6 qseqid sseqid full_qseq full_sseq qlen slen pident length evalue qcovhsp scovhsp -p 64