'''
Concept:
Extract multi-genus and specific-genus families.
'''

def specific_multi(infile,outfile1,outfile2):
    out1 = open(outfile1,'wt')
    out2 = open(outfile2,'wt')

    with open(infile,'rt') as f:
        for line in f:
            smorf,multi,specific,number = line.strip().split('\t')
            if number >2:
                if multi == 'kingdom-multi':
                    out1.write(f'{smorf}\t{number}\n')
                if multi == 'phylum-multi':
                    out1.write(f'{smorf}\t{number}\n')
                if multi == 'class-multi':
                    out1.write(f'{smorf}\t{number}\n')
                if multi == 'order-multi':
                    out1.write(f'{smorf}\t{number}\n')
                if multi == 'family-multi':
                    out1.write(f'{smorf}\t{number}\n')
                if multi == 'genus-multi':
                    out1.write(f'{smorf}\t{number}\n')       

                if specific == 'species-specific':
                    out2.write(f'{smorf}\t{number}\n')
                if specific == 'genus-specific':
                    out2.write(f'{smorf}\t{number}\n')
    out1.close()
    out2.close()

infile = '90AA_taxa_multi_specific.tsv'
outfile1 = 'multi_genus_3.tsv'
outfile2 = 'specific_genus_3.tsv'

specific_multi(infile,outfile1,outfile2)