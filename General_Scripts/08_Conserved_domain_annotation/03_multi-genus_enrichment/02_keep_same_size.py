def merge():
    import pandas as pd
    multi = pd.read_csv(r'multi_genus_3_habitat_size.tsv',header=None,names=['size','multi_number'],sep='\t')
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

def select_same_size(outfile1,infile2,outfile2):
    import random

    size_dict = {}
    with open(outfile1,'rt') as f1:
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

    with open(outfile2,'wt') as out:
        for key,value in number_dict.items():
            if key in size_dict.keys():
                selected = random.sample(value,int(size_dict[key]))
                for item in selected:
                    out.write(item)

infile1 = 'size_genus_whole_3.csv'
infile2 = 'whole_3.tsv'
outfile1 = 'size_genus_whole_3_compare.tsv'
outfile2 = 'whole_3_selected.tsv'

merge()
compare(infile1,outfile1)
select_same_size(outfile1,infile2,outfile2)