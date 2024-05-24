'''
Map samples and taxonomy to 90AA smORF families which are multi-phylum and distributed in 8 habitat categories and have more than 100 species.
'''
def store_100(infile1):
    import lzma
    sample_100 = {}
    with lzma.open(infile1,'rt') as f1:
        for line in f1:
            smorf,sample = line.strip().split('\t')
            if smorf not in sample_100.keys():
                sample_100[smorf] = []
            sample_100[smorf].append(sample)
    return sample_100

def map_90(sample_100,infile2,outfile):
    import lzma
    from itertools import chain

    sample_90 = {}
    with lzma.open(infile2,'rt') as f2:
        for line in f2:
            member,cluster = line.strip().split('\t')
            if member in sample_100.keys():
                if cluster not in sample_90.keys():
                    sample_90[cluster] = []
                sample_90[cluster].append(sample_100[member])
    sample_100 = {}
    with open(outfile,'wt') as out:
        for key,value in sample_90.items():
            merge_sample = ','.join(list(set(chain.from_iterable(value))))
            out.write(f'{key}\t{merge_sample}\n')

def map_sample(infile1,infile2,outfile):
    new = set()
    with open(infile1,'rt') as f1:
        for line in f1:
            smorf,number = line.strip().split('\t')
            if number > 100:
                new.add(smorf)

    with open(outfile,'wt') as out:
        with open(infile2,'rt') as f2:
            for line in f2:
                cluster,sample = line.strip().split('\t')
                if cluster in new:
                    out.write(line)

def map_taxonomy(infile1,infile2,outfile):
    import lzma
    seqs = set()

    with open(infile1,'rt') as f:
        for line in f:
            smorf,number = line.strip().split('\t')
            if number > 100:
                seqs.add(smorf)

    with open(outfile,'wt') as out:
        with lzma.open(infile2,'rt') as f:
            for line in f:
                cluster,member,taxonomy = line.strip().split('\t',2)
                if cluster in seqs:
                    out.write(line)

infile1 = '100AA_sample.tsv.xz'
infile2 = 'GMSC.cluster.tsv.gz'
infile3 = 'housekeeping_species.tsv'
infile4 = 'metag_cluster_tax_90.tsv.xz'

outfile1 = '90AA_sample.tsv'
outfile2 = 'housekeeping_sample.txt'
outfile3 = 'housekeeping_taxonomy.txt'

sample_100 = store_100(infile1)
map_90(sample_100,infile2,outfile1)
map_sample(infile3,outfile1,outfile2)
map_taxonomy(infile3,infile4,outfile3)
