def file_name(file_dir,outfile):
    import os
    out = open(outfile, "w")
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
                            line = line.strip()
                            linelist = line.split("\t")
                            if float(linelist[-1]) < 0.05:
                                filesplit = infile.split(".")
                                name = filesplit[0]+"."+filesplit[1]+"."+filesplit[2]
                                out.write(name+"\n")
                                break
            else:
                break
    out.close()
file_dir = "RNAcode_result/rna"
outfile = "RNAcode_result/filt/result/smORF_0.9_RNAcode.tsv"
file_name(file_dir,outfile)
