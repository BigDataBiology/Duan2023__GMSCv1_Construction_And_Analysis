# Frozen versions of data
## FASTA files (FNA & FAA)

### 100% identity smORF catalog

100% identity smORF catalog contains all the non-singletons in raw data, and rescued singletons that can be aligned to 90% of 50% identity representitive pepetides.

The number of 100% identity smORF catalog is `977,020,743`.

**Identifier:** 

Peptides are named: 
`>GMSC10.100AA.XXX_XXX_XXX_XXX`

Where `XXX_XXX_XXX_XXX` is a unique numerical identifier (starting at zero). Numbers were assigned in order of increasing number of copies. So that the lower the number, the lower the number of copies of that peptide was present in the input data. And if the number of copies is same, numbers were assigned in order of letters of peptides.

**Files:**

FAA: `100AA_GMSC.faa.xz`

e.g.
```
>GMSC10.100AA.000_000_000_000
MAAAAAAAAAAAAAAAAAAAAAAGGARGENFDENKIDAEREAGVDVQVDRGVLLLLLLILLLLLLLLLLLLVLVTLAAVLPCRDKGGD
>GMSC10.100AA.000_000_000_001
MAAAAAAAAAAAAAFVVFVGFPSSSFLSDDFLTFLSESGKDGRAGFRLRGNRGGGALVSWYPANICWASIAASTRLEMYRAVNSERS
>GMSC10.100AA.000_000_000_002
MAAAAAAAAAAAAKGSAVRNIFSTGMLETLRALADGVAASDILPRVLAVRHRSILPIPRVSILAVFRIMYVCTA
```
FNA: `100AA_metag.fna.xz`

e.g.

```
>GMSC10.100AA.000_960_031_295
ATGAATGCCCGTGGTAGATCGGACAGAGAATTAGAGCGAGCAAAAACAATGATCCCGAGTCGGGGATTCCCGATTATCAAGGACGAATTCGGGTCTTGTTTCATTAGGGCTTTATTTACTGGGCTTTTAATGGGTCTAGCGTTGTCTTAA
>GMSC10.100AA.000_920_857_026
ATGAACCGCAGCGACATGCTGCGCATGGGGCTGACCGATGGTGACGACGTCGATCTGGTCGGCGATGCGGGCGACAATGGCGACCGCCGCTTCAACAAGCTGCGCGTCGTCGAATATTCGATTCCGGAAGGGTGCGTCGGGGCCTATTACCCCGAGTGCAACCTGCTGATGCCGGTCGCGCACCATGCGCGCGAAAGCCATGTGCCTGCCGCCAAGTCGGTGCCGGTGCGGATCGAGAAGACGCGCTGA
>GMSC10.100AA.000_857_592_878
GTGTATGAGGAGGTTGAAGATGCATTGCCAAATATAGGAACCATGGCAAATGAGATCGTGAAAGGCAAATCTGAGGTGATTGAGTTGAATGCTTCTATTCAAGAATTGAAAGAAGATGCAAAGTGGAGCAAAATGGAAATCCGGAAATTGAAAGTGCTGGTGAAAGTCTGTGTAGTGTGGGTTTGTGTAATGAACCTTGTCATTGCTTACCAAATGATTGGTAAAGCAAAAGAAACAAGCTTTGTTCTAGGAAAGTATTAG
```
Rename mapping file: `100AA_rename.tsv.xz`

Columns: 

1. original name 

2. new name 

e.g.
```
GMSC10.SMORF.004_062_819_852    GMSC10.100AA.000_000_000_000
GMSC10.SMORF.004_153_471_380    GMSC10.100AA.000_000_000_001
GMSC10.SMORF.000_276_383_562    GMSC10.100AA.000_000_000_002
GMSC10.SMORF.000_264_320_897    GMSC10.100AA.000_000_000_003
GMSC10.SMORF.000_254_909_641    GMSC10.100AA.000_000_000_004
```
### 90% identity smORF catalog

90% identity smORF catalog contains the representitive peptides by clustering at 90% identidy using Linclust.

The number of 90% identity smORF catalog is `287,926,875`.

**Identifier:**

Peptides are named: 
`>GMSC10.90AA.XXX_XXX_XXX_XXX`

