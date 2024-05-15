'''
Concept:
Each raw data cluster can come from different habitats.
Combine multiple habitats for each smORF from the same cluster.
Select 100AA smORFs with habitats.
Change habitats to general name.
'''
    
def multi_habitat(infile,outfile):
    import lzma

    cluster_dict = {}
    habitat_set = set()
    out = lzma.open(outfile,"wt")
    
    with lzma.open(infile,"rt") as f1:
        for line in f1:
            cluster,metag,habitat = line.strip().split("\t")
            if cluster_dict:
                if cluster in cluster_dict:
                    cluster_dict[cluster].append(metag)
                    habitat_set.add(habitat)
                else:
                    multihabitat = ",".join(sorted(list(habitat_set)))
                    for key,value in cluster_dict.items():
                        for smorf in value:
                            out.write(f'{key}\t{smorf}\t{multihabitat}\n')
                    cluster_dict = {}
                    habitat_set = set()      
                    cluster_dict[cluster] = [metag]
                    habitat_set.add(habitat)
            else:
                cluster_dict[cluster] = [metag]
                habitat_set.add(habitat)
    out.close()        
            
def extract(infile1,infile2,outfile):
    import lzma
    import gzip
    smorf = set()
    out = lzma.open(outfile, "wt")
    
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            member,cluster = line.strip().split("\t")
            smorf.add(member)
            
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            seq,habitat = line.strip().split("\t")
            if seq in smorf:
                out.write(f'{seq}\t{habitat}\n')
            else:
                continue
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
            smorf,multihabitat = line.strip().split("\t")
            multilist = multihabitat.split(",")
            change = set()
            for i in multilist:
                i = i.replace("-"," ")
                change.add(env[i])
            generalhabitat = ",".join(sorted(list(change)))
            out.write(f'{smorf}\t{generalhabitat}\n')
    out.close()

INPUT_FILE_1 = "metag_cluster_habitat.tsv.xz"
INPUT_FILE_2 = "GMSC.cluster.tsv.gz"
INPUT_FILE_3 = "habitat_general.txt"
OUTPUT_FILE_1 = "all_cluster_multi_habitat.tsv.xz"
OUTPUT_FILE_2 = "100AA_multi_habitat.tsv.xz" 
OUTPUT_FILE_3 = "100AA_multi_general_habitat.tsv.xz"

multi_habitat(INPUT_FILE_1,OUTPUT_FILE_1)
extract(INPUT_FILE_2,OUTPUT_FILE_1,OUTPUT_FILE_2)
general(INPUT_FILE_3,OUTPUT_FILE_2,OUTPUT_FILE_3)