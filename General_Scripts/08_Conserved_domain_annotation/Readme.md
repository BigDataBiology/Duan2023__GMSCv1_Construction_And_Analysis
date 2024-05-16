## 07_GMSC_mapper_benchmark

### 01_Annotation

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: | 
| 01_cdd.sh | Map 90AA families to CDD database. | 90AA_GMSC.faa | 90AA_cdd.tsv |
| 02_add_pssm_length.py | Filter results with target coverage >80%. | cddid_all.tbl.gz 90AA_cdd.tsv | 1_cdd_tcov_90AA.tsv |

### 02_multi-phylum analysis

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: | 
| 01_multi_specific.py | Analyse if 90AA families are specific or multiple at each taxonomy rank. | metag_cluster_tax_90.tsv | 90AA_taxa_multi_specific.tsv 90AA_specific_multi.tsv |
| 02_get_all_habitat.py | Add CDD annotation to 90AA families across all 8 habitat categories. | GMSC10.90AA.general_habitat.tsv.xz 1_cdd_tcov_90AA.tsv.gz cddid_all.tbl.gz | all_habitat_smorf_motif.tsv |
| 03_species_number.py | Calculate the species number in 90AA families across all 8 habitat categories. | metag_cluster_tax_90.tsv.xz all_habitat_smorf.tsv | housekeeping_species.tsv |
| 04_merge_multi-phylum.py | multi-phylum 90AA families | housekeeping_species.tsv 90AA_taxa_multi_specific.tsv | housekeeping_multi.tsv |
| 05_map_sample_taxonomy.py | Map samples and taxonomy to multi-phylum 90AA families which occurs in 8 habitat categories and are from more than 100 species | 100AA_sample.tsv.xz GMSC.cluster.tsv.gz housekeeping_species.tsv metag_cluster_tax_90.tsv.xz | 90AA_sample.tsv housekeeping_sample.txt housekeeping_taxonomy.txt |

### 03_multi-genus_enrichment

| **Code** | **Description** |
| :---: | :---: | :---: | :---: | 
| 01_multi_genus.py | Extract multi-genus and specific-genus families. | 90AA_taxa_multi_specific.tsv | multi_genus_3.tsv specific_genus_3.tsv  |
| 02_keep_size.py | Keep the same size for selected clusers from multi-genus and the whole clusters. | 90AA_taxa_multi_specific.tsv multi_genus_3.tsv| whole_3_selected.tsv |
| 03_extract_count.py | Calculate fraction of habitats and cdd annotation of families from the whole GMSCwith the same size distribution. | whole_3_selected.tsv  90AA_multi_habitat_cdd.tsv 90AA_multi_habitat.tsv | whole_3_selected_habitat_cdd.tsv whole_3_selected_habitat.tsv |