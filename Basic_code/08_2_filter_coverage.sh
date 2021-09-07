#!/usr/bin/env bash

#Concept: 
#Add coverage rate into Diamond result and filter Diamond result by coverage rate (>= 0.9).

set -e
set -o pipefail

cd diamond/analysis/analysis_0.5

for i in {0..23}
  do
  cat sub${i}.faa.gz.tsv.tmp.1 | awk '{print $0"\t"$6/$2"\t"$6/$4}' > sub${i}.faa.gz.tsv.tmp.2
  awk '$8 >= 0.9 && $9 >= 0.9' sub${i}.faa.gz.tsv.tmp.2 > sub${i}.faa.gz.tsv.tmp.3
  done


cd diamond/analysis/analysis_0.9

for i in {0..23}
  do
  cat sub${i}.faa.gz.tsv.tmp.1 | awk '{print $0"\t"$6/$2"\t"$6/$4}' > sub${i}.faa.gz.tsv.tmp.2
  awk '$8 >= 0.9 && $9 >= 0.9' sub${i}.faa.gz.tsv.tmp.2 > sub${i}.faa.gz.tsv.tmp.3
  done