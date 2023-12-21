'''
Make consistency between Progenomes2 taxonomy and GTDB taxonomy
'''
def change(infile1,infile2,outfile1,outfile2):
    import lzma

    fix = {}

    with open(infile1,'rt') as f1:
        for line in f1:
            number,old,fixed = line.strip().split('\t')
            fix[old] = fixed

    with open(outfile2,'wt') as out2:
        with open(outfile1,'wt') as out1:
            with lzma.open(infile2,'rt') as f2:
                for line in f2:
                    linelist = line.strip().split('\t')
                    if len(linelist) >1:
                        if linelist[1] in fix.keys():
                            out1.write(f'{linelist[0]}\t{fix[linelist[1]]}\n')
                            out2.write(f'{linelist[0]}\t{linelist[1]}\t{fix[linelist[1]]}\n')
                        else:
                            out1.write(line)
                    else:
                        out1.write(line)

infile1 = '100AA_tax_change.tsv'
infile2 = '100AA_taxonomy.tsv.xz'
outfile1 = 'GMSC10.100AA.taxonomy.tsv'
outfile2 = '100AA_fixed.tsv'

change(infile1,infile2,outfile1,outfile2)

infile1 = '90AA_tax_change.tsv'
infile2 = '90AA_tax.tsv.xz'
outfile1 = 'GMSC10.90AA.taxonomy.tsv'
outfile2 = '90AA_fixed.tsv'

change(infile1,infile2,outfile1,outfile2)