### Antifam

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_run_antifam.sh | Map 100AA smORFs to antifam | AntiFam.hmm 100AA_GMSC_sort.faa | antifam_result.tsv |
| 02_assign_all_level.py | Assign antifam results to 90AA smORFs. | antifam_result.tsv all_0.9_0.5_family.tsv.xz | antifam_90AA.tsv.gz |

### Coordinates

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_allcoordinate.py | Detect if there is a STOP codon on the upstream of the smORF in the contigs | GMSC10.metag_smorfs.rename.txt.xz ./contigs/ | result.tsv.gz | 
| 02_assign_all_level.py | Assign terminal checking results to 100AA and 90AA smORFs | result.tsv.gz 100AA_rename.tsv.xz all_0.9_0.5_family.tsv.xz | 100AA_coordinate.tsv.gz 90AA_coordinate.tsv.gz | 

### RNAcode

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_filter8_addfna_split.py | Select clusters(>= 8 members) | all_0.5_0.9.tsv metag_ProG_smorfs.fna.xz | ./split/*.fna | 
| 02_run_MSA.sh | Multiple sequences alignment of each .fna file | ./split/*.fna | *.aln | 
| 03_run_RNAcode.sh | Run RNAcode | *.aln | *.tsv | 
| 04_filter_RNAcode.py | Filter RNAcode result | *.tsv | smORF_0.9_RNAcode.tsv | 
| 05_assign_all_level.py | Assign RNAcode results to 100AA and 90AA smORFs | smORF_0.9_RNAcode.tsv all_0.5_0.9_filter.tsv 100AA_rename.tsv.xz 90AA_rename.tsv.xz all_0.9_0.5_family.tsv.xz | rnacode_true_100AA.tsv.xz rnacode_false_100AA.tsv.xz rnacode_true_90AA.tsv.xz rnacode_false_90AA.tsv.xz | 

### metatranscriptomics

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_run_bwa_ngless.sh | Map metatranscriptome reads to smORFs | 90AA_GMSC.fna *.fastq.gz | *.tsv | 
| 02_merge_filter.py | Merge and filter mapping results | *.tsv | metaT_result_filter.tsv | 
| 03_assign_all_level.py | Assign results to 100AA and 90AA smORFs | metaT_result_filter.tsv all_0.9_0.5_family.tsv.xz | metaT_100AA.tsv.gz metaT_90AA.tsv.gz | 

### riboseq

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_run_bwa_ngless.sh | Map riboseq reads to smORFs | 90AA_GMSC.fna *.fastq.gz | *.tsv | 
| 02_merge_filter.py | Merge and filter mapping results | *.tsv | riboseq_result_filter.tsv | 
| 03_assign_all_level.py | Assign results to 100AA and 90AA smORFs | riboseq_result_filter.tsv all_0.9_0.5_family.tsv.xz | riboseq_100AA.tsv.gz riboseq_90AA.tsv.gz | 

### metaproteomics

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 00_split_100AA.py 01_map.py | For each metaproteomes peptides from each project in PRIDE,find their exact match against 100AA smORFs | 100AA_GMSC.faa.xz *.fasta | *.tsv | 
| 02_merge.py | Calculate and filter peptide coverage rate of each smORF | *.tsv | coverage_analysis.tsv | 
| 03_assign_all_level.py | Assign results to 90AA smORFs | coverage_analysis.tsv all_0.9_0.5_family.tsv.xz | metaP_90AA.tsv.gz | 


### merge_quality_control

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_merge.py | Merge all the quality control results | 100AA_rename.tsv.xz rnacode_true_100AA.tsv.xz rnacode_false_100AA.tsv.xz antifam_result.tsv coverage_analysis.tsv.gz riboseq_100AA.tsv.gz 100AA_coordinate.tsv.gz metaT_100AA.tsv.gz | allquality_100AA.tsv.gz allpass_100AA.txt | 