Where `XXX_XXX_XXX_XXX` is a unique numerical identifier (starting at zero). Numbers were assigned in order of increasing number of peptides in clusters. So that the lower the number, the lower the number of peptides in the cluster. And if the number of peptides in clusters is same, numbers were assigned in order of letters of representitive peptides in each cluster.

**Files:**

FAA: `90AA_GMSC.faa.xz`

e.g.

```
>GMSC10.90AA.000_000_000_000
MAAAAAAAAAAAAA
>GMSC10.90AA.000_000_000_001
MAAAAAAAAAAAAAAAAAAAAAAAAAAVAVAVAAAATAA
>GMSC10.90AA.000_000_000_002
MAAAAAAAAAAAAAAAAAAAAAAAAAQQSTLESTNAIYVYNNLNKKAVQL
```
FNA: `90AA_metag.fna.xz`

Rename mapping file: `90AA_rename.tsv.xz`

Columns: 

1. original name of representitive peptides

2. new name 

e.g.

```
GMSC10.SMORF.002_858_651_254    GMSC10.90AA.000_000_000_000
GMSC10.SMORF.003_257_627_643    GMSC10.90AA.000_000_000_001
GMSC10.SMORF.002_852_461_498    GMSC10.90AA.000_000_000_002
GMSC10.SMORF.004_063_339_490    GMSC10.90AA.000_000_000_003
GMSC10.SMORF.003_074_035_489    GMSC10.90AA.000_000_000_004
```
### 50% identity smORF catalog

**Identifier:** 

50% identity smORF catalog contains the representitive peptides by clustering at 50% identidy using Linclust.

The number of 90% identity smORF catalog is `231,429,250`.

Peptides are named: 
`>GMSC10.50AA.XXX_XXX_XXX_XXX`

Where `XXX_XXX_XXX_XXX` is a unique numerical identifier (starting at zero). Numbers were assigned in order of increasing number of peptides in clusters. So that the lower the number, the lower the number of peptides in the cluster. And if the number of peptides in clusters is same, numbers were assigned in order of letters of representitive peptides in each cluster.

**Files:**

FAA: `50AA_GMSC.faa.xz`

e.g.

```
>GMSC10.50AA.000_000_000_000
MAAAAAAAAAAAAA
>GMSC10.50AA.000_000_000_001
MAAAAAAAAAAAAAAAAAAAAAAAAAAVAVAVAAAATAA
>GMSC10.50AA.000_000_000_002
MAAAAAAAAAAAAAAAAAAAAAAAAAQQSTLESTNAIYVYNNLNKKAVQL

```
FNA: `50AA_metag.fna.xz`

Rename mapping file: `50AA_rename.tsv.xz`

Columns: 

1. original name of representitive peptides 

2. new name 

e.g.
```
GMSC10.SMORF.002_858_651_254    GMSC10.50AA.000_000_000_000
GMSC10.SMORF.003_257_627_643    GMSC10.50AA.000_000_000_001
GMSC10.SMORF.002_852_461_498    GMSC10.50AA.000_000_000_002
GMSC10.SMORF.004_063_339_490    GMSC10.50AA.000_000_000_003
GMSC10.SMORF.003_074_035_489    GMSC10.50AA.000_000_000_004
GMSC10.SMORF.003_089_439_589    GMSC10.50AA.000_000_000_005
```
## Family mapping files

The table relating the name of smORFs, and the clusters they belong to at 90% and 50% identity.

**Files:**

Family mapping file: `all_0.9_0.5_family.tsv.xz`

Columns: 

1. 100AA smORFs 

2. 90AA smORFs

3. 50AA smORFs

e.g.

```
GMSC10.100AA.000_976_791_810    GMSC10.90AA.000_239_231_375     GMSC10.50AA.000_177_946_388
GMSC10.100AA.000_976_810_884    GMSC10.90AA.000_287_372_025     GMSC10.50AA.000_230_005_140
GMSC10.100AA.000_975_103_963    GMSC10.90AA.000_265_921_230     GMSC10.50AA.000_216_386_407
GMSC10.100AA.000_976_980_042    GMSC10.90AA.000_287_670_730     GMSC10.50AA.000_231_342_197
GMSC10.100AA.000_976_925_591    GMSC10.90AA.000_287_480_299     GMSC10.50AA.000_230_896_312
```
