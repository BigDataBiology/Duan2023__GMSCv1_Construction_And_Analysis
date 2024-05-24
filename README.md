# A catalogue of small proteins from the global microbiome

This repository contains files and scripts to generate analysis and figures in the manuscript _A catalogue of small proteins from the global microbiome_:

> Yiqian Duan, Celio Dias Santos-Junior, Thomas Sebastian Schmidt, Anthony Fullam, Breno L. S. de Almeida, Chengkai Zhu, Kuhn Michael, Xing-Ming Zhao, Peer Bork, Luis Pedro Coelho
> bioRxiv 2023.12.27.573469; doi: https://doi.org/10.1101/2023.12.27.573469

The results Global Microbial SMORFs Catalogue (GMSC) is available at https://gmsc.big-data-biology.org

## Structure

The folder `Resource_Generation` contains scripts to generate the GMSC resource from raw data. Note that this requires downloading all the contigs from [SPIRE](https://spire.embl.de) and [ProGenomes v2](https://progenomes2.embl.de/) as well as very large computational resources. The scripts are provided for transparency and reproducibility, but we recommend using the precomputed data (deposited at Zenodo or included here, see below) and the GMSC resource at https://gmsc.big-data-biology.org.

The folder `Manuscript_Analysis` contains pre-computed files and scripts to run the analysis and generate figures included in the GMSC manuscript. The scripts are written in Python (depenencies listed below). Generally speaking, these do not require large computational resources and interested users can run them on their own machines and adapt them to perform follow-up analyses.

## Dependencies

The following are required for the scripts (other versions may work, we list the ones that were used).

| **Software** | **Availability** |
| :---: | :---: |
| NGLess (v.1.3.0) | https://github.com/ngless-toolkit/ngless |
| Prodigal (v 2.6.3) | https://github.com/hyattpd/Prodigal |
| Macrel (v.0.5) | https://github.com/BigDataBiology/macrel |
| JUG (v.2.1.1) | https://github.com/luispedro/jug |
| MMseqs2 | https://github.com/soedinglab/MMseqs2 |
| Swipe (v.2.1.1) | https://github.com/torognes/swipe |
| DIAMOND (v.2.0.4) | https://github.com/bbuchfink/diamond |
| HMMer (v.3.3.2) | https://hmmer.org/ |
| MAFFT (v.7.475) | https://mafft.cbrc.jp/alignment/software/ |
| RNAcode (v.0.3) | https://github.com/ViennaRNA/RNAcode |
| BWA (v.0.7.17) | https://github.com/lh3/bwa |
| BLAST (v.2.13.0) | https://blast.ncbi.nlm.nih.gov/Blast.cgi |
| TMHMM (v.2.0) | https://services.healthtech.dtu.dk/services/TMHMM-2.0/ |
| SignalP (v.5.0) | https://services.healthtech.dtu.dk/services/SignalP-5.0/ |

## Data Availability

### Database

These databases are used in the construction and analysis of the catalogue.

| **Database** | **Availability** |
| :---: | :---: |
| SPIRE | https://spire.embl.de |
| ProGenomes v2 | https://progenomes2.embl.de/ |
| AntiFam (v.7.0) | ftp://ftp.ebi.ac.uk/pub/databases/Pfam/AntiFam/ |
| PRIDE | https://www.ebi.ac.uk/pride/ |
| RefSeq | https://ftp.ncbi.nlm.nih.gov/refseq/release/ |
| The Conserved Domain Database | https://ftp.ncbi.nih.gov/pub/mmdb/cdd |
| GTDB R95 | https://gtdb.ecogenomic.org/ |

### Preprocessed data

smORF catalogue & annotations: The smORF catalogue and its annotations are available at https://doi.org/10.5281/zenodo.7944370

Preprocessed data: For convenience, the preprocessed files are available under the `Manuscript_anlysis/data` folder.

