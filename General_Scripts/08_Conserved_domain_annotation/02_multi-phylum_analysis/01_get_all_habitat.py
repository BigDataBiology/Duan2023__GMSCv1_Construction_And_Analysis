'''
Select 90AA smORF families across all 8 habitat categories.
Add cdd annotation to these 90AA smORF families.
'''
def map_high(infile,outfile):
    import lzma

    higher_level = {
            'fermented food' : 'anthropogenic',
            'activated sludge' : 'anthropogenic',
            'wastewater' : 'anthropogenic',
            'built environment' : 'anthropogenic',
            'anthropogenic': 'anthropogenic',
            'groundwater' : 'aquatic',
            'river associated' : 'aquatic',
            'lake associated' : 'aquatic',
            'water associated' : 'aquatic',
            'marine' : 'aquatic',
            'pond associated' : 'aquatic',
            'plant associated' : 'soil/plant',
            'soil' : 'soil/plant',
            'bird gut' : 'other animal',
            'chicken gut' : 'other animal',
            'cattle rumen' : 'other animal',
            'bee gut' : 'other animal',
            'dog associated' : 'other animal',
            'cattle associated' : 'other animal',
            'insect gut' : 'other animal',
            'crustacean associated' : 'other animal',
            'planarian associated' : 'other animal',
            'sponge associated' : 'other animal',
            'goat rumen' : 'other animal',
            'crustacean gut' : 'other animal',
            'annelidae associated' : 'other animal',
            'bird skin' : 'other animal',
            'beatle gut' : 'other animal',
            'termite gut' : 'other animal',
            'fish gut' : 'other animal',
            'tunicate associated' : 'other animal',
            'mussel associated' : 'other animal',
            'mollusc associated' : 'other animal',
            'ship worm associated' : 'other animal',
            'wasp gut' : 'other animal',
            'insect associated' : 'other animal',
            'coral associated' : 'other animal',
            'turtle gut' : 'other animal',
            'human urogenital tract' : 'other human',
            'human associated' : 'other human',
            'human respiratory tract' : 'other human',
            'human skin' : 'other human',
            'human digestive tract' : 'other human',
            'human saliva' : 'other human',
            'human mouth' : 'other human',
            'human respiratory tract' : 'other human',
            'human skin' : 'other human',
            'human digestive tract' : 'other human',
            'human saliva' : 'other human',
            'human mouth' : 'other human',
            'human gut' : 'human gut',
            'isolate' : 'isolate',
            'dog gut' : 'mammal gut',
            'cat gut' : 'mammal gut',
            'rat gut' : 'mammal gut',
            'cattle gut' : 'mammal gut',
            'deer gut' : 'mammal gut',
            'mouse gut' : 'mammal gut',
            'primate gut' : 'mammal gut',
            'pig gut' : 'mammal gut',
            'bear gut' : 'mammal gut',
            'bat gut' : 'mammal gut',
            'goat gut' : 'mammal gut',
            'rodent gut' : 'mammal gut',
            'fisher gut' : 'mammal gut',
            'coyote gut' : 'mammal gut',
            'rabbit gut' : 'mammal gut',
            'horse gut' : 'mammal gut',
            'guinea pig gut' : 'mammal gut',
            'dolphin gut' : 'mammal gut',
            'whale gut' : 'mammal gut'
            }

    habitat_high_set = set()

    with open(outfile,'wt') as out:
        with lzma.open(infile,'rt') as f:
            for line in f:
                smorf,habitat= line.strip().split('\t')
                for item in habitat.split(','):
                    if item in higher_level.keys():
                        habitat_high = higher_level[item]
                    else:
                        habitat_high = 'other'
                    if habitat_high != 'isolate':
                        habitat_high_set.add(habitat_high)
                higher_habitat = ','.join(sorted(list(habitat_high_set)))
                habitat_high_set = set()
                if higher_habitat == 'anthropogenic,aquatic,human gut,mammal gut,other,other animal,other human,soil/plant':
                    out.write(line)

def merge_habitat_motif(infile1,infile2,infile3,outfile):
    import pandas as pd
    motif = pd.read_csv(infile1,compression='gzip',sep='\t')
    motif['cdd'] = motif['cdd'].apply(lambda x:x.split('|')[2])
    motif['cdd'] = motif['cdd'].astype('int')
    habitat = pd.read_csv(infile2,sep='\t',header=None,names=['smorf','habitat'])
    result = motif.merge(habitat,'right',on='smorf')

    cdd = pd.read_csv(infile3,compression='gzip',sep='\t',header=None,names=['cdd','accession','short_name','description','PSSM_Length'])
    merged = result.merge(cdd,'left',on='cdd')
    merged.to_csv(outfile,index=None,sep='\t')

infile1 = 'GMSC10.90AA.general_habitat.tsv.xz'
infile2 = '1_cdd_tcov_90AA.tsv.gz'
infile3 = 'cddid_all.tbl.gz'
outfile1 = 'all_habitat_smorf.tsv'
outfile2 = 'all_habitat_motif_right.tsv'

map_high(infile1,outfile1)
merge_habitat_motif(infile2,outfile1,infile3,outfile2)