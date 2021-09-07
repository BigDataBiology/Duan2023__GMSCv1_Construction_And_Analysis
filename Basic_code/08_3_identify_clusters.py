'''
Concept:
Identify the clusters which rescued(aligned) singletons belong to according to best e-value.
'''

def identify(infile,outfile):
    nameset = set()
    out = open(outfile, "w")
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in nameset:
                continue
            else:
                nameset.add(linelist[0])
                out.write(linelist[0]+"\t"+linelist[2]+"\n")
    out.close()

for i in range(24):
    INPUT_FILE_1 = "/diamond/analysis/analysis_0.5/sub"+str(i)+".faa.gz.tsv.tmp.3"
    INPUT_FILE_2 = "/diamond/analysis/analysis_0.9/sub"+str(i)+".faa.gz.tsv.tmp.3"
    OUT_FILE_1 = "/diamond/analysis/analysis_0.5/sub"+str(i)+".faa.gz.tsv.tmp.4"
    OUT_FILE_2 = "/diamond/analysis/analysis_0.9/sub"+str(i)+".faa.gz.tsv.tmp.4"
    identify(INPUT_FILE_1,OUT_FILE_1)
    identify(INPUT_FILE_2,OUT_FILE_2)