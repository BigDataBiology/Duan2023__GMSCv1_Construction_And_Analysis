'''
Concept:
Integrate 90% and 50% result into a .tsv file including 3 columns (name 50%cluster 90%cluster).
Then we can reformat the same result of non-singletons cluster.And merge them into all_0.5_0.9.tsv.gz.
'''

def join(infile1,infile2,outfile):
    tsv50 = {}
    tsv90 = {}    
    out = open(outfile, "w")
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")
            tsv50[linelist[0]] = linelist[1]
            tsv90[linelist[0]] = ""

    with open (infile2) as f2:
        for line in f2 :
            line = line.strip()
            linelist = line.split("\t")
            tsv90[linelist[0]] = linelist[1]
            if linelist[0] in tsv50.keys():
                continue
            else:
                tsv50[linelist[0]] = ""
    for key,value in tsv50.items():
        out.write(key+"\t"+value+"\t"+tsv90[key]+"\n")
    out.close()
    
INPUT_FILE_1 = "/diamond/analysis/analysis_0.5/singleton_0.5.tsv"
INPUT_FILE_2 = "/diamond/analysis/analysis_0.9/singleton_0.9.tsv"
OUT_FILE = "/diamond/analysis/singleton_0.5_0.9.tsv"
join(INPUT_FILE_1,INPUT_FILE_2,OUT_FILE)
