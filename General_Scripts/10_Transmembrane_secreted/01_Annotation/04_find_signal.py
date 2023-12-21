'''
Find 90AA families with signalP as true.
'''
def statistic(infile,outfile):
    out = open(outfile,'wt')
    with open(infile,'rt') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                linelist = line.strip().split(' ')
                print(linelist)
                if linelist[18] == 'Y':
                    out.write(line)
    out.close()

def overlap(infile1,infile2,outfile):
    sig_p = set()
    sig_n = set()
    out = open(outfile,'wt')
    with open(infile1,'rt') as f:
        for line in f:
            linelist = line.strip().split(' ')
            sig_p.add(linelist[0])
            out.write(line)
    with open(infile2,'rt') as f:
        for line in f:
            linelist = line.strip().split(' ')
            sig_n.add(linelist[0])
            if linelist[0] not in sig_p:
                out.write(line)
    out.close()

infile1 = '90AA_signalp_gram_positive.tsv'
infile2 = '90AA_signalp_gram_negative.tsv'
outfile1 = '90AA_signalp_gram_positive_true.tsv'
outfile2 = '90AA_signalp_gram_negative_true.tsv'
outfile3 = '90AA_signalp.tsv'

statistic(infile1,outfile1)
statistic(infile2,outfile2)
overlap(outfile1,outfile2,outfile3)