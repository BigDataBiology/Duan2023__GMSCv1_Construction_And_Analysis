'''
Concept:
Map habitat to 90% identity clusters.
Combine multiple habitats for each smORF from the same cluster.
Change habitats to general name.
'''

import gzip
import lzma

def mapcluster(infile1,infile2,outfile):
    habitat = {}
    out = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            smorf,habitat = line.strip().split("\t",1)
            habitat[smorf] = habitat

    with gzip.open(infile2,"rt") as f2:
        for line in f2:
            member,cluster = line.strip().split("\t") 
            out.write(f'{cluster}\t{member}\t{habitat[member]}\n')
    out.close()

def multi_habitat(infile,outfile):
    import lzma

    cluster_dict = {}
    habitat_set = set()
    out  = lzma.open(outfile, "wt")
    
    with lzma.open(infile,"rt") as f1:
        for line in f1:
            cluster,metag,habitat = line.strip().split("\t")
            if cluster_dict:
                if cluster in cluster_dict:
                    cluster_dict[cluster].append(metag)
                    habitatlist = habitat.split(",")
                    for h in habitatlist:
                        habitat_set.add(h)
                else:
                    multihabitat = ",".join(sorted(list(habitat_set)))
                    for key,value in cluster_dict.items():
                        for smorf in value:
                            out.write(f'{key}\t{smorf}\t{multihabitat}\n')
                    cluster_dict = {}
                    habitat_set = set()      
                    cluster_dict[cluster] = [metag]
                    habitatlist = habitat.split(",")
                    for h in habitatlist:
                        habitat_set.add(h)
            else:
                cluster_dict[cluster] = [metag]
                habitatlist = habitat.split(",")
                for h in habitatlist:
                    habitat_set.add(h)
    out.close() 

def general(infile1,infile2,outfile):
    import lzma
    out = lzma.open(outfile,"wt")
    env = {}

    with open(infile1,"rt") as f1:
        for line in f1:
            sample,amp,microontology,name,host,habitat = line.strip().split("\t")
            if host != "":
                fullhabitat = microontology + " # " + host
            else:
                fullhabitat = microontology
            env[fullhabitat] = habitat
        env["isolate"] = "isolate"

    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            smorf_cluster,smorf,multihabitat = line.strip().split("\t")
            multilist = multihabitat.split(",")
            change = set()
            for i in multilist:
                i = i.replace("-"," ")
                change.add(env[i])
            generalhabitat = ",".join(sorted(list(change)))
            out.write(f'{smorf_cluster}\t{smorf}\t{generalhabitat}\n')
            
    out.close()

INPUT_FILE_1 = "GMSC10.100AA.general_habitat.tsv.xz"   
INPUT_FILE_2 = "GMSC.cluster.tsv.gz"
INPUT_FILE_3 = "habitat_general.txt"
OUTPUT_FILE_1 = "cluster_multi_habitat_90.tsv.xz" 
OUTPUT_FILE_2 = "90AA_multi_habitat.tsv.xz"
OUTPUT_FILE_3 = "GMSC10.90AA.general_habitat.tsv.xz"

mapcluster(INPUT_FILE_1,INPUT_FILE_2,OUTPUT_FILE_1)
multi_habitat(OUTPUT_FILE_1,OUTPUT_FILE_2)
general(INPUT_FILE_3,OUTPUT_FILE_2,OUTPUT_FILE_3)