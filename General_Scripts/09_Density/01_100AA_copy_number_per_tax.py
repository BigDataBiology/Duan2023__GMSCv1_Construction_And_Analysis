def store_100(infile):
    import lzma
    name = set()
    with lzma.open(infile,'rt') as f:
        for line in f:
            old,new = line.strip().split('\t')
            name.add(old)
    return name

def cal(infile,name,outfile):
    import lzma
    kingdom = {}
    phylum = {}
    cl = {}
    order = {}
    family = {}
    genus = {}
    species = {}
    with lzma.open(infile,'rt') as f:
        for line in f:
            linelist = line.strip().split('\t',2)
            if linelist[0] in name:
                if int(linelist[1].split('.')[2].replace('_','')) > 34617404:
                    if len(linelist) == 3:
                        rank= linelist[2].split('\t')
                        if len(rank) >= 1:
                            if rank[0] in kingdom.keys():
                                kingdom[rank[0]] += 1
                            else:
                                kingdom[rank[0]] = 1
                        if len(rank) >= 2:
                            if rank[1] in phylum.keys():
                                phylum[rank[1]] += 1
                            else:
                                phylum[rank[1]] = 1
                        if len(rank) >= 3:
                            if rank[2] in cl.keys():
                                cl[rank[2]] += 1
                            else:
                                cl[rank[2]] = 1
                        if len(rank) >= 4:
                            if rank[3] in order.keys():
                                order[rank[3]] += 1
                            else:
                                order[rank[3]] = 1
                        if len(rank) >= 5:
                            if rank[4] in family.keys():
                                family[rank[4]] += 1
                            else:
                                family[rank[4]] = 1
                        if len(rank) >= 6:
                            if rank[5] in genus.keys():
                                genus[rank[5]] += 1
                            else:
                                genus[rank[5]] = 1
                        if len(rank) >= 7:
                            if rank[6] in species.keys():
                                species[rank[6]] += 1
                            else:
                                species[rank[6]] = 1
    name = set()
    with open(outfile,'wt') as out:
        for key,value in kingdom.items():
            out.write(f'{key}\t{value}\n')
        for key,value in phylum.items():
            out.write(f'{key}\t{value}\n')
        for key,value in cl.items():
            out.write(f'{key}\t{value}\n')
        for key,value in order.items():
            out.write(f'{key}\t{value}\n')
        for key,value in family.items():
            out.write(f'{key}\t{value}\n')
        for key,value in genus.items():
            out.write(f'{key}\t{value}\n')
        for key,value in species.items():
            out.write(f'{key}\t{value}\n')

infile1 = '100AA_rename.tsv.xz'
infile2 = 'metag_cluster_taxonomy.tsv.xz'
outfile = 'cpnumber_per_tax.tsv'

name = store_100(infile1)
cal(infile2,name,outfile)