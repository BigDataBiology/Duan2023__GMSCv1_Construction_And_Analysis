#!/usr/bin/env bash

# Concept: 
# Run SisnalP 4.1 on 90AA smORF families

signalp -t gram+ 90AA_GMSC.faa >90AA_signalp_gram_positive.tsv
signalp -t gram- 90AA_GMSC.faa >90AA_signalp_gram_negative.tsv