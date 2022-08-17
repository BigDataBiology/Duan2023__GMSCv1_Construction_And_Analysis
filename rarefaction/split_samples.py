# Use pypy3 for better performance
# pypy3 split_samples.py

import csv, lzma, re

with lzma.open('100AA_sample.tsv.xz', 'rt') as fileIn:
    tsvIn = csv.reader(fileIn, delimiter='\t')

    for i, row in enumerate(tsvIn):

        smorf_id = str(int(re.search(r'A\..*', row[0]).group(0)[2:].replace('_', '')))

        with open('data_samples/' + row[1], 'a') as sample:
            sample.write(smorf_id + '\n')

        print(i, smorf_id, row[1])