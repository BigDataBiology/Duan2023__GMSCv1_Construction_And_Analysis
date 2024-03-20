# General_Scripts
The folder contains scripts to generate GMSC resourece from the raw data.

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

## 01_Taxonomy_mapping

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_map_prog_taxa_dedup.py | Remove redundancy of smORFs from Progenomes and map specI taxonomy to genomes | genome_prog.tsv specI_genome_taxa.txt GMSC10.ProG_smorfs.faa.gz | prog_specI_genome_taxa.tsv prog_dedup_sort.faa.gz prog_redundant.tsv.gz |
| 02_run_linclust.sh 03_lca_change_format.py | Cluster smORFs from Progenomes at 90% amino acid identity and 90% coverage and map taxonomy by LCA | prog_dedup.faa.gz prog_redundant.tsv.gz prog_specI_genome_taxa.tsv.gz | prog_taxonomy_change.tsv.gz |
| 04_map_metag_taxid_full.py | Map taxid of smORFs from metaG based on contigs and et the fullname of taxid based on GTDB | mmseqs2.lca_taxonomy.full.tsv.xz GMSC10.metag_smorfs.rename.txt.xz gtdb_taxonomy.tsv | metag_taxid.tsv.xz taxid_fullname_gtdb.tsv |
| 05_dedup_cluster.py | Get clusters at 100% identity of raw data | GMSC10.metag_ProG_smorfs.faa.gz | dedup_cluster.tsv.gz |
| 06_map_taxonomy.py | Map taxonomy for all the smORFs from metaG | taxid_fullname_gtdb.tsv metag_taxid.tsv.xz dedup_cluster.tsv.gz prog_taxonomy_change.tsv.gz | metag_cluster_taxonomy.tsv.xz |
| 07_deep_lca_100.py | Map taxonomy for 100% identity smORFs with LCA | metag_cluster_taxonomy.tsv.xz all_0.5_0.9.tsv.gz | 100AA_taxonomy.tsv.xz |
| 08_map_cluster_tax.py | Map taxonomy for 90% identity smORFs clusters with LCA | 100AA_taxonomy.tsv.xz all_cluster_0.9.tsv.xz | 90AA_tax.tsv.xz |
| 09_fix_prog_tax.py | Make consistency between Progenomes2 taxonomy and GTDB taxonomy | 100AA_taxonomy.tsv.xz 90AA_tax.tsv.xz | GMSC10.100AA.taxonomy.tsv GMSC10.90AA.taxonomy.tsv |

## 02_Habitat_mapping

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_map_habitat.py | Map habitat for all the smORFs from metaG | metadata.tsv GMSC10.metag_smorfs.rename.txt.xz dedup_cluster.tsv.gz| metag_cluster_habitat.tsv.xz |
| 02_multi_habitat.py | Combine multiple habitats for each smORF from the same cluster | metag_cluster_habitat.tsv.xz 100AA_rename.tsv.xz habitat_general.txt| 100AA_multi_general_habitat.tsv.xz |
| 03_map_cluster_habitat.py | Map habitat to 90% identity smORFs clusters. | all_0.5_0.9.tsv.gz 100AA_multi_general_habitat.tsv.xz | cluster_multi_habitat_90.tsv.xz |
|04_multi_habitat_90_50.py | Combine multiple habitats for each smORF from the same 90AA cluster |cluster_multi_habitat_90.tsv.xz habitat_general.txt | 90AA_multi_general_habitat.tsv.xz |

## 03_Quality_control

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

