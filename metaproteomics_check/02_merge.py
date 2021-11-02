import os
import re
import pandas as pd

def mergeall(folder,ofile):    
    fdict = dict()
    for directory, subdirectories, files in os.walk(folder):
        for file in files: 
            infile = os.path.join(directory, file)
            with open(infile, 'r') as db:   
                for row in db:
                    row = row.strip().split('\t')
                    substring_lst = row[2]
                    for replacement in ['[', ']', "'", ' ']:
                        substring_lst = substring_lst.replace(replacement, '')                                                      
                    substring_lst = substring_lst.split(',')
                    if row[0] == "seqid":
                        continue
                    else:
                        if row[0] in fdict.keys():
                            for element in substring_lst:
                                fdict[row[0]][1].append(element)
                        else:
                            fdict[row[0]] = [row[1], substring_lst]
    ftable = pd.DataFrame.from_dict(fdict).T
    ftable.rename({0: 'Sequence',1: 'List_of_substrings'},axis=1,inplace=True)
    ftable = ftable.reset_index().rename({'index': 'Access'},axis=1)
    ftable.to_csv(ofile,sep='\t',header=True,index=None)

def covcalc(string,substr_lst):        
    n = len(string)
    covarr = [0]*n
    coords = []  
    phred33 = '![#%$&]()*+-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for substr in substr_lst:
        if n >= len(substr):
            startstop = [(a.start(),a.end()) for a in re.finditer(substr,string)]
            for i in startstop:
                coords.append(i)
    if len(coords) > 0:
        for (init, end) in coords:
            for idx in range(init, end):
                covarr[idx] += 1
    coverage = 1 - covarr.count(0) / n
    strqual = ''
    for a in covarr:
        if a <= 56:
            strqual += phred33[a]
        else:
            strqual += phred33[56]
    return coverage, strqual, covarr

def processfile_cov(infile):
    with open(infile, 'rt') as db:
        out = []
        for row in db:
            smorf, seq, substr_lst = row.strip().split('\t')
            for s in ['[',']',"'",' ']:
                substr_lst = substr_lst.replace(s, '')
            substr_lst = substr_lst.split(',')
            if (smorf != 'query') and (seq != 'Sequence'):
                cov, qualstr, _ = covcalc(seq, substr_lst)                     
                cov = round(cov, 1)
                if cov >= 0.5:
                    out.append([smorf, cov, qualstr])
        df = pd.DataFrame(out,columns=['Access','Coverage','QualityString'])
        return df.sort_values('Access')
    
if __name__ == '__main__':
    folder = "/GMSC/metaproteomes/map_result"
    ofile = "/GMSC/metaproteomes/merge_result/merged_output.tsv"
    mergeall(folder,ofile)
    # properly calculating the coverage per peptide
    df = processfile_cov(ofile)
    # saving final results
    df.to_csv('/GMSC/metaproteomes/merge_result/coverage_analysis.tsv',sep='\t', header=True, index=None)