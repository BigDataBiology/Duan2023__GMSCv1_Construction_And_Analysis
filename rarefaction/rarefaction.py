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

def run_calculations(name_env, samples, p):

    print('... Starting permutation {} ...'.format(p))

    start = time.time()

    with shelve.open('database/smorfs') as db:
        samples_db = samples.copy()

        np.random.seed()
        random.shuffle(samples_db)

        N = int(1e9)
        smorfs = bitarray(N)
        smorfs.setall(False)

        with open('rarefaction/{}/perm_{}.tsv'.format(name_env, p), 'a') as rarefication_file:
            rarefication_file.write('k\tsmorfs\n')

        for k, sample in enumerate(samples_db):

            for smorf_id in db[sample]:
                smorfs[smorf_id] = True

            with open('rarefaction/{}/perm_{}.tsv'.format(name_env, p), 'a') as rarefication_file:
                rarefication_file.write('{}\t{}\n'.format(k + 1, smorfs.count()))
    
    print('... Permutation {} completed in {:2f} seconds ...'.format(p, time.time() - start))

def create_database(samples_dir, samples, env):
    database_dir = 'database'
    if not os.path.exists(database_dir):
        os.mkdir(database_dir)

    print('Creating database for {}'.format(env))

    with shelve.open(database_dir + '/smorfs') as db:
        for sample in tqdm(samples):
            dt_file = dt.fread(samples_dir + '/' + sample, header = None)

            smorfs = set(dt_file.to_list()[0])

            db[sample] = smorfs

def rarefy(environment, samples, n_perms, parallel):

    name_env = environment.replace(' ', '_')
    
    L = len(samples)

    print('------------------------------------------------------')

    print('{} samples for {} environment.'.format(L, environment))

    output_dir = 'rarefaction/' + name_env
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    else:
        shutil.rmtree(output_dir)
        os.mkdir(output_dir)

    if parallel:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for p in range(n_perms):
                executor.submit(run_calculations, name_env, samples, p)
    else:
        for p in range(n_perms):
            run_calculations(name_env, samples, p)