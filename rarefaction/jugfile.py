from rarefaction import rarefy
from rarefaction import create_database
import pandas as pd
import os
import shutil
from jug import TaskGenerator

# def parse_args():
#         desc = """Script for rarefaction of 100AA smORFs. Rarefaction can be made for higher level environments or general environment names. """
#         parser = argparse.ArgumentParser(description=desc)

#         parser.add_argument('-n', '--n_perms', help='Number of permutations',
#                                 required=True, dest='n_perms')
#         parser.add_argument('-e', '--env', help='Higher level environment or general environment name',
#                                 choices=['high',
#                                         'general'],
#                                 required=True, dest='env')
#         parser.add_argument('-s', '--samples_dir', help='Directory in which the samples are stored.',
#                                 default='data_samples', dest='samples_dir')
#         parser.add_argument('-hab', '--habitat_data', help='Directory for habitat relationships data with the samples.',
#                         default='data', dest='habitat_data')

#         return parser.parse_args()

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

output_dir = 'rarefaction'
os.makedirs(output_dir, exist_ok=True)

samples_dir = 'data_samples'
habitat_data = 'data'
n_perms = 24
env = 'high'
parallel = True

df = get_samples_relationship(samples_dir, habitat_data)

if env == 'high':
        high_df = higher_env(df)

        high_envs = high_df['high'].unique()

        for high_env in high_envs:
                print(high_env)

                high_df = df[df['high'] == high_env]
                samples_high = list(high_df['sample_accession'])

                name_env = high_env.replace(' ', '_')

                create_database(samples_dir, samples_high, name_env)

                rarefy(name_env, samples_high, n_perms, parallel)
elif env == 'general':
        general_envs = df['general_envo_name'].unique()

        for general_env in general_envs:
                print(general_env)

                general_df = df[df['general_envo_name'] == general_env]
                samples_general = list(general_df['sample_accession'])

                name_env = general_env.replace(' ', '_')

                create_database(samples_dir, samples_general, name_env)

                rarefy(name_env, samples_general, n_perms, parallel)