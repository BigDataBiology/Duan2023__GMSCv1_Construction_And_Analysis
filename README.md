# A catalogue of small proteins from the global microbiome
This repository contains files and scripts to generate analysis and figures in the manuscript "A catalogue of small proteins from the global microbiome":
> Yiqian Duan, Celio Dias Santos-Junior, Thomas Sebastian Schmidt, Anthony Fullam, Breno L. S. de Almeida, Chengkai Zhu, Kuhn Michael, Xing-Ming Zhao, Peer Bork, Luis Pedro Coelho
bioRxiv 2023.12.27.573469; doi: https://doi.org/10.1101/2023.12.27.573469

The global microbial smORFs catalogue (GMSC) is available at https://gmsc.big-data-biology.org

## Introduction

The folder **General_Scripts** contains scripts to generate GMSC resourece from the raw data.

The folder **Manuscript_Analysis** contains pre-computed files and scripts to run the analysis and generate figures included in the GMSC manuscript.

## Dependencies

The softwares are required for the scripts.

| **Software** | **Availability** |
| :---: | :---: |
| NGLess (v.1.3.0) | https://github.com/ngless-toolkit/ngless |
| Prodigal (v 2.6.3) | https://github.com/hyattpd/Prodigal |
| Macrel (v.0.5) | https://github.com/BigDataBiology/macrel |
| MMseqs2 | https://github.com/soedinglab/MMseqs2 |
| Swipe (v.2.1.1) | https://github.com/torognes/swipe |
| DIAMOND (v.2.0.4) | https://github.com/bbuchfink/diamond |
| HMMer (v.3.3.2) | http://hmmer.org/ |
| MAFFT (v.7.475) | https://mafft.cbrc.jp/alignment/software/ |
| RNAcode (v.0.3) | https://github.com/ViennaRNA/RNAcode |
| BWA (v.0.7.17) | https://github.com/lh3/bwa |
| BLAST (v.2.13.0) | https://blast.ncbi.nlm.nih.gov/Blast.cgi |
| TMHMM (v.2.0) | https://services.healthtech.dtu.dk/services/TMHMM-2.0/ |
| SignalP (v.5.0) | https://services.healthtech.dtu.dk/services/SignalP-5.0/ |

## Data Availability

### Database

Theese databases are used in the construction and analysis of the catalogue.

| **Database** | **Availability** |
| :---: | :---: |
| SPIRE | http://spire.embl.de |
| ProGenomes v2 | http://progenomes2.embl.de/ |
| AntiFam (v.7.0) | ftp://ftp.ebi.ac.uk/pub/databases/Pfam/AntiFam/ |
| PRIDE | https://www.ebi.ac.uk/pride/ |
| RefSeq | https://ftp.ncbi.nlm.nih.gov/refseq/release/ |
| The Conserved Domain Database | https://ftp.ncbi.nih.gov/pub/mmdb/cdd |
| GTDB R95 | https://gtdb.ecogenomic.org/ |

### Preprocessed data

smORF catalogue & annotations: The smORF catalogue and its annotations are available at https://doi.org/10.5281/zenodo.7944370.

Preprocessed data: For convenience, the preprocessed files are available under the Preprocessed_Files folder.