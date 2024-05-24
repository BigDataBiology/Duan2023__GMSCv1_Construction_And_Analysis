'''
Concept:
Calculate the species number in 90AA families.
'''
def tax_format(infile,outfile):
    import lzma
    with open(outfile,"wt") as out:
        with lzma.open(infile,"rt") as f:
            for line in f:
                linelist = line.strip().split("\t",2)
                if len(linelist) == 3:
                    tax = linelist[2].replace("\t",";")
                    out.write(f'{linelist[0]}\t{tax}\n')
                else:
                    out.write(f'{linelist[0]}\tUnknown\n')

def cal_species(infile,outfile):
    species_number = {}
    with open(infile,'rt') as f:
        for line in f:
            smorf,taxa = line.strip().split('\t')
            if smorf not in species_number.keys():
                species_number[smorf] = set()
            taxalist = taxa.split(';')
            if len(taxalist) == 7:
                species_number[smorf].add(taxalist[6])
    with open(outfile,'wt') as out:
        for key,value in species_number.items():
            out.write(f'{key}\t{len(value)}\n')

def count(infile1,infile2,outfile):
    housekeeping = set()
    with open(infile1,'rt') as f:
        for line in f:
            smorf,habitat = line.strip().split('\t')
            housekeeping.add(smorf)

    with open(outfile,'wt') as out:
        with open(infile2,'rt') as f:
            for line in f:
                smorf,number = line.strip().split('\t')
                if smorf in housekeeping:
                    out.write(f'{smorf}\t{number}\n')

infile1 = "metag_cluster_tax_90.tsv.xz"
infile2 = 'all_habitat_smorf.tsv'
outfile1 = "metag_cluster_tax_90.tsv"
outfile2 = '90AA_species_number.tsv'
outfile3 = 'housekeeping_species.tsv'

tax_format(infile1,outfile1)
cal_species(outfile1,outfile2)
count(infile2,outfile2,outfile3)