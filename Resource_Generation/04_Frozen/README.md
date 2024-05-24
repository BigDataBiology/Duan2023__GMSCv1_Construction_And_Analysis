## 04_Frozen

| **Code** | **Description** | **Input** | **Output** |
| :---: | :---: | :---: | :---: |
| 01_rename_list.py | Rename 100AA sequences | metag_ProG.raw_number.tsv.gz metag_ProG_nonsingleton.faa.gz singleton_0.9.tsv metag_ProG_singleton.faa.gz| nonsingleton_rename.tsv singleton_rename.tsv |
| 02_100AA_faa_fna.py | Generate 100AA faa and fna file with new identifier | 100AA_rename.tsv metag_ProG_dedup.faa.gz GMSC10.metag_smorfs.fna.xz GMSC.ProGenomes2.smorfs.fna.xz | 100AA_GMSC.faa.xz 100AA_metag.fna.xz 100AA_prog.fna.xz |
| 03_90AA_faa_fna.py | Rename 90AA sequences and generate 90AA faa and fna file with new identifier | metag_ProG_nonsingleton_0.9_clu_rep.faa.gz metag_ProG_nonsingleton_0.9_clu.tsv.gz 100AA_rename.tsv.xz 100AA_GMSC.fna.xz | 90AA_rename.tsv.xz 90AA_rename_all.tsv.xz 90AA_GMSC.faa.xz 90AA_GMSC.fna.xz |
| 04_family.py | Generate the family table | 90AA_rename_all.tsv.xz 100AA_rename.tsv all_0.9.tsv.gz | GMSC.cluster.tsv |