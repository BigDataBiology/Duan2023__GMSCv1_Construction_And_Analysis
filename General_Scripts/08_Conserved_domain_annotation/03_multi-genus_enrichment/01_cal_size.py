def cal_multi(infile,outfile):
    size = {}
    with open(infile,'rt') as f:
        for line in f:
            smorf,number,anno = line.strip().split('\t')
            if number not in size.keys():
                size[number] = 1
            else:
                size[number] += 1
    with open(outfile,'wt') as out:
        for key,value in size.items():
            out.write(f'{key}\t{value}\n')


def cal_whole(infile,outfile,outfile2):
    size = {}
    with open(outfile2,'wt') as out:
        with open(infile,'rt') as f:
            for line in f:
                linelist = line.strip().split('\t')
                if int(linelist[3]) >=3:
                    out.write(line)
                    if linelist[3] not in size.keys():
                        size[linelist[3]] = 1
                    else:
                        size[linelist[3]] += 1
    with open(outfile,'wt') as out:
        for key,value in size.items():
            out.write(f'{key}\t{value}\n')

infile1 = 'multi_genus_3_habitat.tsv'
outfile1 = 'multi_genus_3_habitat_size.tsv'
cal_multi(infile1,outfile1)

infile2 = '90AA_multi_newname.tsv'
outfile2 = 'whole_3_size.tsv'
outfile3 = 'whole_3.tsv'
cal_whole(infile2,outfile2,outfile3)