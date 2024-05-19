'''
Map Pfam clan.
Count Pfam number.
'''

def select_pfam(infile,outfile):
    with open(outfile,'wt') as out:
        with open(infile,'rt') as f:
            for line in f:
                if line.startswith('smorf'):
                    out.write(line)
                else:
                    linelist = line.strip().split('\t')
                    if len(linelist) > 10 and linelist[10].startswith('pfam'):
                        out.write(line)

# map Pfam clan A
def pfam2clan(in_file1,in_file2,out_file):
    pfam_dict = {}

    with open(in_file1,'rt') as f1:
        for line in f1:
            linelist = line.strip().split('\t')
            pfam = linelist[0].replace('PF','')
            pfam_dict[pfam] = f'{linelist[1]}\t{linelist[2]}\t{linelist[4]}' 

    with open(out_file,'wt') as out:
        out.write(f'smorf\tcdd\tquery_length\tscore\talign_length\tidentity\tevalue\ttarget_length\ttcov\tnumber\taccession\tshort_name\tdescription\tPSSM_Length\tclan_id\tclan\tshort_description\n')
        with open(in_file2,'rt') as f2:
            for line in f2:
                if line.startswith('smorf'):
                    continue
                else:
                    line = line.replace('\n','')
                    linelist = line.split('\t')
                    pf = linelist[10].replace('pfam','')
                    if pf in pfam_dict.keys():
                        out.write(f'{line}\t{pfam_dict[pf]}\n')
                    else:
                        out.write(f'{line}\n')

# map Pfam clan C
def map_clan_c(in_file1,in_file2,out_file):
    pfam_dict = {}

    with open(in_file1,'rt') as f1:
        for line in f1:
            linelist = line.strip().split('\t')
            pfam_dict[linelist[1]] = linelist[2]

    with open(out_file,'wt') as out:
        with open(in_file2,'rt') as f2:
            for line in f2:
                line = line.strip()
                if line.startswith('smorf'):
                    out.write(f'{line}\tclan_description\n')
                else:
                    linelist = line.split('\t')  
                    if len(linelist) == 17 and linelist[-2] in pfam_dict.keys():
                        out.write(f'{line}\t{pfam_dict[linelist[-2]]}\n')
                    else:
                        out.write(f'{line}\n')

# group ribosomal and unknown proteins
def modify(infile,outfile):
    with open(outfile,'wt') as out:
        with open(infile,'rt') as f:
            for line in f:
                line = line.strip()
                if line.startswith('smorf'):
                    out.write(f'group\t{line}\n')
                else:
                    linelist = line.split('\t')
                    if len(linelist) >16:
                        if len(linelist) == 17:
                            if 'ribosomal' in linelist[-1].casefold():
                                out.write(f'Ribosomal protein\t{line}\n')
                            elif 'uncharacterised' in linelist[-1].casefold() or 'unknown' in linelist[-1].casefold():
                                out.write(f'Domain of unknown function\t{line}\n')
                            else:
                                group = linelist[-1].split(',')[0]
                                out.write(f'{group}\t{line}\n')                                
                        else:
                            if 'ribosomal' in linelist[-2].casefold():
                                out.write(f'Ribosomal protein\t{line}\n')
                            else:
                                out.write(f'{linelist[-1]}\t{line}\n')
                    else:
                        out.write(f'\t{line}\n')

def count_pfam(infile,outfile1,outfile2):
    group = {}
    pfam = {}
    all = set()

    pfam_info = {}
    
    out1 = open(outfile1,'wt')
    out2 = open(outfile2,'wt')

    with open(infile,'rt') as f:
        for line in f:
            if line.startswith('group'):
                continue
            else:
                linelist = line.strip().split('\t')
                if linelist[0] not in group.keys():
                    group[linelist[0]] = set()
                group[linelist[0]].add(linelist[1])               
                if linelist[11] not in pfam.keys():
                    pfam[linelist[11]] = set()
                    pfam_info[linelist[11]] = f'{linelist[0]}\t{linelist[12]}\t{linelist[13]}\t{linelist[15]}\t{linelist[16]}\t{linelist[17]}'
                pfam[linelist[11]].add(linelist[1])

                all.add(linelist[1])

    out1.write(f'group\tcount\tall_count\n')
    for key,value in group.items():
        number = len(value)
        all_number = len(all)
        out1.write(f'{key}\t{number}\t{all_number}\n')

    out2.write(f'pfam\tcount\tall_count\tgroup\tshort_name\tdescription\tclan_id\tclan\tshort_description\n')
    for key,value in pfam.items():
        number = len(value)
        all_number = len(all)
        out2.write(f'{key}\t{number}\t{all_number}\t{pfam_info[key]}\n')

    out1.close()
    out2.close()

infile1 = 'multi_genus_3_cdd.tsv'
infile2 = '90AA_multi_habitat_cdd.tsv'
outfile1 = 'multi_genus_3_pfam.tsv'
outfile2 = '90AA_multi_habitat_pfam.tsv'
select_pfam(infile1,outfile1)
select_pfam(infile2,outfile2)

pfama = 'Pfam-A.clans.tsv'
outfile3 = 'multi_genus_3_pfam_clan_A.tsv'
outfile4 = '90AA_multi_habitat_pfam_clan_A.tsv'
pfam2clan(pfama,outfile1,outfile3)
pfam2clan(pfama,outfile2,outfile4)

pfamc = 'pfam-c_format.txt'
outfile5 = 'multi_genus_3_pfam_clan_A_C.tsv'
outfile6 = '90AA_multi_habitat_pfam_clan_A_C.tsv'
map_clan_c(pfamc,outfile5,outfile6)

outfile7 = 'multi_genus_3_pfam_clan_A_C_group.tsv'
outfile8 = '90AA_multi_habitat_pfam_clan_A_C_group.tsv'
modify(outfile7,outfile8)

outfile9 = 'multi_genus_3_pfam_group_count.tsv'
outfile10 = 'multi_genus_3_pfam_count.tsv'
outfile11 = '90AA_multi_habitat_pfam_group_count.tsv'
outfile12 = '90AA_multi_habitat_pfam_count.tsv'
count_pfam(outfile7,outfile9,outfile10)
count_pfam(outfile8,outfile11,outfile12)