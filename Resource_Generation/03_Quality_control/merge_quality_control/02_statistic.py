def statistic(infile,outfile):
    import pandas as pd
    df = pd.read_csv(infile, compression='xz',header=None,sep='\t',na_filter=None,names=['smorf','rnacode','antifam','metap','riboseq','coordinate','metat'])
    rnacode_count=df['rnacode'].value_counts().to_dict()
    antifam_count=df['antifam'].value_counts().to_dict()
    metap_count=df['metap'].value_counts().to_dict()
    riboseq_count=df['riboseq'].value_counts().to_dict()
    coordinate_count=df['coordinate'].value_counts().to_dict()
    metat_count=df['metat'].value_counts().to_dict()
    with open(outfile,"wt") as out:
        out.write(f"Quality test\tPass\tFail\tNot perform\n")
        out.write(f"Terminal checking\t{coordinate_count['T']}\t{coordinate_count['F']}\t{coordinate_count['NA']}\n")
        out.write(f"AntiFam\t{antifam_count['T']}\t{antifam_count['F']}\t0\n")
        out.write(f"RNAcode\t{rnacode_count['T']}\t{rnacode_count['F']}\t{rnacode_count['NA']}\n")
        out.write(f"MetaTranscriptomic\t{metat_count['T']}\t{metat_count['F']}\t0\n")
        out.write(f"Ribo-Seq\t{riboseq_count['T']}\t{riboseq_count['F']}\t0\n")
        out.write(f"MetaProteomic\t{metap_count['T']}\t{metap_count['F']}\t0\n")

INPUT_FILE = "GMSC10.100AA.quality.tsv.xz"
OUTPUT_FILE = "quality_100AA_statistic.tsv"
statistic(INPUT_FILE,OUTPUT_FILE)