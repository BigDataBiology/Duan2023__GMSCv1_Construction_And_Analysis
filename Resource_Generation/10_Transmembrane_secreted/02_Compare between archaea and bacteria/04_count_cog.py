'''
Count the number of each COG of smORFs with annotation
'''
import pandas as pd

def count_arc(infile,outfile):
    result = pd.read_csv(infile,sep='\t',header=None,names=['smorf','PSSM_Id','accession','short_name','description','PSSM_Length','category'])
    cog_count = result['accession'].value_counts()
    cog_count = cog_count.to_frame(name='arc_count').reset_index().rename(columns={'index':'cog'})
    cog_count['arc_percentage'] = cog_count['arc_count']/cog_count['arc_count'].sum()
    cog_count['arc_all'] = cog_count['arc_count'].sum()
    cog_count.to_csv(outfile,sep='\t',index=None)

def count_bg(infile,outfile):
    result = pd.read_csv(infile,sep='\t')
    cog_count = result['accession'].value_counts()
    cog_count = cog_count.to_frame(name='bg_count').reset_index().rename(columns={'index':'cog'})
    cog_count['bg_all'] = len(result.drop_duplicates('smorf',keep='first'))
    cog_count['bg_percentage'] = cog_count['bg_count']/cog_count['bg_all']
    cog_count.to_csv(outfile,sep='\t',index=None)

infile1 = '0_arc_motif_cog.tsv'
outfile1 = '1_arc_motif_cog_count.tsv'
infile2 = '0_bg_motif_cog.tsv'
outfile2 = '1_bg_motif_cog_count.tsv'

count_arc(infile1,outfile1)
count_bg(infile2,outfile2)
