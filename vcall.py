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
  
    qc = parser.add_argument_group(title='Reads QC options')
    qc.add_argument("--min", default=0,type=int,help='Filter at a minimum reads length. [default:0]')
    qc.add_argument("--max", default=1000000,type=int,help='Filter at a maximum reads length. [default:1000000]')
    qc.add_argument("--n", default=6000,type=int,help='The downsampling numbers of the raw reads. [default:6000] ')
    qc.add_argument("--q",default=10,type=int,help='The cutoff of q-value, the reads with q-value less than the cutoff will be removed. [default:10]') 
    
    aligmengt = parser.add_argument_group(title='Alignment options')
    aligmengt.add_argument("--Q", default=60,type=int,help='Reads mapping quality >= INT. [default:60]')
    aligmengt.add_argument("--spot1", default=16426,type=int,help='The primer start position of circle reference, if line sequence the value need to be set 1.')
    aligmengt.add_argument("--spot2", default=16570,type=int,help='The end position of reference sequence.')
    
    vcall = parser.add_argument_group(title='Varints calling options')
    vcall.add_argument("--depth", default=100,type=int,help='The lowest depth of reads. [default:100]')
    vcall.add_argument("--a1", default=0.75,type=float,help='First allele frequency. [default:0.75]')  # 0.8 0.8 0.98
    vcall.add_argument("--a2", default=0.1,type=float,help='Second allele frequency. [default:0.1]')  # 0.1 0.05 0.025
    vcall.add_argument("--FC", default=25,type=int,help='The fold change value between a1 and a2. [default:25]')  # 6.5 9.5
    vcall.add_argument("--nbase", default=3,type=int,help='The k-mer value, it will be use to generate the motifs of reads. [default:3]')
    vcall.add_argument("--delr", default=0.7,type=float,help='The frequency of deletion. [default:0.7]')
    vcall.add_argument("--bg", default=0.1,type=float,help='The background nosie of the sequencing platform. [default:.0.1]')
    
    args = parser.parse_args()
    tmpdir = args.inputdir
    depth = args.depth
    a1 = args.a1
    a2 = args.a2
    FC = args.FC
    Delr = args.delr
    ref = args.ref
    P = Path(tmpdir)
    homodir = args.homodir
    homofile = args.refname
    homoP = Path(homodir)
    homofilepath = homoP/homofile
    nbase = args.nbase
    min = args.min
    max = args.max
    n = args.n
    Q = args.Q
    q = args.q
    bg = args.bg
    spot1 = args.spot1
    spot2 = args.spot2
    refid = args.refid
    
    Run().VCALL(refid=refid,P=P, ref=ref, a1=a1,a2=0.00, FC=FC, nbase=nbase, n=n, Q=Q, min=15000, max=17000,depth=depth,homoP=homoP,homoF=homofilepath,spot1=2120,spot2=16570,q=q,Delr=Delr,bg=0.05)
