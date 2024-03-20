## 09_Density

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_100AA_copy_number_per_tax.py | Calculate the copy number of smORFs per taxonomy | 100AA_rename.tsv.xz metag_cluster_taxonomy.tsv.xz | cpnumber_per_tax.tsv |
| 02_nbps_per_tax.py | Calculate nbps per taxonomy | taxid_fullname_gtdb.tsv bps-per-taxon.tsv | per_tax_rank.txt full_nbp.txt |
| 03_calculate_density.py | Calculate density of phylum and genus | cpnumber_per_tax.tsv per_tax_rank.txt| density_phylum.tsv density_genus.tsv |