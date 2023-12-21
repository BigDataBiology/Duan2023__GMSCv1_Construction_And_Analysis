'''
Extract bacterial and archaeal 90AA families with COG annotation
'''
import lzma
import gzip

def extract(infile1,infile2,outfile1,outfile2):
    taxa_dict = {}
    with lzma.open(infile1,'rt') as f1:
        for line in f1:
            linelist = line.strip().split('\t')
            if len(linelist) > 1:
                taxa_dict[linelist[0]] = linelist[1]

    out1 = open(outfile1,'wt')
    out2 = open(outfile2,'wt')
    with gzip.open(infile2,'rt') as f2:
        for line in f2:
            linelist = line.strip().split('\t',1)
            if linelist[0] in taxa_dict.keys():
                if taxa_dict[linelist[0]].startswith('d__Bacteria'):
                    out1.write(line)
                else:
                    out2.write(line)
    out1.close()
    out2.close()

def cog(infile1,infile2,infile3,outfile):
    import pandas as pd
    result = pd.read_table(infile1,sep='\t',skiprows=0,usecols=[0,1],header=None,names=['smorf','PSSM_Id'])
    result['PSSM_Id'] = result['PSSM_Id'].apply(lambda x:x.split('|')[2])
    result['PSSM_Id'] = result['PSSM_Id'].astype('int')
    cdd = pd.read_csv(infile2,sep='\t',header=None,names=['PSSM_Id','accession','short_name','description','PSSM_Length'])
    df = result.merge(cdd,'left',on='PSSM_Id')
    df= df[df['accession'].str.contains('COG')]

    cog = pd.read_csv(infile3,sep='\t',usecols=[0,1],names=['accession','category'])
    merged = df.merge(cog,'left',on='accession')

    merged.to_csv(outfile,sep='\t',index=None)

infile1 = '90AA_ref_taxonomy_format.tsv.xz'
infile2 = '1_cdd_tcov_90AA.tsv.gz'
infile3 = 'cddid_all.tbl'
infile4 = 'cog-20.def.tab.tsv'
outfile1 = 'bac_motif.txt'
outfile2 = 'arc_motif.txt'
outfile3 = '0_arc_motif_cog.tsv'
outfile4 = '0_bac_motif_cog.tsv'
outfile4 = '0_bg_motif_cog.tsv'

extract(infile1,infile2,outfile1,outfile2)
cog(outfile2,infile3,infile4,outfile3)
cog(outfile1,infile3,infile4,outfile4)
cog(infile2,infile3,infile4,outfile4)