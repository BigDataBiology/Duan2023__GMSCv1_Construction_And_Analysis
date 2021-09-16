def getfa(fa):
    '''
    Every sample has separated .fa.gz file containing all the contigs of this sample.
    The function is to store all the contig sequences of each sample.
    '''
    import gzip
    seqdict = {}
    fa_file = "/home1/luispedro/SHARED/sample-contigs/"+fa+"-assembled.fa.gz"
    with gzip.open(fa_file,"rt") as f2:
        for line in f2:
            line = line.strip()
            if line.startswith(">"):
                line = line.strip(">")
                index = line.split(" ")[0]
            else:
                seqdict[index] = line  
    return seqdict

def add_contigdict(contigdict,GMSC,original):
    '''
    Some smORFs are predicted from the same contig,such as k141_13652_1 and k141_13652_2.
    So make dict to store all the smORFs with their information for each contig.
    e.g.
    'k141_13652': [['GMSC10.SMORF.000_034_767_330', 'k141_13652', 51, 182, 1], ['GMSC10.SMORF.000_034_767_331', 'k141_13652', 182, 412, 1]]
    The function is to add the smORF information into contig dict.
    '''
    (contig_number,start,end,flag,other) = original.split(" # ",4)
    contig = contig_number.split("_")[0] + "_" + contig_number.split("_")[1]
    if contig not in contigdict.keys():
        contigdict[contig] = [[GMSC,contig,int(start),int(end),int(flag)]]
    else:
        contigdict[contig].append([GMSC,contig,int(start),int(end),int(flag)])
               
def detect_sequence(sitelist,seq,out):
    '''
    The function is to detect if the smORF sequence is true(near the head of the contig)
    If the sequence of the contig before the smORF has start codon or stop codon,the smORF is False.Otherwise it's True.
    '''
    codon = {"ATG","TAG","TAA","TGA"}
    tf = 1
    (GMSC,contig,start,end,flag) = sitelist
    if flag == 1:
        for i in range(start-1):
            triplet = seq[i:i+3]                   
            if triplet in codon:
                tf = 0
                break
        if tf == 0:
            out.write(GMSC+"\t"+"F"+"\n")
        else:
            out.write(GMSC+"\t"+"T"+"\n")
        tf = 1
    else:
        for i in range(1,len(seq)-end+1):
            triplet = seq[-i:-i-3:-1]
            if triplet in codon:
                tf = 0
                break
        if tf == 0:
            out.write(GMSC+"\t"+"F"+"\n")
        else:
            out.write(GMSC+"\t"+"T"+"\n")
        tf = 1  
        
def detect_contigdict(contigdict,seqdict,out):
    '''
    The function is to detect the contigdict.
    For example,    
    'k141_13652': [['GMSC10.SMORF.000_034_767_330', 'k141_13652', 51, 182, 1], ['GMSC10.SMORF.000_034_767_331', 'k141_13652', 182, 412, 1]]
    Two smORFs are predicted from k141_13652 and their flags are all 1.
    So the second one which site is 182, 412 cannot near the head of contig.It doesn't need to detect and can be skip.
    
    Condition 1:The contigdict only has one smORF,then detect it normally.
    Condition 2:The contigdict has two smORFs,and the flags are 1,then detect the first one.
                The contigdict has two smORFs,and the flags are -1,then detect the second one.
                The contigdict has two smORFs,and the flags are different,then detect both.
    Condition 3:If contigdict has more than two smORFs,smORFs in the middle of contigs must be true.
                So we only need to detect the first one and last one.
                If their flags are 1,then detect the first one.
                If their flags are -1,then detect the last one.
                If their flags are different,then detect both.       
    '''    
    for key,value in contigdict.items():
        if len(value) == 1:
            seq = seqdict[key]
            detect_sequence(value[0],seq,out)
        elif len(value) == 2:
            seq = seqdict[key]
            if value[0][4] == value[1][4]:
                if value[0][4] == 1:
                    detect_sequence(value[0],seq,out)                 
                    out.write(value[1][0]+"\t"+"T"+"\n")
                else:
                    out.write(value[0][0]+"\t"+"T"+"\n")
                    detect_sequence(value[1],seq,out)                                
            else:
                for i in range(len(value)):
                    detect_sequence(value[i],seq,out)                        
        else:
            seq = seqdict[key]
            if value[0][4] == value[-1][4]:         
                if value[0][4] == 1:
                    detect_sequence(value[0],seq,out) 
                    for i in range(1,len(value)):
                        out.write(value[i][0]+"\t"+"T"+"\n")
                else:
                    for i in range(0,len(value)-1):
                        out.write(value[i][0]+"\t"+"T"+"\n")
                    detect_sequence(value[-1],seq,out)                                  
            else:
                detect_sequence(value[0],seq,out)      
                for i in range(1,len(value)-1):
                    out.write(value[i][0]+"\t"+"T"+"\n")   
                detect_sequence(value[-1],seq,out)
    
def coordinate(infile,outfile):   
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
    out = open(outfile, "wt")

    with gzip.open(infile,"rt") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith("#GMSC_id"):
                continue
            else:
                (GMSC,sample,original) = line.split("\t")
                if sample not in sampleset:
                    if contigdict == {}:
                        seqdict = getfa(sample)
                        sampleset.add(sample)
                        add_contigdict(contigdict,GMSC,original)
                    else:
                        detect_contigdict(contigdict,seqdict,out)
                        contigdict = {}
                        add_contigdict(contigdict,GMSC,original)
                        seqdict = getfa(sample)
                        sampleset.add(sample)
                else:   
                    add_contigdict(contigdict,GMSC,original)

        detect_contigdict(contigdict,seqdict,out)                 
    out.close()  
    
infile = "/home1/duanyq/GMSC/coordinate/new/GMSC10.metag_smorfs.rename.txt.gz"  
outfile = "/home1/duanyq/GMSC/coordinate/new/coordinate_result.tsv"
coordinate(infile,outfile)