'''
Concept:
Add full ranks for npbs per taxon.
'''
def store_taxid_name(infile1):
    taxid_dict = {}
    with open(infile1,'rt') as f:
        for line in f:
            linelist = line.strip().split('\t',1)
            if len(linelist) == 2:
                name = linelist[1].replace('d__','').replace('p__','').replace('c__','').replace('o__','').replace('f__','').replace('g__','').replace('s__','').replace('\t',';')
                taxid_dict[linelist[0]] = name
    return taxid_dict

def call_full(taxid_dict,infile2,outfile):
    with open(outfile,'wt') as out:
        with open(infile2,'rt') as f:
            for line in f:
                if line.startswith('taxid'):
                    continue
                else:
                    taxid,level,name,nbps = line.strip().split('\t')
                    if taxid in taxid_dict.keys():
                        out.write(f'{taxid}\t{level}\t{taxid_dict[taxid]}\t{nbps}\n')
                    else:
                        if level == 'phylum':
                            out.write(f'{taxid}\t{level}\t;{name}\t{nbps}\n')
                        if level == 'class':
                            out.write(f'{taxid}\t{level}\t;;{name}\t{nbps}\n')
                        if level == 'order':
                            out.write(f'{taxid}\t{level}\t;;;{name}\t{nbps}\n')
                        if level == 'family':
                            out.write(f'{taxid}\t{level}\t;;;;{name}\t{nbps}\n')
                        if level == 'genus':
                            out.write(f'{taxid}\t{level}\t;;;;;{name}\t{nbps}\n')
                        if level == 'species':
                            out.write(f'{taxid}\t{level}\t;;;;;;{name}\t{nbps}\n')

