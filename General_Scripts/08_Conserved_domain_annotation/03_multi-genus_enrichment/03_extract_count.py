'''

'''
def extract(infile_1,infile_2,outfile):
    smorf_set = set()

    with open(infile_1,'rt') as f1:
        for line in f1:
            smorf,size = line.strip().split('\t')
            smorf_set.add(smorf)

    with open(outfile,'wt') as out:
        with open(infile_2,'rt') as f2:
            for line in f2:
                linelist = line.strip().split('\t',1)
                if linelist[0] in smorf_set:
                    out.write(line)

def count_multi_cdd(infile):
    all = set()
    cdd = set()
    pfam = set()

    with open(infile,'rt') as f:
        for line in f:
            if line.startswith('smorf'):
                continue
            else:
                linelist = line.strip().split('\t')
                all.add(linelist[0])
                if linelist[1] != '':
                    cdd.add(linelist[0])
                if len(linelist) > 10 and linelist[10].startswith('pfam'):
                    pfam.add(linelist[0])

    cdd_fraction = len(cdd)/len(all)
    pfam_fraction = len(pfam)/len(all)
    print(f'{len(cdd)}\t{len(pfam)}\t{len(all)}\t{cdd_fraction}\t{pfam_fraction}\n')

def count_multi_habitat(infile):
    multi_habitat = 0
    all = 0

    with open(infile,'rt') as f:
        for line in f:
            if line.startswith('smorf'):
                continue
            else:
                habitat_set = set()
                smorf,habitat= line.strip().split('\t')
                habitat_list = habitat.split(',')

                for item in habitat_list:
                    if item !='isolate':
                        habitat_set.add(item)
                all += 1

                if len(habitat_set) > 1:
                    multi_habitat += 1
                
    fraction = multi_habitat/all
    print(f'{multi_habitat}/{all}\t{fraction}')

infile1 = 'whole_3_selected.tsv'
infile2 = '90AA_multi_habitat_cdd.tsv'
outfile1 = 'whole_3_selected_habitat_cdd.tsv'
extract(infile1,infile2,outfile1)

infile3 = '90AA_multi_habitat.tsv'
outfile2 = 'whole_3_selected_habitat.tsv'
extract(infile1,infile3,outfile2)

count_multi_cdd(outfile1)
count_multi_habitat(outfile2)