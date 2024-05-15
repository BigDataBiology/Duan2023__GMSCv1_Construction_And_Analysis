## 01_Taxonomy_mapping

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_map_prog_taxa_dedup.py | Remove redundancy of smORFs from Progenomes and map specI taxonomy to genomes | genome_prog.tsv specI_genome_taxa.txt GMSC10.ProG_smorfs.faa.gz | prog_specI_genome_taxa.tsv prog_dedup_sort.faa.gz prog_redundant.tsv.gz |
| 02_run_linclust.sh 03_lca_change_format.py | Cluster smORFs from Progenomes at 90% amino acid identity and 90% coverage and map taxonomy by LCA | prog_dedup.faa.gz prog_redundant.tsv.gz prog_specI_genome_taxa.tsv.gz | prog_taxonomy_change.tsv.gz |
| 04_map_metag_taxid_full.py | Map taxid of smORFs from metaG based on contigs and et the fullname of taxid based on GTDB | mmseqs2.lca_taxonomy.full.tsv.xz GMSC10.metag_smorfs.rename.txt.xz gtdb_taxonomy.tsv | metag_taxid.tsv.xz taxid_fullname_gtdb.tsv |
| 05_dedup_cluster.py | Get clusters at 100% identity of raw data | GMSC10.metag_ProG_smorfs.faa.gz | dedup_cluster.tsv.gz |
| 06_map_taxonomy.py | Map taxonomy for all the smORFs from metaG | taxid_fullname_gtdb.tsv metag_taxid.tsv.xz dedup_cluster.tsv.gz prog_taxonomy_change.tsv.gz | metag_cluster_taxonomy.tsv.xz |
| 07_deep_lca_100.py | Map taxonomy for 100% identity smORFs with LCA | metag_cluster_taxonomy.tsv.xz GMSC.cluster.tsv.gz | 100AA_taxonomy.tsv.xz |
| 08_map_cluster_tax.py | Map taxonomy for 90% identity smORFs with LCA | 100AA_taxonomy.tsv.xz GMSC.cluster.tsv.gz | 90AA_tax.tsv.xz |
| 09_fix_prog_tax.py | Make consistency between Progenomes2 taxonomy and GTDB taxonomy | 100AA_taxonomy.tsv.xz 90AA_tax.tsv.xz | GMSC10.100AA.taxonomy.tsv GMSC10.90AA.taxonomy.tsv |
