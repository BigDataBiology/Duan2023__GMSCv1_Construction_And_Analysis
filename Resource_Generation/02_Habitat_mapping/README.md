## 02_Habitat_mapping

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_map_habitat.py | Map habitat for all the smORFs from metaG | metadata.tsv GMSC10.metag_smorfs.rename.txt.xz dedup_cluster.tsv.gz| metag_cluster_habitat.tsv.xz |
| 02_multi_habitat.py | Combine multiple habitats for each smORF from the same cluster | metag_cluster_habitat.tsv.xz GMSC.cluster.tsv.gz habitat_general.txt| GMSC10.100AA.general_habitat.tsv.xz |
| 03_map_cluster_habitat.py | Map multiple habitats to 90% identity smORFs clusters. | GMSC.cluster.tsv.gz 100AA_multi_general_habitat.tsv.xz habitat_general.txt| GMSC10.90AA.general_habitat.tsv.xz |
