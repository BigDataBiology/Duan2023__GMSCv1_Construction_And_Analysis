Introduction:
The global microbial smORF catalog(GMSC) is constructed from GMGCv2 and Progenomes2.
GMGC is an integrated and consistently-processed gene catalog of the microbial world combining metagenomics and sequenced isolates. 
(Coelho, L.P., Alves, R., del Río, Á.R. et al. Towards the biogeography of prokaryotic genes. Nature 601, 252–256 (2022). https://doi.org/10.1038/s41586-021-04233-4)
Progenomes2 is  a prokaryotic genome resource that provides consistent taxonomic and functional annotations as well as habitat-specific representative genomes.
(Daniel R Mende, Ivica Letunic, Oleksandr M Maistrenko, Thomas S B Schmidt, Alessio Milanese, Lucas Paoli, Ana Hernández-Plaza, Askarbek N Orakov, Sofia K Forslund, Shinichi Sunagawa, Georg Zeller, Jaime Huerta-Cepas, Luis Pedro Coelho, Peer Bork, proGenomes2: an improved database for accurate and consistent habitat, taxonomic and functional annotations of prokaryotic genomes, Nucleic Acids Research, Volume 48, Issue D1, 08 January 2020, Pages D621–D625, https://doi.org/10.1093/nar/gkz1002)
Habitat of GMSC is annotated by GMGCv2 metadata.
Taxonomy of GMSC is annotated by GTDB.
Quality of GMSC is checked by computational checking(RNAcode,AntiFam) and experimental checking(metatranscriptomic,metaproteomic and riboseq data). High quality means smORFs pass computational checking and at least have one experimental evidence.

Methods:
We use Macrel to predicted smORFs from contigs.
(Santos-Júnior CD, Pan S, Zhao XM, Coelho LP. Macrel: antimicrobial peptide screening in genomes and metagenomes. PeerJ. 2020 Dec 18;8:e10555. doi: 10.7717/peerj.10555.)
We use Diamond to map predicted smORFs against our non-redundant 90AA smORF catalog.(90AA: We clustered our raw predicted smORFs at 90% identity and 90% coverage)

Results:
macrel.out.smorfs.faa : All smORFs predicted from Macrel
diamond.result.filtered.habitat.taxa.quality.tsv : Diamond results mapped with habitat,taxonomy and quality.(Cutoff: identity:0.9,E-value:1e-5)
diamond.result.filtered.faa : All mapped and filtered smORFs
habitat.tsv : Habitat annotation for each mapped smORF
taxonomy.tsv : Taxonomy annotation for each mapped smORF
quality.tsv : Quality annotation for each mapped smORF
summary.txt : Basic statistic of results
geo.png : Geographical and habitat distribution map