'''
Concept:
Add length of PSSM and filter with target coverage >80%.
'''
def add_length(infile1,infile2,outfile):
    import gzip

    cdd_dict = {}
    with gzip.open(infile1,'rt') as f1:
        for line in f1:
            linelist = line.strip().split('\t')
            cdd_dict[linelist[0]] = linelist[4]

    with gzip.open(outfile,'wt',compresslevel=1) as out:
        with open(infile2,'rt') as f2:
            for line in f2:
                if line.startswith('smorf'):
                    continue
                else:
                    line = line.strip()
                    linelist = line.split('\t')
                    pssm = linelist[1].split('|')[2]
                    if cdd_dict[pssm] != '0':
                        out.write(f'{line}\t{cdd_dict[pssm]}\n')

def filter_cov(infile,outfile):
    import pandas as pd
    result = pd.read_csv(infile,compression='gzip',sep='\t',header=None,names=['smorf','cdd','query_length','score','align_length','identity','evalue','target_length'])
    result['tcov'] = result['align_length']/result['target_length']
    result = result[result['tcov'] >0.8]
    result.to_csv(outfile,sep='\t',index=None)

infile1 = 'cddid_all.tbl.gz'
infile2 = '90AA_cdd.tsv'
outfile1 = '90AA_cdd_tl.tsv.gz'
outfile2 = '1_cdd_tcov_90AA.tsv'

add_length(infile1,infile2,outfile1)
filter_cov(infile1,outfile2)