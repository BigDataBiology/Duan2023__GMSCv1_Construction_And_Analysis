def getfasta(sample,fasta_path):
    '''
    Every sample has separated .fa.gz file containing all the contigs of this sample.
    The function is to store all the contig sequences of each sample.
    '''
    import gzip
    seqdict = {}
    fasta_file = fasta_path+sample+"-assembled.fa.gz"
    header = None
    chunks = []
    with gzip.open(fasta_file, 'rt') as f:
        for line in f:
            if line[0] == '>':
                if header is not None:
                    seqdict[header] = ''.join(chunks)
                line = line[1:].strip()
                if not line:
                    header = ''
                else:
                    header = line.split()[0]
                chunks = []
            else:
                chunks.append(line.strip())
        if header is not None:
            seqdict[header] = ''.join(chunks)
    return seqdict

def add_contigdict(contigdict,GMSC,original):
    '''
    Some smORFs are predicted from the same contig,such as k141_13652_1 and k141_13652_2.
    So make dict to store all the smORFs with their information for each contig.
    e.g.
    'k141_13652': [['GMSC10.SMORF.000_034_767_330', 51, 182, 1], ['GMSC10.SMORF.000_034_767_331', 182, 412, 1]]
    The function is to add the smORF information into contig dict.
    '''
    (contig_number,start,end,flag,other) = original.split(" # ",4)
    contig = contig_number.split("_")[0] + "_" + contig_number.split("_")[1]
    if contig not in contigdict.keys():
        contigdict[contig] = [[GMSC,int(start),int(end),int(flag)]]
    else:
        contigdict[contig].append([GMSC,int(start),int(end),int(flag)])

def complement(seq):
    '''
    Get complement sequence.
    '''
    return seq.translate(str.maketrans('ACGT', 'TGCA'))

def detect_sequence(sitelist,seq,out):
    '''
    The function is to detect if the smORF sequence is true(near the head of the contig)
    If the sequence of the contig before the smORF has stop codon,the smORF is True.Otherwise it's False.
    '''
    codon = {"TAG","TAA","TGA"} #stop codon
    tf = 0 #default is False
    (GMSC,start,end,flag) = sitelist
    if flag == 1:
        for i in range(start-1,2,-3):
            triplet = seq[i-3:i]            
            if triplet in codon: 
                tf = 1
                break
        if tf == 0:
            out.write(GMSC+"\t"+"F"+"\n")
        else:
            out.write(GMSC+"\t"+"T"+"\n")
        tf = 0   
    else:
        seq = complement(seq)
        for i in range(end-1,len(seq)-3,3):
            triplet = seq[i+3:i:-1]
            if triplet in codon:
                tf = 1
                break
        if tf == 0:
            out.write(GMSC+"\t"+"F"+"\n")
        else:
            out.write(GMSC+"\t"+"T"+"\n")
        tf = 0      