## 04_Frozen

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_rename_list.py | Rename 100AA sequences | metag_ProG.raw_number.tsv.gz metag_ProG_nonsingleton.faa.gz singleton_0.5_0.9.tsv metag_ProG_singleton.faa.gz| nonsingleton_rename.tsv singleton_rename.tsv |
| 02_100AA_faa_fna.py | Generate 100AA faa and fna file with new identifier | 100AA_rename.tsv.xz metag_ProG_dedup.faa.gz GMSC10.metag_smorfs.fna.xz GMSC.ProGenomes2.smorfs.fna.xz | 100AA_GMSC.faa.xz 100AA_metag.fna.xz 100AA_prog.fna.xz |
| 03_90AA_faa_fna.py | Rename 90AA sequences and generate 90AA faa and fna file with new identifier | metag_ProG_nonsingleton_0.9_clu_rep.faa.gz metag_ProG_nonsingleton_0.9_clu.tsv.gz 100AA_rename.tsv.xz 100AA_GMSC.fna.xz | 90AA_rename.tsv.xz 90AA_rename_all.tsv.xz 90AA_GMSC.faa.xz 90AA_GMSC.fna.xz |
| 04_family.py | Generate the cluster table | 90AA_rename_all.tsv.xz all_0.5_0.9_rename.tsv.gz | all_0.9_0.5_family.tsv.xz |

## 05_Rarefaction

| **Code** | **Description** |
| :---: | :---: | 
| split_samples.py | Separates the samples into files given the initial dataset, also discretizing the smORFs by their unique numbers |
| jugfile.py | Main code for doing the rarefaction. Select the samples for the expected environments|
| rarefaction.py | Auxiliary functions for the rarefaction |

## 06_Compare_with_other_datasets

| **Code** | **Description** |
| :---: | :---: |
| 01_download.sh 02_filter_sp_dedup.py | Download archaeal and bacterial proteins from Refseq, filter sequences (<100aa) and remove redundancy | 
| 03_align.sh | Use Diamond to align sequences to GMSC | 

## 07_GMSC_mapper_benchmark

### 01_sensitivity

| **Code** | **Description** | 
| :---: | :---: | 
| 01_sensitivity.sh | Test the recovery of smORFs by different sensitivity of Diamond and MMseqs2 with different length | 

### 02_time

| **Code** | **Description** |
| :---: | :---: |
| 01_time.sh | Test the time cost by Diamond and MMseqs2 | 

### 03_identity

| **Code** | **Description** |
| :---: | :---: | 
| 01_select_mutation.py  | Randomly selected and mutated 10,000 sequences from 90AA smORFs with different length (20,30,40,60,80,all) at different identity. | 
| 02_identity.sh | Test the recovery of smORFs between Blast,Diamond,MMseqs with different length (20,30,40,60,80,all) and different identity | 

## 08_Conserved_domain_annotation

### 01_Annotation

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_cdd.sh | Map to CDD database | 90AA_GMSC.faa ~/Cdd | 90AA_cdd.tsv |
| 02_add_pssm_length.py | Add length of PSSM and filter with target coverage >80%. | cddid_all.tbl.gz 90AA_cdd.tsv | 1_cdd_tcov_90AA.tsv |

### 02_multi-phylum_analysis

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_get_all_habitat.py | Select 90AA smORF families across all 8 habitat categories and map CDD annotation | GMSC10.90AA.general_habitat.tsv.xz 1_cdd_tcov_90AA.tsv.gz cddid_all.tbl.gz | all_habitat_smorf.tsv all_habitat_motif_right.tsv |
| 02_species_number.py | Calculate the species number in 90AA families | metag_cluster_tax_90.tsv.xz 90AA_rename.tsv.xz all_habitat_smorf.tsv | 90AA_species_number.tsv housekeeping_species.tsv |
| 03_multi_specific.py | Analyse if smORFs 90AA families are specific or multiple at the taxonomy rank | metag_cluster_tax_90.tsv 90AA_rename.tsv.xz | 90AA_multi_newname.tsv 90AA_specific_multi.tsv |
| 04_merge_multi-phylum.py | Merge table with multi-phylum 90AA families, habitats, and the number of species | housekeeping_species.tsv 90AA_multi_newname.tsv housekeeping_species.tsv all_habitat_motif.tsv | housekeeping_motif_species_multi_phylum_all.tsv |
| 05_map_sample_taxonomy.py | Map samples and taxonomy which are multi-phylum and distributed in 8 habitat categories and have more than 100 species | 100AA_sample.tsv.xz all_0.9_0.5_family_sort.tsv.xz housekeeping.txt 90AA_rename.tsv.xz metag_cluster_tax_90.tsv.xz | housekeeping_sample.txt housekeeping_taxonomy.txt |

