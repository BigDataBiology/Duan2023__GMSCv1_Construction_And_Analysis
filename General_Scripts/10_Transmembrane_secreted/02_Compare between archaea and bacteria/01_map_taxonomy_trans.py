'''
Map transmembrane or secreted families to taxonomy.
Count transmembrane fraction of each phylum.
'''

def store_trans(infile1):
    import gzip
    trans = set()
    with gzip.open(infile1,'rt') as f:
        for line in f:
            trans.add(line.strip())
    return trans

def map_trans(trans,infile2,outfile):
    import lzma
    with open(outfile,'wt') as out:
        with lzma.open(infile2,'rt') as f:
            for line in f:
                linelist = line.strip().split('\t')
                if len(linelist) > 1:
                    linelist[1] = linelist[1].replace(';','\t')
                    if linelist[0] in trans:
                        out.write(f'Y\t{linelist[0]}\t{linelist[1]}\n')
                    else:
                        out.write(f'N\t{linelist[0]}\t{linelist[1]}\n')

def count_trans(infile,outfile):
    import pandas as pd
    df = pd.read_csv(infile,sep='\t',names=['transmembrane','smorf','domain','phylum','cl','order','family','genus','species'])
    trans_count = df.groupby(['domain','phylum'])['transmembrane'].value_counts()
    trans_count.to_csv(outfile)

infile1 = '90AA_tm_signal.tsv.gz'
infile2 = '90AA_ref_taxonomy_format.tsv.xz'
outfile1 = 'trans_taxa.tsv'
outfile2 = 'trans_phylum.csv'


trans = store_trans(infile1)
map_trans(trans,infile2,outfile1)
count_trans(outfile1,outfile2)
