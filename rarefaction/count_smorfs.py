import os
import datatable as dt
from tqdm import tqdm
import numpy as np
import pickle
import gzip
from bitarray import bitarray

samples_dir = 'data_samples'
samples = os.listdir(samples_dir)

print('... Counting smORFs for each sample ...')

freq_arr = np.zeros((1000000000), dtype=np.uint16)

for sample in tqdm(samples):
    dt_file = dt.fread(samples_dir + '/' + sample, header = None)
    smorfs = set(dt_file.to_list()[0])

    for smorf_id in smorfs:
        freq_arr[smorf_id] += 1

print('... Saving smORFs more frequent than 1% or 5% ...')

for pct in [0.01, 0.05]:
    N = int(1e9)
    freq_smorfs = bitarray(N)
    freq_smorfs.setall(False)

    for smorf in tqdm(range(N)):
        if (freq_arr[smorf]/len(samples)) >= pct:
            freq_smorfs[smorf] = True

    with gzip.open('freq_smorfs/' + str(pct) + '_smorfs.gz', 'wb') as f: 
        pickle.dump(freq_smorfs, f)

