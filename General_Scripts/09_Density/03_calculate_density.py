'''
Calculate density of phylum and genus
'''
import pandas as pd

smorf_number = pd.read_csv('cpnumber_per_tax.tsv',sep= '\t',header=None,names=['taxonomy','number'])
smorf_number = smorf_number[smorf_number['taxonomy'].str.contains('p__')]
smorf_number['taxonomy'] = smorf_number['taxonomy'].str.replace('p__','')
smorf_number['rank'] = 'phylum'

per_tax = pd.read_csv('per_tax_rank.txt',sep= '\t',header=None,names=['rank','taxonomy','nbps'])
tax_number_nbps = smorf_number.merge(per_tax,'inner',on=['rank','taxonomy'])

tax_number_nbps['density'] = tax_number_nbps['number']*1e6/tax_number_nbps['nbps']
tax_number_npbs = tax_number_nbps.sort_values('density',ascending=False)
tax_number_npbs.to_csv('density_phylum.tsv',sep='\t',index=None)


smorf_number = pd.read_csv('cpnumber_per_tax_sum.tsv',sep= '\t',header=None,names=['taxonomy','number'])
smorf_number = smorf_number[smorf_number['taxonomy'].str.contains('g__')]
smorf_number['taxonomy'] = smorf_number['taxonomy'].str.replace('g__','')
smorf_number['rank'] = 'genus'

per_tax = pd.read_csv('per_tax_rank.txt',sep= '\t',header=None,names=['rank','taxonomy','nbps'])
tax_number_nbps = smorf_number.merge(per_tax,'inner',on=['rank','taxonomy'])

tax_number_nbps['density'] = tax_number_nbps['number']*1e6/tax_number_nbps['nbps']
tax_number_nbps = tax_number_nbps.sort_values('density',ascending=False)
tax_number_nbps.to_csv('density_genus.tsv',sep='\t',index=None)