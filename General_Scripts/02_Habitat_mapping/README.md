## 02_Habitat_mapping

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_map_habitat.py | Map habitat for all the smORFs from metaG | metadata.tsv GMSC10.metag_smorfs.rename.txt.xz dedup_cluster.tsv.gz| metag_cluster_habitat.tsv.xz |
| 02_multi_habitat.py | Combine multiple habitats for each smORF from the same cluster | metag_cluster_habitat.tsv.xz 100AA_rename.tsv.xz habitat_general.txt| 100AA_multi_general_habitat.tsv.xz |
| 03_map_cluster_habitat.py | Map habitat to 90% identity smORFs clusters. | all_0.5_0.9.tsv.gz 100AA_multi_general_habitat.tsv.xz | cluster_multi_habitat_90.tsv.xz |
|04_multi_habitat_90_50.py | Combine multiple habitats for each smORF from the same 90AA cluster |cluster_multi_habitat_90.tsv.xz habitat_general.txt | 90AA_multi_general_habitat.tsv.xz |
