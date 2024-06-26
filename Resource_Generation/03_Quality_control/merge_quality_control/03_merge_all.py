def merge(number,n,infile1,infile2,infile3,infile4,infile5,outfile):
    import lzma
    
    antifam = {}
    terminal = {}
    rnacode = {}
    metat = {}
    riboseq = {}
    metap = {}

    with lzma.open(infile1,'rt') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                linelist = line.strip().split('\t')
                antifam[linelist[0]] = linelist[2]
                terminal[linelist[0]] = linelist[5]

    with open(infile2,'rt') as f:
        for line in f:
            cluster,number = line.strip().split('\t')
            rnacode[cluster] = number
    
    with open(infile3,'rt') as f:
        for line in f:
            cluster,number = line.strip().split('\t')
            metat[cluster] = number

    with open(infile4,'rt') as f:
        for line in f:
            cluster,number = line.strip().split('\t')
            riboseq[cluster] = number

    with open(infile5,'rt') as f:
        for line in f:
            cluster,number = line.strip().split('\t')
            metap[cluster] = number

    with open(outfile,'wt') as out:
        out.write(f'AntiFam\tTerminal checking\tRNAcode\tmetaTranscriptome\tRiboseq\tmetaProteome\n')
        for i in range(number):
            nf = f'{i:09}'
            name = f'GMSC10.{n}AA.{nf[:3]}_{nf[3:6]}_{nf[6:9]}'
            out.write(f'{antifam[name]}\t{terminal[name]}\t{rnacode[name]}\t{metat[name]}\t{riboseq[name]}\t{metap[name]}\n')

def hq(infile,outfile,aa):
    with open(outfile,'wt') as out:
        with open(infile,'rt') as f:
            for n, line in enumerate(f):
                if line.startswith('AntiFam'):
                    continue
                else:
                    antifam,terminal,rnacode,metat,riboseq,metap = line.strip().split('\t')
                    if rnacode != 'NA':
                        if (antifam == 'T' and terminal == 'T' and float(rnacode)<0.05) and (int(metat)>1 or int(riboseq)>1 or float(metap) >= 0.5):
                            number = n-1
                            nf = f'{number:09}'
                            name = f'GMSC10.{aa}AA.{nf[:3]}_{nf[3:6]}_{nf[6:9]}'
                            out.write(f'{name}\n')

NUMBER_100 = 964970496
NUMBER_90 = 287926875

infile1 = 'GMSC10.100AA.quality.tsv.xz'
infile2 = '100AA_RNAcode.tsv'
infile3 = '100AA_metaT.tsv'
infile4 = '100AA_RiboSeq.tsv'
infile5 = '100AA_metaP_all.tsv'
outfile1 = 'GMSC10.100AA.quality_test.tsv'
merge(NUMBER_100,100,infile1,infile2,infile3,infile4,infile5,outfile1)

infile1 = 'GMSC10.90AA.quality.tsv.xz'
infile2 = '90AA_RNAcode.tsv'
infile3 = '90AA_metaT.tsv'
infile4 = '90AA_RiboSeq.tsv'
infile5 = '90AA_metaP.tsv'
outfile2 = 'GMSC10.90AA.quality_test.tsv'
merge(NUMBER_90,90,infile1,infile2,infile3,infile4,infile5,outfile2)

outfile3 = 'GMSC10.100AA.high_quality.tsv'
outfile4 = 'GMSC10.90AA.high_quality.tsv'
hq(outfile1,outfile3,100)
hq(outfile2,outfile4,90)