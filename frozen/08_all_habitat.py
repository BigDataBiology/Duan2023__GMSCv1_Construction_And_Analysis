'''
Generate all level habitat mapping file.
Columns:
100AA smORF accession
90AA smORF accession
50AA smORF accession
Habitat at 100AA
Habitat at 90AA
Habitat at 50AA
'''

def map_habitat(infile1,infile2,infile3,infile4,outfile):
    import lzma
    habitat100 = {}
    habitat90 = {}
    habitat50 = {}
    out = lzma.open(outfile, "wt")
    with lzma.open(infile1,"rt") as f1:
        for line in f1:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) == 2:
                habitat100[linelist[0]] = linelist[1]
            else:
                continue
    with lzma.open(infile2,"rt") as f2:
        for line in f2:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) == 2:
                habitat90[linelist[0]] = linelist[1]
            else:
                continue
    with lzma.open(infile3,"rt") as f3:
        for line in f3:
            line = line.strip()
            linelist = line.split("\t")
            if len(linelist) == 2:
                habitat50[linelist[0]] = linelist[1]
            else:
                continue
    with lzma.open(infile4,"rt") as f4:
        for line in f4:
            line = line.strip()
            linelist = line.split("\t")             
            out.write(line+"\t")
            if len(linelist) == 3:
                if linelist[0] in habitat100.keys():
                    out.write(habitat100[linelist[0]]+"\t")
                else:
                    out.write(""+"\t")
                if linelist[1] in habitat90.keys():
                    out.write(habitat90[linelist[1]]+"\t")
                else:
                    out.write(""+"\t")            
                if linelist[2] in habitat50.keys():
                    out.write(habitat50[linelist[2]]+"\n")
                else:
                    out.write(""+"\n")       
            else:
                out.write(""+"\t")
                if linelist[0] in habitat100.keys():
                    out.write(habitat100[linelist[0]]+"\t")
                else:
                    out.write(""+"\t")
                if linelist[1] in habitat90.keys():
                    out.write(habitat90[linelist[1]]+"\t")
                else:
                    out.write(""+"\t")            
                out.write(""+"\n")                  
    out.close()
       
INPUT_FILE_1 = "/data/frozen/100AA_habitat.tsv.xz"   
INPUT_FILE_2 = "/frozen/90AA_ref_habitat.tsv.xz"
INPUT_FILE_3 = "/frozen/50AA_ref_habitat.tsv.xz"
INPUT_FILE_4 = "/frozen/all_0.9_0.5_family_sort.tsv.xz"
OUTPUT_FILE_1 = "/frozen/all_habitat.tsv.xz" 

map_habitat(INPUT_FILE_1,INPUT_FILE_2,INPUT_FILE_3,INPUT_FILE_4,OUTPUT_FILE_1)