def per_tax(infile,outfile):
    kingdom_number = {}
    phylum_number = {}
    class_number = {}
    order_number = {}
    family_number = {}
    genus_number = {}
    species_number = {}
    
    with open(infile,'rt') as f:
        for line in f:
            taxid,rank,name,nbps = line.strip().split('\t')
            taxalist = name.split(';')
            if len(taxalist) == 1:
                if taxalist[0] != '':
                    if taxalist[0] not in kingdom_number.keys():
                        kingdom_number[taxalist[0]] = int(nbps)
                    else:
                        kingdom_number[taxalist[0]] += int(nbps)
            if len(taxalist) == 2:
                if taxalist[0] != '':
                    if taxalist[0] not in kingdom_number.keys():
                        kingdom_number[taxalist[0]] = int(nbps)
                    else:
                        kingdom_number[taxalist[0]] += int(nbps)
                if taxalist[1] != '':
                    if taxalist[1] not in phylum_number.keys():
                        phylum_number[taxalist[1]] = int(nbps)
                    else:
                        phylum_number[taxalist[1]] += int(nbps)
            if len(taxalist) == 3:
                if taxalist[0] != '':
                    if taxalist[0] not in kingdom_number.keys():
                        kingdom_number[taxalist[0]] = int(nbps)
                    else:
                        kingdom_number[taxalist[0]] += int(nbps)
                if taxalist[1] != '':
                    if taxalist[1] not in phylum_number.keys():
                        phylum_number[taxalist[1]] = int(nbps)
                    else:
                        phylum_number[taxalist[1]] += int(nbps)
                if taxalist[2] != '':
                    if taxalist[2] not in class_number.keys():
                        class_number[taxalist[2]] = int(nbps)
                    else:
                        class_number[taxalist[2]] += int(nbps)
            if len(taxalist) == 4:
                if taxalist[0] != '':
                    if taxalist[0] not in kingdom_number.keys():
                        kingdom_number[taxalist[0]] = int(nbps)
                    else:
                        kingdom_number[taxalist[0]] += int(nbps)
                if taxalist[1] != '':
                    if taxalist[1] not in phylum_number.keys():
                        phylum_number[taxalist[1]] = int(nbps)
                    else:
                        phylum_number[taxalist[1]] += int(nbps)
                if taxalist[2] != '':
                    if taxalist[2] not in class_number.keys():
                        class_number[taxalist[2]] = int(nbps)
                    else:
                        class_number[taxalist[2]] += int(nbps)
                if taxalist[3] != '':
                    if taxalist[3] not in order_number.keys():
                        order_number[taxalist[3]] = int(nbps)
                    else:
                        order_number[taxalist[3]] += int(nbps)
            if len(taxalist) == 5:
                if taxalist[0] != '':
                    if taxalist[0] not in kingdom_number.keys():
                        kingdom_number[taxalist[0]] = int(nbps)
                    else:
                        kingdom_number[taxalist[0]] += int(nbps)
                if taxalist[1] != '':
                    if taxalist[1] not in phylum_number.keys():
                        phylum_number[taxalist[1]] = int(nbps)
                    else:
                        phylum_number[taxalist[1]] += int(nbps)
                if taxalist[2] != '':
                    if taxalist[2] not in class_number.keys():
                        class_number[taxalist[2]] = int(nbps)
                    else:
                        class_number[taxalist[2]] += int(nbps)
                if taxalist[3] != '':
                    if taxalist[3] not in order_number.keys():
                        order_number[taxalist[3]] = int(nbps)
                    else:
                        order_number[taxalist[3]] += int(nbps)
                if taxalist[4] != '':
                    if taxalist[4] not in family_number.keys():
                        family_number[taxalist[4]] = int(nbps)
                    else:
                        family_number[taxalist[4]] += int(nbps)
            if len(taxalist) == 6:
                if taxalist[0] != '':
                    if taxalist[0] not in kingdom_number.keys():
                        kingdom_number[taxalist[0]] = int(nbps)
                    else:
                        kingdom_number[taxalist[0]] += int(nbps)
                if taxalist[1] != '':
                    if taxalist[1] not in phylum_number.keys():
                        phylum_number[taxalist[1]] = int(nbps)
                    else:
                        phylum_number[taxalist[1]] += int(nbps)
                if taxalist[2] != '':
                    if taxalist[2] not in class_number.keys():
                        class_number[taxalist[2]] = int(nbps)
                    else:
                        class_number[taxalist[2]] += int(nbps)
                if taxalist[3] != '':
                    if taxalist[3] not in order_number.keys():
                        order_number[taxalist[3]] = int(nbps)
                    else:
                        order_number[taxalist[3]] += int(nbps)
                if taxalist[4] != '':
                    if taxalist[4] not in family_number.keys():
                        family_number[taxalist[4]] = int(nbps)
                    else:
                        family_number[taxalist[4]] += int(nbps)
                if taxalist[5] != '':
                    if taxalist[5] not in genus_number.keys():
                        genus_number[taxalist[5]] = int(nbps)
                    else:
                        genus_number[taxalist[5]] += int(nbps)
            if len(taxalist) == 7:
                if taxalist[0] != '':
                    if taxalist[0] not in kingdom_number.keys():
                        kingdom_number[taxalist[0]] = int(nbps)
                    else:
                        kingdom_number[taxalist[0]] += int(nbps)
                if taxalist[1] != '':
                    if taxalist[1] not in phylum_number.keys():
                        phylum_number[taxalist[1]] = int(nbps)
                    else:
                        phylum_number[taxalist[1]] += int(nbps)
                if taxalist[2] != '':
                    if taxalist[2] not in class_number.keys():
                        class_number[taxalist[2]] = int(nbps)
                    else:
                        class_number[taxalist[2]] += int(nbps)
                if taxalist[3] != '':
                    if taxalist[3] not in order_number.keys():
                        order_number[taxalist[3]] = int(nbps)
                    else:
                        order_number[taxalist[3]] += int(nbps)
                if taxalist[4] != '':
                    if taxalist[4] not in family_number.keys():
                        family_number[taxalist[4]] = int(nbps)
                    else:
                        family_number[taxalist[4]] += int(nbps)
                if taxalist[5] != '':
                    if taxalist[5] not in genus_number.keys():
                        genus_number[taxalist[5]] = int(nbps)
                    else:
                        genus_number[taxalist[5]] += int(nbps)
                if taxalist[6] != '':
                    if taxalist[6] not in species_number.keys():
                        species_number[taxalist[6]] = int(nbps)
                    else:
                        species_number[taxalist[6]] += int(nbps)

    with open(outfile,'wt') as out:
        for key,value in kingdom_number.items():
            out.write(f'superkingdom\t{key}\t{value}\n')
        for key,value in phylum_number.items():
            out.write(f'phylum\t{key}\t{value}\n')
        for key,value in class_number.items():
            out.write(f'class\t{key}\t{value}\n')
        for key,value in order_number.items():
            out.write(f'order\t{key}\t{value}\n')
        for key,value in family_number.items():
            out.write(f'family\t{key}\t{value}\n')
        for key,value in genus_number.items():
            out.write(f'genus\t{key}\t{value}\n')
        for key,value in species_number.items():
            out.write(f'species\t{key}\t{value}\n')
                     
infile1 = 'taxid_fullname_gtdb.tsv'
infile2 = 'bps-per-taxon.tsv'
outfile1 = 'full_nbp.txt'
outfile2 = 'per_tax_rank.txt'  

taxid_dict = store_taxid_name(infile1)
call_full(taxid_dict,infile2,outfile1)
per_tax(outfile1,outfile2)