#!/usr/bin/python

'''
read through data files from E.coli in various formats

https://github.com/peterjc/biopython_workshop
'''

from Bio import SeqIO

import sys
from os import path

filename = sys.argv[1]

if filename.endswith(".gbk"):
    filetype = "genbank"
else:
    filetype = "fasta"

#read in vesca pseudomolecules as a dictionary name:seqrecord
with open(filename) as f:
    for rec in SeqIO.parse(f,filetype):
        print rec.id,len(rec.seq),len(rec.features)
            #for x in rec.features: print x
