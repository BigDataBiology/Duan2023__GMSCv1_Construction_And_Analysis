#!/usr/bin/env bash

# Concept: 
# Map 100AA smORFs to antifam to find spurious sequences.

set -e
set -o pipefail

hmmpress AntiFam.hmm

hmmsearch --cut_ga --tblout antifam_result_100.tsv AntiFam.hmm 100AA_GMSC.faa

awk 'NR>3&&NR<4031131&&$5 <= 0.00001' antifam_result_100.tsv > antifam_result_100.tsv.tmp

cut -d ' ' -f 1 antifam_result_100.tsv.tmp|sort|uniq >antifam_result.tsv