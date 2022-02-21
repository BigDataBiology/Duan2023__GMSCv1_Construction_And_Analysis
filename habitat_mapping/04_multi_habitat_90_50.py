'''
Concept:
Each 90AA/50AA cluster can come from different habitats.
Combine multiple habitats for each smORF from the same cluster.
Change habitats to general name.
'''
    
def multi_habitat(infile,outfile):
    import lzma

    cluster_dict = {}
    habitat_set = set()
    out  = lzma.open(outfile, "wt")
    
    with lzma.open(infile,"rt") as f1:
        for line in f1:
            line = line.strip()
            cluster,metag,habitat = line.split("\t")
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
                            out.write(key+"\t"+smorf+"\t"+multihabitat+"\n")
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
            line = line.strip()
            sample,amp,microontology,name,host,habitat = line.split("\t")
            if host != "":
                fullhabitat = microontology + " # " + host
            else:
                fullhabitat = microontology
            env[fullhabitat] = habitat
        env["isolate"] = "isolate"
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            smorf_cluster,smorf,multihabitat = line.split("\t")
            multilist = multihabitat.split(",")
            change = set()
            for i in multilist:
                i = i.replace("-"," ")
                change.add(env[i])
            generalhabitat = ",".join(sorted(list(change)))
            out.write(smorf_cluster+"\t"+smorf+"\t"+generalhabitat+"\n")
            
    out.close()

INPUT_FILE_1 = "/habitat/id90/cluster_multi_habitat_90.tsv.xz"
INPUT_FILE_2 = "/habitat/id50/cluster_multi_habitat_50.tsv.xz"
INPUT_FILE_3 = "habitat_general.txt"
OUTPUT_FILE_1 = "/habitat/id90/90AA_multi_habitat.tsv.xz"
OUTPUT_FILE_2 = "/habitat/id50/50AA_multi_habitat.tsv.xz" 
OUTPUT_FILE_3 = "/habitat/id90/90AA_multi_general_habitat.tsv.xz"
OUTPUT_FILE_4 = "/habitat/id20/50AA_multi_general_habitat.tsv.xz"

multi_habitat(INPUT_FILE_1,OUTPUT_FILE_1)
multi_habitat(INPUT_FILE_2,OUTPUT_FILE_2)
general(INPUT_FILE_3,OUTPUT_FILE_1,OUTPUT_FILE_3)
general(INPUT_FILE_3,OUTPUT_FILE_2,OUTPUT_FILE_4)