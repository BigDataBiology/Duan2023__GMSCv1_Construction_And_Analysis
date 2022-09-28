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

e.g.

```
>GMSC10.90AA.000_000_000_000
ATGGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCTGCGGCATAA
>GMSC10.90AA.000_000_000_001
GTGGCAGCGGCTGCGGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGTGGCGGTGGCTGTGGCGGCTGCGGCGACAGCGGCATGA
>GMSC10.90AA.000_000_000_002
ATGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCAGCGGCAGCAGCGGCAGCGGCGGCGGCGGCGGCGGCAGCGCAACAATCGACCCTTGAATCAACGAACGCAATTTATGTTTATAATAATCTAAATAAAAAAGCTGTACAGCTGTAA
```

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

e.g.

```
>GMSC10.50AA.000_000_000_000
ATGGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCTGCGGCATAA
>GMSC10.50AA.000_000_000_001
GTGGCAGCGGCTGCGGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGCTGTGGCGGTGGCTGTGGCGGCTGCGGCGACAGCGGCATGA
>GMSC10.50AA.000_000_000_002
ATGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCAGCGGCAGCAGCGGCAGCGGCGGCGGCGGCGGCGGCAGCGCAACAATCGACCCTTGAATCAACGAACGCAATTTATGTTTATAATAATCTAAATAAAAAAGCTGTACAGCTGTAA
```
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

1. 100AA smORF accession

2. 90AA smORF accession

3. 50AA smORF accession

e.g.

```
GMSC10.100AA.000_000_000_000    GMSC10.90AA.000_000_000_003     GMSC10.50AA.000_000_000_003
GMSC10.100AA.000_000_000_001    GMSC10.90AA.000_000_000_063     GMSC10.50AA.000_000_000_064
GMSC10.100AA.000_000_000_002    GMSC10.90AA.000_000_046_429     GMSC10.50AA.000_000_036_067
```

## Habitat mapping files

Table relating smORF accession and their habitat of origin.

Habitat contains microontology and host (separated by ' # '). 

Multiple habitats are separated by ','.

Microontology is a scheme used to annotate environments via metadata, it has different levels of complexity separated by ':'

Host NCBI taxid is used to annotate hosts of host-associated metagenomes via metadata.

If smORF is from isolated genome, its habitat will be annotated as isolate.

Columns: 

1. smORF accession

2. Habitat

### 100% identity smORF catalog

**Files:**

Habitat mapping file: `100AA_ref_multi_habitat.tsv.xz`

e.g.
```
GMSC10.100AA.000_000_000_016    aquatic:marine:pelagic
GMSC10.100AA.000_000_000_017    aquatic:marine;host-associated:animal host:coral reef # 51062
GMSC10.100AA.000_000_000_018    host-associated:plant host:plant litter # 381124
GMSC10.100AA.000_000_000_019    terrestrial:soil # 2706
GMSC10.100AA.000_000_000_020    terrestrial:soil # 38727
```

### 90% identity smORF catalog

**Files:**

Habitat mapping file: `90AA_ref_multi_habitat.tsv.xz`

e.g.

```
GMSC10.90AA.000_000_000_000     aquatic:saline
GMSC10.90AA.000_000_000_001     aquatic:freshwater:lake
GMSC10.90AA.000_000_000_002     aquatic:saline
GMSC10.90AA.000_000_000_003     aquatic:freshwater
GMSC10.90AA.000_000_000_004     host-associated:animal host:digestive tract:intestine # 46569
```

### 50% identity smORF catalog


**Files:**

Habitat mapping file: `50AA_ref_multi_habitat.tsv.xz`

e.g.

```
GMSC10.50AA.000_000_000_000     aquatic:saline
GMSC10.50AA.000_000_000_001     aquatic:freshwater:lake
GMSC10.50AA.000_000_000_002     aquatic:saline
GMSC10.50AA.000_000_000_003     aquatic:freshwater
GMSC10.50AA.000_000_000_004     host-associated:animal host:digestive tract:intestine # 46569
```

## Taxonomy mapping files

Table relating smORF accession and their taxonomy.

If the taxonomy of smORFs in a cluster is different, we annotated taxonomy using LCA. But we ignored the blank to make it more specific.

Columns: 

1. smORF accession

2. Taxonomy

### 100% identity smORF catalog

**Files:**

Taxonomy mapping file: `100AA_ref_taxonomy_format.tsv.xz`

e.g.
```
GMSC10.100AA.000_000_000_019    d__Bacteria;p__Actinobacteriota;c__Thermoleophilia;o__Solirubrobacterales;f__Solirubrobacteraceae;g__Solirubrobacter
GMSC10.100AA.000_000_000_020    d__Bacteria;p__Actinobacteriota;c__Thermoleophilia;o__Solirubrobacterales;f__Solirubrobacteraceae;g__Solirubrobacter
GMSC10.100AA.000_000_000_021    d__Bacteria;p__Actinobacteriota;c__Thermoleophilia;o__Solirubrobacterales;f__Thermoleophilaceae;g__AC-37
```

### 90% identity smORF catalog

**Files:**

Taxonomy mapping file: `90AA_ref_taxonomy_format.tsv.xz`

e.g.

```
GMSC10.90AA.000_000_000_082     d__Archaea;p__Thermoproteota;c__Nitrososphaeria;o__Nitrososphaerales;f__Nitrososphaeraceae;g__UBA10452;s__UBA10452 sp003176995
GMSC10.90AA.000_000_000_083     d__Bacteria;p__Actinobacteriota;c__Actinomycetia;o__Streptosporangiales;f__Streptosporangiaceae
GMSC10.90AA.000_000_000_084     d__Archaea;p__Thermoproteota;c__Nitrososphaeria;o__Nitrososphaerales;f__Nitrososphaeraceae;g__UBA10452;s__UBA10452 sp003176995
```

### 50% identity smORF catalog


**Files:**

Taxonomy mapping file: `50AA_ref_taxonomy_format.tsv.xz`

e.g.

```
GMSC10.50AA.000_000_000_080     d__Archaea;p__Thermoproteota;c__Nitrososphaeria;o__Nitrososphaerales;f__Nitrososphaeraceae;g__UBA10452;s__UBA10452 sp003176995
GMSC10.50AA.000_000_000_081     d__Bacteria;p__Actinobacteriota;c__Actinomycetia;o__Streptosporangiales;f__Streptosporangiaceae
GMSC10.50AA.000_000_000_082     d__Archaea;p__Thermoproteota;c__Nitrososphaeria;o__Nitrososphaerales;f__Nitrososphaeraceae;g__UBA10452;s__UBA10452 sp003176995
```