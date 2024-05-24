# Concept: 
# Filter sequences (<100aa) and remove redundancy.

def filter_dedup(infile,outfile):
    from fasta import fasta_iter
    seqset = set()
    with open(outfile,'wt') as out:
        for header,seq in fasta_iter(infile):
            if len(seq) < 100:
                if seq not in seqset:
                    out.write(f'>{header}\n{seq}\n')
                    seqset.add(seq)

infile1 = 'database.faa'
outfile1 = 'database_dedup.faa'

filter_dedup(infile1,outfile1)