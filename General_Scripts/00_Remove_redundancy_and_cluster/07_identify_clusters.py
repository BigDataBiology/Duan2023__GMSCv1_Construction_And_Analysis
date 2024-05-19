'''
Concept:
Identify the clusters which rescued (aligned) singletons mapped based on the best e-value.
'''

def identify(infile,outfile):
    nameset = set()
    with open(outfile,'wt') as out:
        with open (infile) as f:
            for line in f:
                linelist = line.strip().split('\t')
                if linelist[0] in nameset:
                    continue
                else:
                    nameset.add(linelist[0])
                    out.write(f'{linelist[2]}\t{linelist[0]}\n')

for i in range(24):
    INPUT_FILE_1 = "sub"+str(i)+".faa.gz.tsv"
    OUT_FILE_1 = "sub"+str(i)+".faa.gz.tsv.tmp"
    identify(INPUT_FILE_1,OUT_FILE_1)

# Then merge all the tmp subfiles into singleton_0.9.tsv