#!/usr/bin/python

'''
parse xml blast hits
output hits as genomix DNA sequence rather than translated into protein
'''

from Bio import SeqIO
from Bio.Blast import NCBIXML
import argparse,sys

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument('--inpxml',required=True,type=str,help='blast XML inputfile')
ap.add_argument('--inpfasta',required=True,type=str,help='genomic DNA sequence FASTA')
ap.add_argument('--out',default='STDOUT',type=str,help='genomic sequence of the hits FASTA')
conf = ap.parse_args()

#load hits into a dictionary keyed by scaffold
hit_dict = {}

ct = 0

f = open(conf.inpxml)
for hit in NCBIXML.parse(f):
    for align in hit.alignments:
        uid =  align.hit_def.split()[0]
        ct += 1
        print ct
        for hsp in align.hsps:
            start = hsp.sbjct_start #positions in BLAST coordinate convention
            end = hsp.sbjct_end     #positions in BLAST coordinate convention
            
            if not uid in hit_dict: hit_dict[uid] = []
            if end < start: start,end = end,start
            hit_dict[uid].append( [start,end] )
            ct += 1
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
