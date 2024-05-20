### Antifam

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_run_antifam.sh | Map 100AA smORFs to antifam | AntiFam.hmm 100AA_GMSC_sort.faa | antifam_result.tsv |
| 02_assign_all_level.py | Assign antifam results to 90AA smORFs. | antifam_result.tsv GMSC.cluster.tsv.gz | antifam_90AA.tsv.gz |

### Coordinates

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_allcoordinate.py | Detect if there is a STOP codon on the upstream of the smORF in the contigs | GMSC10.metag_smorfs.rename.txt.xz ./contigs/ | result.tsv.gz | 
| 02_assign_all_level.py | Assign terminal checking results to 100AA and 90AA smORFs | result.tsv.gz GMSC.cluster.tsv.gz | 100AA_coordinate.tsv.gz 90AA_coordinate.tsv.gz | 

### RNAcode

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_filter8_addfna_split.py | Select clusters(>= 8 members) | GMSC.cluster.tsv.gz metag_ProG_smorfs.fna.xz | ./split/*.fna | 
| 02_run_MSA.sh | Multiple sequences alignment of each .fna file | ./split/*.fna | *.aln | 
| 03_run_RNAcode.sh | Run RNAcode | *.aln | *.tsv | 
| 04_filter_RNAcode.py | Filter RNAcode result | *.tsv GMSC.cluster_filter.tsv GMSC.cluster.tsv.gz | rnacode_true_90AA.tsv rnacode_true_100AA.tsv rnacode_false_100AA.tsv rnacode_false_90AA.tsv 90AA_RNAcode.tsv 100AA_RNAcode.tsv | 

### metatranscriptomics

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_run_bwa_ngless.sh | Map metatranscriptome reads to smORFs | 90AA_GMSC.fna *.fastq.gz | *.tsv | 
| 02_merge_filter.py | Merge and filter mapping results | *.tsv GMSC.cluster.tsv.gz | metaT_result.tsv metaT_90AA.tsv metaT_100AA.tsv 90AA_metaT.tsv 100AA_metaT.tsv| 

### riboseq

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_run_bwa_ngless.sh | Map riboseq reads to smORFs | 90AA_GMSC.fna *.fastq.gz | *.tsv | 
| 02_merge_filter.py | Merge and filter mapping results | *.tsv GMSC.cluster.tsv.gz | riboseq_result.tsv riboseq_90AA.tsv riboseq_100AA.tsv 90AA_RiboSeq.tsv 100AA_RiboSeq.tsv | 

### metaproteomics

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 00_split_100AA.py 01_map.py | For each metaproteomes peptides from each project in PRIDE,find their exact match against 100AA smORFs | 100AA_GMSC.faa.xz *.fasta | *.tsv | 
| 02_merge.py | Calculate and filter peptide coverage rate of each smORF | *.tsv | coverage_analysis.tsv 100AA_metaP.tsv | 
| 03_assign_all_level.py | Assign results to 90AA smORFs | coverage_analysis.tsv GMSC.cluster.tsv.gz | metaP_90AA.tsv.gz 100AA_metaP_all.tsv 90AA_metaP.tsv | 


### merge_quality_control

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_merge.py | Merge all the quality control results | GMSC.cluster.tsv.gz rnacode_true_100AA.tsv.xz rnacode_false_100AA.tsv.xz antifam_result.tsv coverage_analysis.tsv.gz riboseq_100AA.tsv.gz 100AA_coordinate.tsv.gz metaT_100AA.tsv.gz rnacode_true_90AA.tsv.xz rnacode_false_90AA.tsv.xz antifam_90AA.tsv metaP_90AA.tsv.gz riboseq_90AA.tsv.gz 90AA_coordinate.tsv.gz metaT_90AA.tsv.gz | GMSC10.100AA.quality.tsv.xz GMSC10.90AA.quality.tsv.xz allpass_100AA.txt allpass_90AA.txt | 
| 02_statistic.py | Merge all the quality control results | GMSC.cluster.tsv.gz rnacode_true_100AA.tsv.xz rnacode_false_100AA.tsv.xz antifam_result.tsv coverage_analysis.tsv.gz riboseq_100AA.tsv.gz 100AA_coordinate.tsv.gz metaT_100AA.tsv.gz | allquality_100AA.tsv.gz allpass_100AA.txt | 
| 03_merge_all.py | Merge all the values of quality control results | GMSC10.100AA.quality.tsv.xz 100AA_RNAcode.tsv 100AA_metaT.tsv 100AA_RiboSeq.tsv 100AA_metaP_all.tsv GMSC10.90AA.quality.tsv.xz 90AA_RNAcode.tsv 90AA_metaT.tsv 90AA_RiboSeq.tsv 90AA_metaP.tsv | GMSC10.100AA.quality.tsv.xz GMSC10.90AA.quality.tsv.xz allpass_100AA.txt allpass_90AA.txt GMSC10.100AA.quality_test.tsv GMSC10.90AA.quality_test.tsv | 