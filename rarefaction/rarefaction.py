import datatable as dt
import numpy as np
from tqdm import tqdm
import concurrent.futures
import random
import os
import shutil
import shelve
from bitarray import bitarray
import time

def run_calculations(db_name, env_results_dir, samples, p):

    print('... Starting permutation {} ...'.format(p))

    start = time.time()

    with shelve.open(db_name) as db:
        samples_db = samples.copy()

        np.random.seed()
        random.shuffle(samples_db)

        N = int(1e9)
        smorfs = bitarray(N)
        smorfs.setall(False)

        with open(env_results_dir + '/perm_{}.tsv'.format(p), 'a') as rarefication_file:
            rarefication_file.write('k\tsmorfs\n')

        for k, sample in enumerate(samples_db):

            for smorf_id in db[sample]:
                smorfs[smorf_id] = True

            with open(env_results_dir + '/perm_{}.tsv'.format(p), 'a') as rarefication_file:
                rarefication_file.write('{}\t{}\n'.format(k + 1, smorfs.count()))
    
    print('... Permutation {} completed in {:.2f} seconds ...'.format(p, time.time() - start))

def create_database(samples_dir, samples, env):
    database_dir = 'database'
    os.makedirs(database_dir, exist_ok=True)

    print('Creating database for {}'.format(env))

    db_name = database_dir + '/smorfs'
    with shelve.open(db_name) as db:
        for sample in tqdm(samples):
            dt_file = dt.fread(samples_dir + '/' + sample, header = None)

            smorfs = set(dt_file.to_list()[0])

            db[sample] = smorfs

    return db_name

def rarefy(db_name, output_dir, environment, samples, n_perms, parallel):

    name_env = environment.replace(' ', '_').replace('/', '-')
    
    L = len(samples)

    print('------------------------------------------------------')

    print('{} samples for {} environment.'.format(L, environment))

    env_results_dir = output_dir + '/' + name_env
    if not os.path.exists(env_results_dir):
        os.mkdir(env_results_dir)
    else:
        shutil.rmtree(env_results_dir)
        os.mkdir(env_results_dir)

    if parallel:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for p in range(n_perms):
                executor.submit(run_calculations, db_name, env_results_dir, samples, p)
    else:
        for p in range(n_perms):
            run_calculations(db_name, env_results_dir, samples, p)