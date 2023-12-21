'''
Count cog class number an fraction of transmembrane or secreted smORFs with annotation
'''
def store(infile0):
    import gzip
    trans = set()
    with gzip.open(infile0,'rt') as f:
        for line in f:
            trans.add(line.strip())
    return trans

def merge_class(infile):
    seq_cogs = {}
    with open(infile,'rt') as f:
        for line in f:
            if line.startswith('smorf'):
                continue
            else:
                linelist = line.strip().split('\t')
                if len(linelist) == 7:
                    if linelist[0] not in seq_cogs.keys():
                        seq_cogs[linelist[0]] = set()
                    for item in linelist[6]:
                        seq_cogs[linelist[0]].add(item)
    return seq_cogs

def count_class(trans,seq_cogs,outfile):
    cog_class_trans = {}
    cog_class_not = {}
    t = 0
    f = 0
    for key,value in seq_cogs.items():
        if key in trans:
            t += 1
            for item in value:
                if item not in cog_class_trans.keys():
                    cog_class_trans[item] = 0
                cog_class_trans[item] += 1
        else:
            f += 1
            for item in value:
                if item not in cog_class_not.keys():
                    cog_class_not[item] = 0
                cog_class_not[item] += 1

    with open(outfile,'wt') as out:
        out.write(f'cog\ttrans_count\ttrans_all\tnot_trans_count\tnot_trans_all\n')
        for key,value in cog_class_trans.items():
            if key in cog_class_not.keys():
                out.write(f'{key}\t{value}\t{t}\t{cog_class_not[key]}\t{f}\n')
            else:
                out.write(f'{key}\t{value}\t{t}\t0\t{f}\n')
        for key,value in cog_class_not.items():
            if key not in cog_class_trans.keys():
                out.write(f'{key}\t0\t{t}\t{cog_class_not[key]}\t{f}\n')


infile = '90AA_tm_signal.tsv.gz'
infile1 = '0_arc_motif_cog.tsv'
outfile1 = '1_arc_motif_cog_class_count_trans.tsv'
infile2 = '0_bac_motif_cog.tsv'
outfile2 = '1_bac_motif_cog_class_count_trans.tsv'

trans = store(infile)
seq_cogs = merge_class(infile1)
count_class(trans,seq_cogs,outfile1)
seq_cogs = merge_class(infile2)
count_class(trans,seq_cogs,outfile2)