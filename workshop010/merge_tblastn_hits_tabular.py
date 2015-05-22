#!/usr/bin/python

'''
read blast hits from tsv file
merge overlapping hits
output hits as genomic DNA sequence (not protein)
'''

from Bio import SeqIO
import argparse,sys
from merge_overlaps_funcs import *

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument('--inptsv',required=True,type=str,help='blast tabular inputfile')
ap.add_argument('--inpfasta',required=True,type=str,help='genomic DNA sequence FASTA')
ap.add_argument('--out',default='STDOUT',type=str,help='genomic sequence of the hits FASTA')
conf = ap.parse_args()

#load hits into a dictionary keyed by scaffold
ct = 0
hit_dict = {}
f = open(conf.inptsv)
for line in f:
    tok = line.strip().split('\t')
    uid = tok[1]
    start = int(tok[8])
    end = int(tok[9])
        
    if not uid in hit_dict: hit_dict[uid] = []
    if end < start: start,end = end,start
    hit_dict[uid].append( [start,end] )
    ct += 1
    #if ct % 1000 == 0: print ct
f.close()

#remove redundancy by merging overlapping hits
for uid in hit_dict:
    #print uid
    hits = hit_dict[uid]
    nhits = len(hits)
    #print nhits, ' ==> ',

    #merge overlapping intervals
    hit_dict[uid] = merge_overlaps(hit_dict[uid])
    #print len(hit_dict[uid])

#open output file
if conf.out == 'STDOUT':
    fout = sys.stdout
else:
    fout = open(conf.out,'wb')

#load sequence into memory, output the associated hits 
for rec in SeqIO.parse(conf.inpfasta, "fasta"):
    uid = rec.id
    #print uid
    
    if not uid in hit_dict: continue

    for hit in hit_dict[uid]:
        start = hit[0]
        end = hit[1]
        seq = rec.seq[start:end]

        fout.write('>%s::%d::%d\n'%(uid,start,end))
        fout.write(str(seq) + '\n')
        
if conf.out != 'STDOUT':
    fout.close()
