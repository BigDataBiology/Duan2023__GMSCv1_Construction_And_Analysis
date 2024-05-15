'''
Concept:
Randomly select 1,000 sequences and map them to the representive sequences of the cluster(>1 member) they are from.
'''

def select(infile,outfile):
    import random
    n = 0
    random.seed(1234)
    random_number = set(random.sample(range(150994369,287926875),1000))
    with open(outfile,'wt') as out:
        with open(infile,'rt') as f:
            for line in f:
                member,cluster = line.strip().split('\t')
                if n in random_number:
                    out.write(f'{member}\t{cluster}\n')
                n += 1

def select_100(infile1,infile2,outfile):
    from fasta import fasta_iter
    smorf = set()
    with open(infile1,'rt') as f:
        for line in f:
            id100,id90 = line.strip().split('\t')
            smorf.add(id100)

    with open(outfile,'wt') as out:
        for h,seq in fasta_iter(infile2):
            if h in smorf:
                out.write(f'>{h}\n{seq}\n')

def select_90(infile1,infile2,outfile):
    from fasta import fasta_iter
    smorf = set()
    with open(infile1,'rt') as f:
        for line in f:
            id100,id90 = line.strip().split('\t')
            smorf.add(id90)

    with open(outfile,'wt') as out:
        for h,seq in fasta_iter(infile2):
            if h in smorf:
                out.write(f'>{h}\n{seq}\n')

clusterfile = 'metag_ProG_nonsingleton_0.9_clu.tsv'
selected_cluster = 'selected_cluster.tsv'
select(clusterfile,selected_cluster)

infile1 = 'selected_cluster.tsv'
infile2 = '100AA_GMSC.faa.xz'
outfile = 'selected_100AA.faa'
select_100(infile1,infile2,outfile)

infile1 = 'selected_cluster.tsv'
infile2 = '90AA_GMSC.faa.xz'
outfile = 'selected_90AA.faa'
select_90(infile1,infile2,outfile)