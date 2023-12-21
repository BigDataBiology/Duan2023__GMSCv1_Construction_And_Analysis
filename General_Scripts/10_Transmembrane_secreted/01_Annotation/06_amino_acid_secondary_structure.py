'''
Calculate amino acid fraction to form secondary_structure.
'''

from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SearchIO, AlignIO
from Bio.Align import AlignInfo
from Bio.pairwise2 import format_alignment
from fasta import fasta_iter

infile = '90AA_GMSC_sort.faa.gz'
outfile = '90AA_secondary.tsv'

with open(outfile,'wt') as out:
    for h,seq in fasta_iter(infile):
        analyzed_seq = ProteinAnalysis(str(seq))
        result = analyzed_seq.secondary_structure_fraction()
        out.write(f'{h}\t{result[0]}\t{result[1]}\t{result[2]}\n')