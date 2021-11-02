# Analysis of GMSC against metaproteome sets

This set of scripts search for exact matches in the detected
peptides in metaproteomes available in the PRIDE database.

The valid hits were evaluated over the peptides that passed
the FDR test presenting evidence of realness.

The coverage of peptides was calculated and those presenting
a minimum coverage of 50% are reported as a role. The string
of mapping was also retrieved following a modified Phred33
model.

## Data used in this test are listed in:
  
```
PRIDE_list.txt
```