def detect_contigdict(contigdict,seqdict,out):
    '''
    The function is to detect the contigdict.
    For example,    
    {'k141_13652': [['GMSC10.SMORF.000_034_767_330', 51, 182, 1], ['GMSC10.SMORF.000_034_767_331', 182, 412, 1]]}
    Although two smORFs are predicted from k141_13652 and their flags are all 1,they may have different in-frame.
    We calculate the result of their start posiontion number % 3 ( 51%3 and 182%3 ).
    If the results are different,we need to check both of them.Otherwise,we only check the first one.
    
    {'k141_3601': [['GMSC10.SMORF.000_036_426_119', 3, 269, -1]], 'k141_1144': [['GMSC10.SMORF.000_036_426_120', 1104, 1292, -1], ['GMSC10.SMORF.000_036_426_121', 1389, 1598, -1]]}
    For the reversed one,it's the same. We calculate the result of their stop posiontion number % 3 ( 1598%3, 1292%3 and 269%3 ).
    If the results are different,we need to check all of them.Otherwise,we only check the last one.
    
    {'k141_1047': [['GMSC10.SMORF.000_035_907_733', 2998, 3189, -1], ['GMSC10.SMORF.000_035_907_734', 5020, 5205, 1], ['GMSC10.SMORF.000_035_907_735', 5248, 5484, 1], ['GMSC10.SMORF.000_035_907_736', 5831, 6100, -1], ['GMSC10.SMORF.000_035_907_737', 10112, 10270, 1]]}
    If smORFs are from both positive and reversed strands.We check 1 and -1 separately. 
    If the flag is 1,we calculate 5020%3=1,5248%3=1,and 10112%3=2,so we only check GMSC10.SMORF.000_035_907_734 and GMSC10.SMORF.000_035_907_737.
    If the flag is -1,we calculate 6100%3=1,3189%3=0,so we check both GMSC10.SMORF.000_035_907_736 and GMSC10.SMORF.000_035_907_733.
    '''
    for key,value in contigdict.items():    
        flagp = set()
        flagr = set()
        seq = seqdict[key]
        for i in range(0,len(value)):
            if value[i][3] == 1:
                if len(flagr) == 3:
                    out.write(value[i][0]+"\t"+"T"+"\n")
                else:                
                    if value[i][1] % 3 not in flagp:
                        flagp.add(value[i][1] % 3)
                        detect_sequence(value[i],seq,out)
                    else:
                        out.write(value[i][0]+"\t"+"T"+"\n")
        for i in range(len(value)-1,-1,-1):
            if value[i][3] == -1:
                if len(flagr) == 3:
                    out.write(value[i][0]+"\t"+"T"+"\n")
                else:
                    if value[i][2] % 3 not in flagr:
                        flagr.add(value[i][2] % 3)
                        detect_sequence(value[i],seq,out)
                    else:
                        out.write(value[i][0]+"\t"+"T"+"\n")            
        
def coordinate(infile,fasta_path,outfile):   
    '''
    The input file is GMSC10.metag_smorfs.rename.txt.xz.
    e.g.
    GMSC10.SMORF.000_034_767_319    Karasov_2018_arabidopsis_NextMet127     k141_11169_1 # 156 # 320 # -1 # ID=5_1;partial=00;start_type=ATG;rbs_motif=None;rbs_spacer=None;gc_cont=0.479
    GMSC10.SMORF.000_034_767_320    Karasov_2018_arabidopsis_NextMet127     k141_0_1 # 4 # 285 # 1 # ID=6_1;partial=00;start_type=ATG;rbs_motif=None;rbs_spacer=None;gc_cont=0.638
    GMSC10.SMORF.000_034_767_321    Karasov_2018_arabidopsis_NextMet127     k141_4964_1 # 20 # 277 # 1 # ID=7_1;partial=00;start_type=TTG;rbs_motif=GGA/GAG/AGG;rbs_spacer=5-10bp;gc_cont=0.426
    
    For each sample,we store contig sequences,create contig dict,and detect contigdict.
    '''
    import gzip
    import lzma
    
    sampleset = set()
    contigdict = {}
    out = gzip.open(outfile,compresslevel=1,mode='wt')

    with lzma.open(infile,"rt") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith("#GMSC_id"):
                continue
            else:
                (GMSC,sample,original) = line.split("\t")
                if sample not in sampleset:
                    if contigdict == {}:
                        seqdict = getfasta(sample,fasta_path)
                        sampleset.add(sample)
                        add_contigdict(contigdict,GMSC,original)
                    else:
                        detect_contigdict(contigdict,seqdict,out)
                        contigdict = {}                   
                        seqdict = getfasta(sample,fasta_path)
                        sampleset.add(sample)
                        add_contigdict(contigdict,GMSC,original)
                else:   
                    add_contigdict(contigdict,GMSC,original)

        detect_contigdict(contigdict,seqdict,out)                 
    out.close()  
    
INPUT_FILE = "GMSC10.metag_smorfs.rename.txt.xz" 
FASTA_PATH = "./contigs/" 
OUTPUT_FILE = "result.tsv.gz"
coordinate(INPUT_FILE,FASTA_PATH,OUTPUT_FILE)
