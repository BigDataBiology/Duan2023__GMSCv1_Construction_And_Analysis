'''
Concept:
Analyse if 90AA families are specific or multiple at the taxonomy rank.
'''

import pandas as pd

def fixformat(x):
    x = x.split(';')
    while len(x) < 7:
        x.append('')
    return ';'.join(x)

def reducetab(df):
    df = df.drop_duplicates()
    cols = list(df.columns)
    flag_multi = 'unknown'
    flag_specific = 'unknown'
    for i in range(len(cols)):
        rank = cols[i]
        w = df.loc[df[rank] != '', rank]
        w = w.value_counts()
        if len(w) > 1:
            flag_multi = f'{cols[i]}-multi'
            if i != 0:
                flag_specific = f'{cols[i-1]}-specific'
            else:
                flag_specific = ''
            break
        if len(w) == 1:
            flag_multi = ''
            flag_specific = f'{cols[i]}-specific'
    return flag_multi,flag_specific

def cal(infile,outfile):
    data = pd.read_table(infile,
                         header=None,
                         names=['smorf','taxonomy'])
    data['taxonomy'].replace('Unknown','',inplace=True)
    data.taxonomy = data.taxonomy.apply(lambda x: fixformat(x))
    data = data.groupby('smorf').apply(lambda x: x.taxonomy.tolist())
    data = data.reset_index()
    data = data.rename({0: 'taxonomy'}, axis=1)

    out = open(outfile,'wt')
    for _, smorf, tax in data.itertuples():
        number = len(tax)
        tax = [x.split(';') for x in tax]
        tax = pd.DataFrame(tax,
                           columns=['kingdom','phylum','class','order','family','genus','species'])
        flag_multi,flag_specific = reducetab(tax)   
        out.write(f'{smorf}\t{flag_multi}\t{flag_specific}\t{number}\n')
    out.close()

# Calculate number of taxonomy specific
def merge(infile,outfile):
    km = 0
    pm = 0
    cm = 0
    om = 0
    fm = 0
    gm = 0
    sm = 0

    ok = 0
    op = 0
    oc = 0
    oo = 0
    of = 0
    og = 0
    os = 0

    ps = 0
    cs = 0
    os = 0
    fs = 0
    gs = 0
    ss = 0
    
    n = 0
    unknown = 0
    with open(infile,'rt') as f:
        for line in f:
            linelist = line.strip().split('\t')
            if int(linelist[3]) >=3:
                n += 1
                if linelist[2] == 'kingdom-specific':
                    if linelist[1] == '':
                        ok += 1
                    elif linelist[1] == 'phylum-multi':
                        pm += 1
                elif linelist[2] == 'phylum-specific':
                    if linelist[1] == '':
                        op += 1
                    elif linelist[1] == 'class-multi':
                        cm += 1
                elif linelist[2] == 'class-specific':
                    if linelist[1] == '':
                        oc += 1
                    elif linelist[1] == 'order-multi':
                        om += 1
                elif linelist[2] == 'order-specific':
                    if linelist[1] == '':
                        oo += 1
                    elif linelist[1] == 'family-multi':
                        fm += 1
                elif linelist[2] == 'family-specific':
                    if linelist[1] == '':
                        of += 1
                    elif linelist[1] == 'genus-multi':
                        gm += 1
                elif linelist[2] == 'genus-specific':
                    if linelist[1] == '':
                        og += 1
                    elif linelist[1] == 'species-multi':
                        sm += 1
                elif linelist[2] == 'species-specific':
                    ss += 1
                elif linelist[1] == 'kingdom-multi':
                    km += 1
                elif linelist[1] == 'unknown' and linelist[2] == 'unknown':
                    unknown += 1
    gs = og + sm + ss
    fs = of + gm + gs
    os = oo + fm + fs
    cs = oc + om + os
    ps = op + cm + cs
    ks = ok + pm + ps 

    with open(outfile,'wt') as out:
        out.write(f'#{n} >=3 90AA families.{km} multi-kingdom families.{unknown} unknown families.\n')
        out.write(f'\tonly\tmulti\tspecific\n')
        out.write(f'species-specific\t{ss}\t0\t0\n')
        out.write(f'genus-specific\t{og}\t{sm}\t{ss}\n')
        out.write(f'family-specific\t{of}\t{gm}\t{gs}\n')
        out.write(f'order-specific\t{oo}\t{fm}\t{fs}\n')
        out.write(f'class-specific\t{oc}\t{om}\t{os}\n')
        out.write(f'phylum-specific\t{op}\t{cm}\t{cs}\n')
        out.write(f'kingdom-specific\t{ok}\t{pm}\t{ps}\n')

infile1 = 'metag_cluster_tax_90.tsv'
outfile1 = '90AA_taxa_multi_specific.tsv'
outfile2 = '90AA_specific_multi.tsv'

cal(infile1,outfile1)
merge(outfile1,outfile2)