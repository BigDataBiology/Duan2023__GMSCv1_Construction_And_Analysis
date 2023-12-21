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
            linelist = line.strip().split('\t')
            if linelist[1] != '':
                if linelist[0] in sample_100.keys():
                    if linelist[1] not in sample_90.keys():
                        sample_90[linelist[1]] = []
                    sample_90[linelist[1]].append(sample_100[linelist[0]])
    sample_100 = {}
    with open(outfile,'wt') as out:
        for key,value in sample_90.items():
            merge_sample = ','.join(list(set(chain.from_iterable(value))))
            out.write(f'{key}\t{merge_sample}\n')

def map_sample(infile1,infile2,outfile):
    new = set()
    with open(infile1,'rt') as f1:
        for line in f1:
            new.add(line.strip())

    with open(outfile,'wt') as out:
        with open(infile2,'rt') as f2:
            for line in f2:
                linelist = line.strip().split('\t')
                if linelist[0] in new:
                    out.write(line)

def map_taxonomy(infile1,infile2,infile3,outfile):
    import lzma
    new = set()
    old = {}
    with open(infile1,'rt') as f1:
        for line in f1:
            new.add(line.strip())

    with lzma.open(infile2,'rt') as f2:
        for line in f2:
            linelist = line.strip().split('\t')
            if linelist[1] in new:
                old[linelist[0]] = linelist[1]

    with open(outfile,'wt') as out:
        with lzma.open(infile3,'rt') as f3:
            for line in f3:
                line = line.strip()
                linelist = line.split('\t',2)
                if linelist[0] in old:
                    out.write(f'{old[linelist[0]]}\t{line}\n')

infile1 = '100AA_sample.tsv.xz'
infile2 = 'all_0.9_0.5_family_sort.tsv.xz'
infile3 = 'housekeeping.txt'
infile4 = '90AA_rename.tsv.xz'
infile5 = 'metag_cluster_tax_90.tsv.xz'
outfile1 = '90AA_sample.tsv'
outfile2 = 'housekeeping_sample.txt'
outfile3 = 'housekeeping_taxonomy.txt'

sample_100 = store_100(infile1)
map_90(sample_100,infile2,outfile1)
map_sample(infile3,outfile1,outfile2)
map_taxonomy(infile3,infile4,infile5,outfile3)
