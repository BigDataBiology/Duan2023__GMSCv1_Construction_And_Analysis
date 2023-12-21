'''
Map transmembrane or secreted families to taxonomy.
Map amino acid ratio to form helix, turn, and sheet of each 90AA family to taxonomy.
Count transmembrane fraction of each phylum.
Calculate the average amino acid ratio of the helix,turn,and sheet in the phylum


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

def map_secondary(infile1,infile2,outfile):
    tax = {}
    with open(infile1,'rt') as f1:
        for line in f1:
            linelist = line.strip().split('\t')
            if len(linelist) > 1:
                linelist[1] = linelist[1].replace(';','\t')
                tax[linelist[0]] = linelist[1]

    with open(outfile,'wt') as out:
        with open(infile2,'rt') as f2:
            for line in f2:
                line = line.strip()
                linelist = line.split('\t',1)
                if linelist[0] in tax.keys():
                    out.write(f'{line}\t{tax[linelist[0]]}\n')

def count_trans(infile,outfile):
    import pandas as pd
    df = pd.read_csv(infile,sep='\t',names=['transmembrane','smorf','domain','phylum','cl','order','family','genus','species'])
    trans_count = df.groupby(['domain','phylum'])['transmembrane'].value_counts()
    trans_count.to_csv(outfile)

def count_secondary(infile,outfile4,outfile5,outfile6):
    import pandas as pd

    df = pd.read_csv(infile,sep='\t',header=None,names=['smorf','Helix', 'Turn', 'Sheet','Taxonomy','Domain','Phylum','Cl','Order','family','Genus','Species'])
    helix = df.groupby(['Domain','Phylum'])['Helix'].mean()
    helix.to_csv(outfile4)
    turn = df.groupby(['Domain','Phylum'])['Turn'].mean()
    turn.to_csv(outfile5)
    sheet = df.groupby(['Domain','Phylum'])['Sheet'].mean()
    sheet.to_csv(outfile6)

infile1 = '90AA_tm_signal.tsv.gz'
infile2 = '90AA_ref_taxonomy_format.tsv.xz'
infile3 = '90AA_secondary.tsv.gz'
outfile1 = 'trans_taxa.tsv'
outfile2 = 'trans_phylum.csv'
outfile3 = '90AA_secondary_taxonomy.tsv'
outfile4 = 'helix_phylum.csv'
outfile5 = 'turn_phylum.csv'
outfile6 = 'sheet_phylum.csv'

trans = store_trans(infile1)
map_trans(trans,infile2,outfile1)
count_trans(outfile1,outfile2)
map_secondary(infile2,infile3,outfile3)
count_secondary(outfile3,outfile4,outfile5,outfile6)