'''
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

def store(infile):
    import lzma
    name = {}
    with lzma.open(infile,'rt') as f:
        for line in f:
            old,new = line.strip().split('\t')
            name[old] = new
    return name

def select(infile2):
    housekeeping = set()
    with open(infile2,'rt') as f2:
        for line in f2:
            smorf,habitat = line.strip().split('\t')
            housekeeping.add(smorf)
    return housekeeping

def count(name,housekeeping,infile,outfile):
    out = open(outfile,'wt')
    with open(infile,'rt') as f1:
        for line in f1:
            smorf,number = line.strip().split('\t')
            if smorf in name.keys():
                if name[smorf] in housekeeping:
                    out.write(f'{name[smorf]}\t{number}\n')
    out.close()

infile1 = "metag_cluster_tax_90.tsv.xz"
infile2 = '90AA_rename.tsv.xz'
infile3 = 'all_habitat_smorf.tsv'
outfile1 = "metag_cluster_tax_90.tsv"
outfile2 = '90AA_species_number.tsv'
outfile3 = 'housekeeping_species.tsv'

tax_format(infile1,outfile1)
cal_species(outfile1,outfile2)
name = store(infile2)
housekeeping = select(infile3)
count(name,housekeeping,outfile2,outfile3)