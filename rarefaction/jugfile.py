from rarefaction import rarefy
from rarefaction import create_database
import pandas as pd
import os
from jug import TaskGenerator

def get_samples_relationship(samples_dir, habitat_data):

        data_general = pd.read_table(habitat_data + '/general_envo_names.tsv', sep='\t')

        data_metadata = pd.read_table(habitat_data + '/metadata.tsv', sep='\t')

        df = pd.merge(data_metadata, data_general, on=['microontology', 'host_scientific_name'])
        df = df[['general_envo_name', 'host_scientific_name', 'microontology', 'sample_accession']]

        data_samples = os.listdir(samples_dir)
        df = df[df['sample_accession'].isin(data_samples)]
        df = df.drop_duplicates()

        return df

def higher_env(df):

        higher_level = {
                'sediment' : 'other',
                'bird gut' : 'other animal',
                'cat gut' : 'mammal gut',
                'insect associated' : 'other animal',
                'human urogenital tract' : 'other human',
                'dog gut' : 'mammal gut',
                'fermented food' : 'anthropogenic',
                'groundwater' : 'aquatic',
                'coral associated' : 'other animal',
                'turtle gut' : 'other animal',
                'rat gut' : 'mammal gut',
                'human associated' : 'other human',
                'cattle gut' : 'mammal gut',
                'deer gut' : 'mammal gut',
                'whale gut' : 'mammal gut',
                'mouse gut' : 'mammal gut',
                'river associated' : 'aquatic',
                'primate gut' : 'mammal gut',
                'human respiratory tract' : 'other human',
                'cattle rumen' : 'other animal',
                'human saliva' : 'other human',
                'activated sludge' : 'anthropogenic',
                'lake associated' : 'aquatic',
                'wastewater' : 'anthropogenic',
                'chicken gut' : 'other animal',
                'air' : 'other',
                'human mouth' : 'other human',
                'plant associated' : 'soil/plant',
                'water associated' : 'aquatic',
                'pig gut' : 'mammal gut',
                'human skin' : 'other human',
                'marine' : 'aquatic',
                'soil' : 'soil/plant',
                'built environment' : 'anthropogenic',
                'human gut' : 'human gut',
                'anthropogenic': 'anthropogenic',
                'bear gut' : 'mammal gut',
                'rabbit gut': 'mammal gut',
                'dolphin gut': 'mammal gut',
                'algae associated': 'other',
                'crustacean gut': 'other animal',
                'cattle associated': 'other animal',
                'bird skin': 'other animal',
                'bee gut': 'other animal',
                'mussel associated': 'other animal',
                'fisher gut': 'mammal gut',
                'bat gut': 'mammal gut',
                'sponge associated': 'other animal',
                'human digestive tract': 'other human',
                'beatle gut': 'other animal',
                'dog associated': 'other animal',
                'insect gut': 'other animal',
                'extreme pH': 'other',
                'food': 'other',
                'guinea pig gut': 'mammal gut',
                'goat rumen': 'other animal',
                'mollusc associated': 'other animal',
                'goat gut': 'mammal gut',
                'horse gut': 'mammal gut',
                'wasp gut': 'other animal',
                'tunicate associated': 'other animal',
                'annelidae associated': 'other animal',
                'rodent gut': 'mammal gut',
                'ship worm associated': 'other animal',
                'coyote gut': 'mammal gut',
                'crustacean associated': 'other animal',
                'termite gut': 'other animal',
                'planarian associated': 'other animal',
                'thermal vent associated': 'other',
                'fish gut': 'other animal',
                'ice associated': 'other',
                'mock community': 'other',
                'mine': 'other',
                'pond associated': 'aquatic',
                'hot spring associated': 'other',
                }

        df['high'] = [higher_level[x] for x in df['general_envo_name']]
        df = df.drop_duplicates(subset = ['sample_accession', 'high'])

        return df

rarefy = TaskGenerator(rarefy)
create_database = TaskGenerator(create_database)

samples_dir = 'data_samples'
habitat_data = 'data'
n_perms = 24
env = 'high'
parallel = True

select = False
selected = ['human gut']

output_dir = 'rarefaction_results'
output_dir = output_dir + '/' + env
os.makedirs(output_dir, exist_ok=True)

df = get_samples_relationship(samples_dir, habitat_data)

if env == 'high':
        high_df = higher_env(df)

        if select:
                high_envs = selected
        else:
                high_envs = high_df['high'].unique()

        for high_env in high_envs:
                print(high_env)

                high_df = df[df['high'] == high_env]
                samples_high = list(high_df['sample_accession'])

                db_name = create_database(samples_dir, samples_high, high_env)

                rarefy(db_name, output_dir, high_env, samples_high, n_perms, parallel)
elif env == 'general':
        env_threshold = df.groupby('general_envo_name')['sample_accession'].count().sort_values(ascending=False)
        
        if select:
                general_envs = selected
        else:
                general_envs = list(env_threshold[:10].index) # Consider the top 10 environments with most samples

        for general_env in general_envs:
                print(general_env)

                general_df = df[df['general_envo_name'] == general_env]
                samples_general = list(general_df['sample_accession'])

                db_name = create_database(samples_dir, samples_general, general_env)

                rarefy(db_name, output_dir, general_env, samples_general, n_perms, parallel)