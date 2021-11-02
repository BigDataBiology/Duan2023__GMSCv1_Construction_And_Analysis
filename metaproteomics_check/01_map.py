import os
import sys
import argparse
import pandas as pd
from fasta import fasta_iter
            
def main(argv):
    parser = argparse.ArgumentParser(description="map")

    parser.add_argument('-db', '--database', required=True, action='store',
            help='database', default=None, dest='db')
    parser.add_argument('-query', '--queryAA', required=True, action='store',
            help='query', default=None, dest='query')
    parser.add_argument('-o', '--output', required=True, action='store',
            help='output', default=None, dest='output')
    return parser.parse_args()

def dbmaker(infile):
    dbin = set()
    length = set()
    for ID,seq in fasta_iter(infile):
        if 8 <= len(seq) <= 100:
            if seq[0] == 'M':
                seq = seq[1:]
            if seq[-1] == '*':
                seq = seq[:-1]
            dbin.add(seq)
            length.add(len(seq))
            
    return dbin,min(length),max(length) 

def dbsearch(dbin,query,db_min,db_max):
    outlist = []
    for ID,seq in fasta_iter(query):
        string_list = []
        for i in range(db_min,db_max+1):
            if len(seq) > i:
                for j in range(0,len(seq)-i+1):
                    qstr = seq[j:j+i]
                    if qstr in dbin:
                        string_list.append(qstr)
        if len(string_list) > 0:
            outlist.append([ID,seq,string_list])   
    return outlist
                   
def print_out(outlist, ofile):
    if len(outlist) > 0:
        data = pd.DataFrame(outlist,columns=['seqid','query','string_list'])
        data.to_csv(ofile,sep='\t', header=True,index=None)
        print('Data was processed successfully\n')
    else:
        print('Processed data did not return any hit\n') 
    
if __name__ == '__main__':

    args = main(sys.argv[1:])
    db = args.db
    query = args.query
    output = args.output
    # directory with the metaproteome files
    directory = '/GMSC/metaproteomes/metaproteomes'
    # directory to store the mapped hits
    odirectory = '/GMSC/metaproteomes/map_result_new'
    ofile = db.replace('.fasta', '') + "_" + output + ".tsv"    
    ofile = os.path.join(odirectory,ofile)
    dbin,db_min,db_max = dbmaker(os.path.join(directory, db))
    outlist = dbsearch(dbin,query,db_min,db_max)   
    print_out(outlist,ofile)            