import datatable as dt
import numpy as np
from tqdm import tqdm
import concurrent.futures
from random import sample
import os
import shutil
import shelve
import time
from bitarray import bitarray

def run_calculations(k, n_perms):
    smorfs_len = []
    avg_smorfs, std_smorfs = 0, 0

    N = int(1e9)

    with shelve.open('database/smorfs') as db:
        samples_db = list(db.keys())

        if len(samples_db) != k:

            for p in range(n_perms):
                np.random.seed()
            
                random_samples = sample(samples_db, k)

                smorfs = bitarray(N)
                smorfs.setall(False)

                for key in random_samples:
                    for smorf_id in db[key]:
                        smorfs[smorf_id] = True

                smorfs_len.append(smorfs.count())

            avg_smorfs = sum(smorfs_len) / n_perms
            std_smorfs = np.std(smorfs_len, ddof=1)
        else:
            smorfs = bitarray(N)
            smorfs.setall(False)

            for key in samples_db:
                for smorf_id in db[key]:
                    smorfs[smorf_id] = True
        
            avg_smorfs = smorfs.count()

    return (k, avg_smorfs, std_smorfs)

def create_database(samples, env):
    database_dir = 'database'
    if not os.path.exists(database_dir):
        os.mkdir(database_dir)
    else:
        shutil.rmtree(database_dir)
        os.mkdir(database_dir)

    print('Creating database for {}'.format(env))

    with shelve.open(database_dir + '/smorfs') as db:
        for sample in tqdm(samples):
            dt_file = dt.fread('data_samples/' + sample, header = None)

            smorfs = set(dt_file.to_list()[0])

            db[sample] = smorfs

def rarefy(environment, samples, n_perms, parallel):

    name_env = environment.replace(' ', '_')
    
    L = len(samples)

    print('{} samples for {} environment'.format(L, environment))

    with open('rarefaction/{}.tsv'.format(name_env), 'a') as rarefication_file:
        rarefication_file.write('{}\t{}\t{}\t{}\n'.format('samples', 'avg_smorfs', 'std_smorfs', 'time'))

    if parallel:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = []

            start = time.time()

            for k in range(1, L + 1, 10):
                futures.append(executor.submit(run_calculations, k, n_perms))
            for future in tqdm(concurrent.futures.as_completed(futures), total=int(L/10)):
                with open('rarefaction/{}.tsv'.format(name_env), 'a') as rarefication_file:
                    rarefication_file.write('{}\t{}\t{}\t{}\n'.format(future.result()[0], future.result()[1], future.result()[2], time.time() - start))
    else:
        start = time.time()

        for k in tqdm(range(1, L + 1, 10)):
            k, presult, std_result = run_calculations(k, n_perms)
            with open('rarefaction/{}.tsv'.format(name_env), 'a') as rarefication_file:
                rarefication_file.write('{}\t{}\t{}\t{}\n'.format(k, presult, std_result, time.time() - start))