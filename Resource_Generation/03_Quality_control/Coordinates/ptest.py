import unittest
import shutil

shutil.copyfile('01_allcoordinate.py',
                'coordinates.py')

def gen_vals_dicts():
    import gzip
    from Bio import SeqIO
    from coordinates import getfasta
    seqdict = getfasta('MH0058', 'example_files/')
    seqdict_corr = dict()
    for record in SeqIO.parse(gzip.open('example_files/MH0058-assembled.fa.gz', 'rt'),
                              'fasta'):
        seqdict_corr[record.id] = str(record.seq)
        
    seqdict = sorted(seqdict.items())
    seqdict_corr = sorted(seqdict_corr.items())
    return dict(seqdict), dict(seqdict_corr)
    
  
def gen_addvals():
    import lzma
    import pandas as pd
    from coordinates import add_contigdict
    
    file_testing = dict()
    with lzma.open('example_files/test_file.tsv.xz', 'rt') as infile:
        for row in infile:
            (GMSC, sample, other) = row.strip().split('\t')
            add_contigdict(file_testing, GMSC, other)

    file_testing_diff = dict()
    data = pd.read_table('example_files/test_file.tsv.xz', header=None, names=['GMSC', 'sample', 'other'])
    data['contig'] = ['_'.join(x.split(' # ')[0].split('_')[0:2]) for x in data.other]
    data['start'] = [int(x.split(' # ')[1]) for x in data.other]
    data['end'] = [int(x.split(' # ')[2]) for x in data.other]
    data['strand'] = [int(x.split(' # ')[3]) for x in data.other]
    data = data[['GMSC', 'contig', 'start', 'end', 'strand']]
    for chunk in data.groupby('contig'):
        file_testing_diff[chunk[0]] = chunk[1].drop('contig', axis=1).to_dict('split')['data']
    file_testing = sorted(file_testing.items())
    file_testing_diff = sorted(file_testing_diff.items())
    return dict(file_testing), dict(file_testing_diff)


def alt_detect_stop(mainlist, seq, ofile):
    gmsc, start, end, flag = mainlist
    stop_codons = ['TAA', 'TAG', 'TGA']
    if flag == -1:
        seq = seq.translate(str.maketrans('ACGT', 'TGCA'))[::-1]
        start = len(seq) - end
    if flag == 1:
        start -= 1
    state_tf = 0
    for i in range(start, -1, -3):
        if (i-3) >= 0 and seq[i-3: i] in stop_codons:
            state_tf += 1
            break
    if state_tf == 1:
        ofile.write(f'{gmsc}\tT\n')
    if state_tf == 0:
        ofile.write(f'{gmsc}\tF\n')
    state_tf = 0


def stopfindingtest(file_testing_diff, seqdict_corr):
    from coordinates import detect_contigdict
    
    out = open('tmp_orig.txt', 'w')
    detect_contigdict(file_testing_diff,
                      seqdict_corr,
                      out)
    out.close()
        
    out2 = open('tmp_alt.txt', 'w')
    for contig, genelist in file_testing_diff.items():
        seq = seqdict_corr[contig]
        for sitelist in genelist:
            alt_detect_stop(sitelist, seq, out2)            
    out2.close()


class Coordinates_Method_Test(unittest.TestCase):
    
    seqdict, seqdict_corr = gen_vals_dicts()
    ftest, ftest_diff = gen_addvals()        
    
    def test_fasta_reader(self):      
        self.assertDictEqual(self.seqdict, self.seqdict_corr)    

    def test_adding_contigs(self):
        self.assertDictEqual(self.ftest, self.ftest_diff)

    def test_prediction(self):
        from os import remove
        stopfindingtest(self.ftest_diff, self.seqdict_corr)
        with open('tmp_orig.txt', 'r') as tst_path:
            tst_path = tst_path.readlines()
            tst_path = sorted(tst_path)
            with open('tmp_alt.txt', 'r') as ref_path:
                ref_path = ref_path.readlines()
                ref_path = sorted(ref_path)
                self.assertListEqual(tst_path, ref_path)
        remove('tmp_orig.txt')
        remove('tmp_alt.txt')
        remove('coordinates.py')

              
if __name__ == '__main__':
    unittest.main()

    
