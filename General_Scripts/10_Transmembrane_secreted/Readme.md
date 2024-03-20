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
