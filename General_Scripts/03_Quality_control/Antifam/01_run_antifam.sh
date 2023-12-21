#!/usr/bin/env bash

# Concept: 
# Map 100AA smORFs to antifam to find spurious sequences.

set -e
set -o pipefail

hmmpress ~/software/antifam/AntiFam.hmm

hmmsearch --cut_ga --tblout ~/antifam/antifam_result_100.tsv ~/software/antifam/AntiFam.hmm ./data/frozen/100AA_GMSC_sort.faa

awk 'NR>3&&NR<4031131&&$5 <= 0.00001' antifam_result_100.tsv > antifam_result_100.tsv.tmp

cut -d ' ' -f 1 antifam_result_100.tsv.tmp|sort|uniq >antifam_result.tsv