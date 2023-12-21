def specific_multi(infile,outfile1,outfile2):
    out1 = open(outfile1,'wt')
    out7 = open(outfile2,'wt')

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
                    out7.write(f'{smorf}\t{number}\n')
                if specific == 'genus-specific':
                    out7.write(f'{smorf}\t{number}\n')

infile = '90AA_multi_newname.tsv'
outfile1 = 'multi_genus_3.tsv'
outfile2 = 'specific_genus_3.tsv'

specific_multi(infile,outfile1,outfile2)