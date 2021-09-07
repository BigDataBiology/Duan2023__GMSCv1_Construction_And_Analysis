#!/usr/bin/env bash

#Concept: 
#Align 1000 singletons against non-singletons using swipe.(identity >= 90,evalue <= 1e-5,coverage rate >= 0.9)

set -e
set -o pipefail

cd clust_result/0.5_result

#make db
makeblastdb -in 0.5clu_nonsingleton.faa -dbtype prot -blastdb_version 4 -parse_seqids -out 0.5clu_nonsingleton_db 
#align
swipe -d 0.5clu_nonsingleton_db -i 0.5clu_singleton_1000.faa -a 18 -m '8 std qcovs' -o result_align_0.5 -p 1 

#analysis of result
#extract name of query sequences
grep ">" 0.5clu_singleton_1000.faa |sed 's/>//g' > query.names
#extract length of query sequences
grep -v ">" 0.5clu_singleton_1000.faa | awk '{print length}' > t
#join name  and length of query sequences
paste -d '\t' query.names t > t2; rm -rf t; mv t2 query.names.list

#extract name of subject sequences
grep ">" 0.5clu_nonsingleton.faa | awk '{print "lcl|"$1}' | sed 's/>//g' > ref.names.list
#extract length of subject sequences
grep -v ">" 0.5clu_nonsingleton.faa | awk '{print length}' > t
#join name and length of subject sequences
paste -d'\t' ref.names.list t > t2; rm -rf t; mv t2 ref.names.list

#select identity > 90 and evalue < 1e-5
awk '$3 >= 90 && $11 <= 1e-5' result_align_0.5 > align.tsv.tmp
#sort the subject lcl name
sort -k1,1 ref.names.list > ref
#sort the subject lcl name of the second column of the align result
cat align.tsv.tmp | sort -k2,2 > align.tsv.tmp.1
#join to add length of subject
join -1 1 -2 2 ref align.tsv.tmp.1 | sed 's/ /\t/g' > align.tsv.tmp.2
#sort the query name
sort -k1,1 query.names.list > query_length
#sort the query name of the third column of the align result
cat align.tsv.tmp.2 | sort -k3,3 > align.tsv.tmp.3
#join to add length of query
join -1 1 -2 3 query_length align.tsv.tmp.3 | sed 's/ /\t/g' > align.tsv.tmp.4
#add coverage rate
cat align.tsv.tmp.4 | awk '{print $0"\t"$6/$2"\t"$6/$4}' > align.tsv.tmp.5
#select coverage rate both > 0.9
awk '$15 >= 0.9 && $16 >= 0.9' align.tsv.tmp.5 > align_filt.tsv

#extract uniq name of query sequences that can be align
cat align_filt.tsv|cut -f 1|sort|uniq >align_query
cut -f 1 align_filt.tsv|sort|uniq -c|wc -l

cd ../0.9_result

#make db
makeblastdb -in 0.9clu_nonsingleton.faa -dbtype prot -blastdb_version 4 -parse_seqids -out 0.9clu_nonsingleton_db 
#align
swipe -d 0.9clu_nonsingleton_db -i 0.9clu_singleton_1000.faa -a 18 -m '8 std qcovs' -o result_align_0.9 -p 1 

#analysis of result
#extract name of query sequences
grep ">" 0.9clu_singleton_1000.faa |sed 's/>//g' > query.names
#extract length of query sequences
grep -v ">" 0.9clu_singleton_1000.faa | awk '{print length}' > t
#join name  and length of query sequences
paste -d '\t' query.names t > t2; rm -rf t; mv t2 query.names.list

#extract name of subject sequences
grep ">" 0.9clu_nonsingleton.faa | awk '{print "lcl|"$1}' | sed 's/>//g' > ref.names.list
#extract length of subject sequences
grep -v ">" 0.9clu_nonsingleton.faa | awk '{print length}' > t
#join name  and length of subject sequences
paste -d'\t' ref.names.list t > t2; rm -rf t; mv t2 ref.names.list

#select identity > 90 and evalue < 1e-5
awk '$3 >= 90 && $11 <= 1e-5' result_align_0.9 > align.tsv.tmp
#sort the subject lcl name
sort -k1,1 ref.names.list > ref
#sort the subject lcl name of the second column of the align result
cat align.tsv.tmp | sort -k2,2 > align.tsv.tmp.1
#join to add length of subject
join -1 1 -2 2 ref align.tsv.tmp.1 | sed 's/ /\t/g' > align.tsv.tmp.2
#sort the query name
sort -k1,1 query.names.list > query_length
#sort the query name of the third column of the align result
cat align.tsv.tmp.2 | sort -k3,3 > align.tsv.tmp.3
#join to add length of query
join -1 1 -2 3 query_length align.tsv.tmp.3 | sed 's/ /\t/g' > align.tsv.tmp.4
#add coverage rate
cat align.tsv.tmp.4 | awk '{print $0"\t"$6/$2"\t"$6/$4}' > align.tsv.tmp.5
#select coverage rate both > 0.9
awk '$15 >= 0.9 && $16 >= 0.9' align.tsv.tmp.5 > align_filt.tsv

#extract uniq name of query sequences that can be align
cat align_filt.tsv|cut -f 1|sort|uniq >align_query
cut -f 1 align_filt.tsv|sort|uniq -c|wc -l