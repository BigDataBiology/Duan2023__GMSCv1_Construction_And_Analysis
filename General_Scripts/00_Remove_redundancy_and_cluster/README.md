## 00_Remove_redundancy_and_cluster
| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_deduplicate_sort_merge.py | Remove redundancy of the raw data (predicted smORFs from metagenomes and genomes) | GMSC10.metag_Prog_smorfs.faa.gz | metag_ProG_dedup.faa.gz metag_ProG.raw_number.tsv.gz|
| 02_extract.py | Extract non-singletons and singletons |metag_ProG_dedup.faa.gz metag_ProG.raw_number.tsv.gz | metag_ProG_nonsingleton.faa.gz metag_ProG_singleton.faa.gz|
| 03_linclust.sh | Cluster non-singletons at 90% amino acid identity and 90% coverage | metag_ProG_nonsingleton.faa.gz | metag_ProG_nonsingleton_0.9_clu.tsv metag_ProG_nonsingleton_0.9_clu_rep.faa 0.9clu_singleton_name |
| 04_1_sig_select1000.py | Randomly select 1,000 cluster with only 1 sequence for cluster significance checking | 0.9clu_singleton_name metag_ProG_nonsingleton_0.9_clu_rep.faa | 0.9clu_singleton.faa 0.9clu_nonsingleton.faa selected_singleton.faa |
| 04_1_sig_select100AA.py | Randomly select 1,000 sequences for mapping back to the representive sequences of the cluster(>1 member) they are from | all_0.9_0.5_family_sort.tsv.xz 100AA_GMSC_sort.faa.xz 90AA_GMSC_sort.faa.gz| selected_cluster.tsv selected_100AA.faa selected_90AA.faa |
| 05_align_swipe.sh | Run swipe to align above sequences | 0.9clu_nonsingleton.faa selected_singleton.faa selected_90AA.faa selected_100AA.faa | result_singleton.tsv result_100AA.tsv |
| 06_split_singletons.py 07_diamond.sh 08_identify_clusters.py 09_join_rescue_result.py| Align all the singletons of raw data against cluster representatives at 90% amino acid identity and 90% coverage | metag_ProG_singleton.faa.gz metag_ProG_nonsingleton_0.9_clu_rep.faa | singleton_0.9.tsv |