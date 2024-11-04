import argparse
from pathlib import Path
from Scripts.run import *

if __name__ == '__main__':
    ######mtDNA##########
    parser = argparse.ArgumentParser()
    general = parser.add_argument_group(title='General options')
    general.add_argument("--inputdir",help='The path of sequencing data, fastq or fasta.')
    general.add_argument("--ref", help='The absolute path of reference.')
    general.add_argument("--homodir", help='Output file of reference homopolymer. ')
    general.add_argument("--refname",help='The name of reference file.')
    general.add_argument("--refid",help='The id of reference sequence.')
    args = parser.parse_args()
    tmpdir = args.inputdir
    P = Path(tmpdir)
    ref = args.ref
    homodir = args.homodir
    homofile = args.refname
    homoP = Path(homodir)
    homofilepath = homoP/homofile
    refid = args.refid
    depth,a1,a2,FC,Delr,nbase,Min,Max,n,Q,q,bg,spot1,spot2 = Run().run()
    Run().VCALL(refid=refid,P=P, ref=ref, a1=a1,a2=a2, FC=FC, nbase=nbase, n=n, Q=Q, min=Min, max=Max,depth=depth,homoP=homoP,homoF=homofilepath,spot1=spot1,spot2=spot2,q=q,Delr=Delr,bg=bg)