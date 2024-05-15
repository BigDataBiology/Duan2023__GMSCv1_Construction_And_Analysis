'''
Concept:
Filter RNAcode results for 100AA,90AA.
'''

def filter(file_dir,outfile):
    import os
    out = open(outfile, "wt")
    for n in range(1,288):
        print("first"+str(n)+"\n")
        first_dir = file_dir+"/first"+str(n)
        for m in range(1,301):
            print("second"+str(m)+"\n")
            second_dir = first_dir+"/second"+str(m)
            if os.listdir(second_dir):
                for infile in os.listdir(second_dir):
                    file_path = second_dir+"/"+infile
                    with open (file_path) as f1:
                        for line in f1 :
                            linelist = line.strip().split("\t")
                            if float(linelist[-1]) < 0.05:
                                filesplit = infile.split(".")
                                name = filesplit[0]+"."+filesplit[1]+"."+filesplit[2]
                                out.write(f'{name}\n')
                                break
            else:
                break
    out.close()

def true_false_100AA_90AA(infile1,infile2,outfile1,outfile2,outfile3):
    out1 = open(outfile1,"wt")
    out2 = open(outfile2,"wt")
    out3 = open(outfile3,"wt")

    true_90AA = set()

    with open(infile1,"rt") as f1:
        for line in f1:
            true_90AA.add(line.strip())
         
    with open(infile2,"rt") as f2:
        for line in f2:
            cluster,member = line.strip().split("\t")
            if cluster in true_90AA:
                out1.write(f'{member}\n')
            else:
                out2.write(f'{member}\n')
                out3.write(f'{cluster}\n')
    out1.close() 
    out2.close()
    out3.close()


INPUT_DIR = "./rnacode"
INPUT_FILE_1 = "GMSC.cluster_filter.tsv"
OUTPUT_FILE_1 = "rnacode_true_90AA.tsv"
OUTPUT_FILE_2 = "rnacode_true_100AA.tsv"
OUTPUT_FILE_3 = "rnacode_false_100AA.tsv"
OUTPUT_FILE_4 = "rnacode_false_90AA.tsv"

filter(INPUT_DIR,OUTPUT_FILE_1)
true_false_100AA_90AA(OUTPUT_FILE_1,INPUT_FILE_1,OUTPUT_FILE_2,OUTPUT_FILE_3,OUTPUT_FILE_4)