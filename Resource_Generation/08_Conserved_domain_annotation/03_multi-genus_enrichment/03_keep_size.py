'''
Keep the same size for selected clusers from multi-genus and the whole clusters.
'''

def cal_multi(infile,outfile):
    size = {}
    with open(infile,'rt') as f:
        for line in f:
            smorf,number = line.strip().split('\t')
            if number not in size.keys():
                size[number] = 1
            else:
                size[number] += 1
    with open(outfile,'wt') as out:
        for key,value in size.items():
            out.write(f'{key}\t{value}\n')

def cal_whole(infile,outfile1,outfile2):
    size = {}
    with open(outfile1,'wt') as out:
        with open(infile,'rt') as f:
            for line in f:
                linelist = line.strip().split('\t')
                if int(linelist[3]) >=3:
                    out.write(line)
                    if linelist[3] not in size.keys():
                        size[linelist[3]] = 1
                    else:
                        size[linelist[3]] += 1
    with open(outfile2,'wt') as out:
        for key,value in size.items():
            out.write(f'{key}\t{value}\n')

def merge():
    import pandas as pd
    multi = pd.read_csv(r'multi_genus_3_size.tsv',header=None,names=['size','multi_number'],sep='\t')
    whole = pd.read_csv(r'whole_3_size.tsv',header=None,names=['size','whole_number'],sep='\t')
    combine = multi.merge(whole,on='size',how='inner')
    combine.to_csv(r'size_genus_whole_3.csv',index=None)

def compare(infile1,outfile1):
    with open(outfile1,'wt') as out:
        with open(infile1,'rt') as f:
            for line in f:
                if line.startswith('size'):
                    continue
                else:
                    size,multi,specific = line.strip().split(',')
                    number = min(int(multi),int(specific))
                    out.write(f'{size}\t{number}\n')

def select_same_size(infile1,infile2,outfile):
    import random

    size_dict = {}
    with open(infile1,'rt') as f1:
        for line in f1:
            size,n = line.strip().split('\t')
            size_dict[size] = n
    
    number_dict = {}
    with open(infile2,'rt') as f2:
        for line in f2:
            linelist = line.strip().split('\t')
            if linelist[3] not in number_dict.keys():
                number_dict[linelist[3]] = [f'{linelist[0]}\t{linelist[3]}\n']
            else:
                number_dict[linelist[3]].append(f'{linelist[0]}\t{linelist[3]}\n')

    with open(outfile,'wt') as out:
        for key,value in number_dict.items():
            if key in size_dict.keys():
                selected = random.sample(value,int(size_dict[key]))
                for item in selected:
                    out.write(item)

infile1 = 'multi_genus_3.tsv'
outfile1 = 'multi_genus_3_size.tsv'
cal_multi(infile1,outfile1)

infile2 = '90AA_taxa_multi_specific.tsv'
outfile2 = 'whole_3.tsv'
outfile3 = 'whole_3_size.tsv'
cal_whole(infile2,outfile2,outfile3)

outfile4 = 'size_genus_whole_3.csv'
outfile5 = 'size_genus_whole_3_compare.tsv'
outfile6 = 'whole_3_selected.tsv'

merge()
compare(outfile4,outfile5)
select_same_size(outfile5,outfile2,outfile6)