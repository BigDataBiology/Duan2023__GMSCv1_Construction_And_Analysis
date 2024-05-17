'''
Count the number of each COG class of smORFs with annotation
'''
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

def count_class(seq_cogs,outfile):
    cog_class = {}

    for key,value in seq_cogs.items():
        for item in value:
            if item not in cog_class.keys():
                cog_class[item] = 0
            cog_class[item] += 1

    n = len(seq_cogs)

    with open(outfile,'wt') as out:
        out.write(f'cog\tcount\tpercentage\tall\n')
        for key,value in cog_class.items():
            out.write(f'{key}\t{value}\t{value/n}\t{n}\n')

infile1 = '0_bac_motif_cog.tsv'
outfile1 = '1_bac_motif_cog_class_count.tsv'
infile2 = '0_arc_motif_cog.tsv'
outfile2 = '1_arc_motif_cog_class_count.tsv'
infile3 = '0_bg_motif_cog.tsv'
outfile3 = '1_bg_motif_cog_class_count.tsv'


seq_cogs = merge_class(infile1)
count_class(seq_cogs,outfile1)
seq_cogs = merge_class(infile2)
count_class(seq_cogs,outfile2)
seq_cogs = merge_class(infile3)
count_class(seq_cogs,outfile3)