'''
Add multiple or specific taxonomy for these families.
Merge all files to generate a table including multi-phylum 90AA families, habitats, the number of species.
'''
def map_multi(infile1,infile2,outfile):
    house_set = set()
    with open(infile1,'rt') as f1:
        for line in f1:
            house,number = line.strip().split('\t')
            house_set.add(house)

    with open(outfile,'wt') as out:
        with open(infile2,'rt') as f2:
            for line in f2:
                family,anno = line.strip().split('\t',1)
                if family in house_set:
                    out.write(f'{family}\t{anno}\n')

def merge():
    import pandas as pd

    multi = pd.read_csv('housekeeping_multi.tsv',sep='\t',header=None,names=['smorf','multi','specific','smorf number of family'])
    species = pd.read_csv('housekeeping_species.tsv',sep='\t',header=None,names=['smorf','species_number'])
    merged_species = multi.merge(species,how = 'left',on='smorf')
    motif = pd.read_csv('all_habitat_motif.tsv',sep='\t')
    merged = merged_species.merge(motif,how = 'left',on='smorf')
    merged.to_csv('housekeeping_motif_species_multi.tsv',sep='\t',index=None)

    df = pd.read_csv('housekeeping_motif_species_multi.tsv',sep='\t')
    df = df[df['multi'].isin(['phylum-multi','kingdom-multi'])]
    df.to_csv('housekeeping_motif_species_multi_phylum_all.tsv',sep='\t',index=None)

infile1 = 'housekeeping_species.tsv'
infile2 = '90AA_taxa_multi_specific.tsv'
outfile = 'housekeeping_multi.tsv'

map_multi(infile1,infile2,outfile)
merge()