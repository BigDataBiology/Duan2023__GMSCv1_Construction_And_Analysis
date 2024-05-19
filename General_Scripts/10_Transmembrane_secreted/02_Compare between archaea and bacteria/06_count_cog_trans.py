def store(infile):
    trans = set()
    with open(infile,'rt') as f:
        for line in f:
            trans.add(line.strip())
    return trans

def split(trans,infile,outfile1,outfile2):
    out1 = open(outfile1,'wt')
    out1.write(f'smorf\tPSSM_Id\taccession\tshort_name\tdescription\tPSSM_Length\tcategory\n')
    out2 = open(outfile2,'wt')
    out2.write(f'smorf\tPSSM_Id\taccession\tshort_name\tdescription\tPSSM_Length\tcategory\n')

    with open(infile,'rt') as f:
        for line in f:
            if line.startswith('smorf'):
                continue
            else:
                linelist = line.strip().split('\t')
                if linelist[0] in trans:
                    out1.write(line)
                else:
                    out2.write(line)
    out1.close()
    out2.close()

def count_arc(infile1,infile2,outfile1,outfile2):
    import pandas as pd
    result = pd.read_csv(infile1,sep='\t')
    cog_count = result['accession'].value_counts()
    cog_count = cog_count.to_frame(name='arc_trans_count').reset_index().rename(columns={'index':'cog'})
    cog_count['arc_trans_all'] = len(result.drop_duplicates('smorf',keep='first'))
    cog_count.to_csv(outfile1,sep='\t',index=None)

    result = pd.read_csv(infile2,sep='\t')
    cog_count = result['accession'].value_counts()
    cog_count = cog_count.to_frame(name='arc_not_trans_count').reset_index().rename(columns={'index':'cog'})
    cog_count['arc_not_trans_all'] = len(result.drop_duplicates('smorf',keep='first'))
    cog_count.to_csv(outfile2,sep='\t',index=None)

def count_bac(infile1,infile2,outfile1,outfile2):
    import pandas as pd
    result = pd.read_csv(infile1,sep='\t')
    cog_count = result['accession'].value_counts()
    cog_count = cog_count.to_frame(name='bac_trans_count').reset_index().rename(columns={'index':'cog'})
    cog_count['bac_trans_all'] = len(result.drop_duplicates('smorf',keep='first'))
    cog_count.to_csv(outfile1,sep='\t',index=None)

    result = pd.read_csv(infile2,sep='\t')
    cog_count = result['accession'].value_counts()
    cog_count = cog_count.to_frame(name='bac_not_trans_count').reset_index().rename(columns={'index':'cog'})
    cog_count['bac_not_trans_all'] = len(result.drop_duplicates('smorf',keep='first'))
    cog_count.to_csv(outfile2,sep='\t',index=None)

infile = '90AA_tm_signal.tsv'

infile1 = '0_arc_motif_cog.tsv'
infile2 = '0_bac_motif_cog.tsv'

outfile1 = '0_arc_motif_cog_trans.tsv'
outfile2 = '0_arc_motif_cog_not_trans.tsv'
outfile3 = '0_bac_motif_cog_trans.tsv'
outfile4 = '0_bac_motif_cog_not_trans.tsv'

outfile5 = '9_arc_motif_cog_count_trans.tsv'
outfile6 = '9_arc_motif_cog_count_not_trans.tsv'
outfile7 = '9_bac_motif_cog_count_trans.tsv'
outfile8 = '9_bac_motif_cog_count_not_trans.tsv'

trans = store(infile)
split(trans,infile1,outfile1,outfile2)
split(trans,infile2,outfile3,outfile4)
count_arc(outfile1,outfile2,outfile5,outfile6)
count_bac(outfile3,outfile4,outfile7,outfile8)