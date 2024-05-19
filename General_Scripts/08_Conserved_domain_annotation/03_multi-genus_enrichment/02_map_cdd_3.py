'''
Map CDD annotation.
'''
def merge_habitat_motif(cdd,annotate,infile,outfile):
    import pandas as pd
    
    motif = pd.read_csv(cdd,compression='gzip',sep='\t')
    motif['cdd'] = motif['cdd'].apply(lambda x:x.split('|')[2])
    motif['cdd'] = motif['cdd'].astype('int')
    habitat = pd.read_csv(infile,sep='\t',header=None,names=['smorf','habitat'])
    result = motif.merge(habitat,'right',on='smorf')

    cdd = pd.read_csv(annotate,compression='gzip',sep='\t',header=None,names=['cdd','accession','short_name','description','PSSM_Length'])
    merged = result.merge(cdd,'left',on='cdd')
    merged.to_csv(outfile,index=None,sep='\t')

def merge_motif(cdd,annotate,infile,outfile):
    import pandas as pd
    
    motif = pd.read_csv(cdd,compression='gzip',sep='\t')
    motif['cdd'] = motif['cdd'].apply(lambda x:x.split('|')[2])
    motif['cdd'] = motif['cdd'].astype('int')
    multi = pd.read_csv(infile,sep='\t',header=None,names=['smorf','number'])
    result = motif.merge(multi,'right',on='smorf')

    cdd = pd.read_csv(annotate,compression='gzip',sep='\t',header=None,names=['cdd','accession','short_name','description','PSSM_Length'])
    merged = result.merge(cdd,'left',on='cdd')
    merged.to_csv(outfile,index=None,sep='\t')

cdd = '1_cdd_tcov_90AA.tsv.gz'
annotate = 'cddid_all.tbl.gz'
infile1 = '90AA_multi_habitat.tsv'
infile2 = 'multi_genus_3.tsv'
outfile1 = '90AA_multi_habitat_cdd.tsv'
outfile2 = 'multi_genus_3_cdd.tsv'
merge_habitat_motif(cdd,annotate,infile1,outfile1)
merge_habitat_motif(cdd,annotate,infile2,outfile2)