### 03_multi-genus_enrichment
| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 00_multi_genus.py | Select multi-genus or specific-genus 90AA smORF families | 90AA_multi_newname.tsv | multi_genus_3.tsv specific_genus_3.tsv |
| 01_cal_size.py | | multi_genus_3_habitat.tsv 90AA_multi_newname.tsv | multi_genus_3_habitat_size.tsv whole_3_size.tsv whole_3.tsv |
| 02_keep_same_size.py | | multi_genus_3_habitat_size.tsv whole_3_size.tsv whole_3.tsv | size_genus_whole_3_compare.tsv whole_3_selected.tsv |
| 03_extract_count.py | | whole_3_selected.tsv  90AA_multi_newname_habitat_cdd.tsv 90AA_multi_newname_habitat.tsv | whole_3_selected_habitat_cdd.tsv whole_3_selected_habitat.tsv |

## 09_Density

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_100AA_copy_number_per_tax.py | Calculate the copy number of smORFs per taxonomy | 100AA_rename.tsv.xz metag_cluster_taxonomy.tsv.xz | cpnumber_per_tax.tsv |
| 02_nbps_per_tax.py | Calculate nbps per taxonomy | taxid_fullname_gtdb.tsv bps-per-taxon.tsv | per_tax_rank.txt full_nbp.txt |
| 03_calculate_density.py | Calculate density of phylum and genus | cpnumber_per_tax.tsv per_tax_rank.txt| density_phylum.tsv density_genus.tsv |

## 10_Transmembrane_secreted

### 01_Annotation

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_TMHMM2.sh 02_find_transmembrane.py | Run TMHMM2 on 90AA smORF families | 90AA_GMSC.faa | 90AA_tm_true.tsv |
| 03_SignalP.sh 04_find_signal.py | Run SisnalP 5.0 on 90AA smORF families | 90AA_GMSC.faa | 90AA_signalp.tsv |
| 05_overlap.py | Combine TMHMM and SignalP results | 90AA_tm_true.tsv 90AA_signalp.tsv | 90AA_tm_signal.tsv |

### 02_Compare between archaea and bacteria

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_map_taxonomy_trans.py | Map transmembrane or secreted families to taxonomy and count transmembrane or secreted fraction of each phylum | 90AA_tm_signal.tsv 90AA_ref_taxonomy_format.tsv.xz | trans_taxa.tsv trans_phylum.csv |
| 02_extract_cog.py | Extract bacterial and archaeal 90AA families with COG annotation | 90AA_ref_taxonomy_format.tsv.xz 1_cdd_tcov_90AA.tsv.gz cddid_all.tbl cog-20.def.tab.tsv | 0_arc_motif_cog.tsv 0_bac_motif_cog.tsv 0_bg_motif_cog.tsv |
| 03_count_cog_class.py | Count cog class number an fraction of smORFs with annotation | 0_bac_motif_cog.tsv 0_arc_motif_cog.tsv 0_bg_motif_cog.tsv | 1_bac_motif_cog_class_count.tsv 1_arc_motif_cog_class_count.tsv 1_bg_motif_cog_class_count.tsv |
| 04_count_cog.py | Count cog number an fraction of smORFs with annotation | 0_arc_motif_cog.tsv 0_bg_motif_cog.tsv | 1_arc_motif_cog_count.tsv 1_bg_motif_cog_count.tsv_new |
| 05_count_cog_class_trans.py | Count cog class number an fraction of transmembrane or secreted smORFs with annotation | 90AA_tm_signal.tsv.gz 0_arc_motif_cog.tsv 0_bac_motif_cog.tsv | 1_arc_motif_cog_class_count_trans.tsv 1_bac_motif_cog_class_count_trans.tsv |
| 06_count_cog_trans.py | Combine TMHMM and SignalP results | 90AA_tm_signal.tsv.gz 90AA_tm_signal.tsv.gz 0_arc_motif_cog.tsv 0_bac_motif_cog.tsv | 1_arc_motif_cog_count_trans.tsv 1_arc_motif_cog_count_not_trans.tsv 1_bac_motif_cog_count_trans.tsv 1_bac_motif_cog_count_not_trans.tsv |
