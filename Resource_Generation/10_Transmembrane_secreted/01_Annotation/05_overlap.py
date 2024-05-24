'''
Combine TMHMM and SignalP results.
'''
def overlap(infile1,infile2):
    union = set()
    out = open(outfile,'wt')
    with open(infile1,'rt') as f:
        for line in f:
            linelist = line.strip().split('\t')
            union.add(linelist[0])
    with open(infile2,'rt') as f:
        for line in f:
            linelist = line.strip().split(' ')
            union.add(linelist[0])
    for item in sorted(list(union)):
        out.write(f'{item}\n')
    out.close()

infile1 = '90AA_tm_true.tsv'
infile2 = '90AA_signalp.tsv'
outfile = '90AA_tm_signal.tsv'
overlap(infile1,infile2)