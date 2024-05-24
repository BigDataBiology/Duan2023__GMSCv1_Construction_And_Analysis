'''
Find 90AA smORF families which are transmembrane
'''
def find_tm(infile,outfile):
    n = 0
    with open(outfile,'wt') as out:
        with open(infile,'rt') as f:
            for line in f:
                id90,_,_,_,tm_hmm,_ = line.strip().split('\t')
                if tm_hmm.split('=')[1] != '0':
                    n += 1
                    out.write(line)
    print(n)

infile = '90AA_tmhmm.tsv'
outfile = '90AA_tm_true.tsv'
find_tm(infile,outfile)