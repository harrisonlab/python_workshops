#!/usr/bin/python

'''


https://github.com/peterjc/biopython_workshop
'''

from Bio import SeqIO

import sys
from os import path

filename = sys.argv[1]

filetype = "genbank"

#read in E coli genbank file, there is only one record
rec = SeqIO.read(filename, filetype)

print rec.id,len(rec.seq),len(rec.features)

#get all the genes
genes = [x for x in rec.features if x.type == 'gene']

print 'genes:',len(genes)

#get the sequence of a single gene
for i,gene in enumerate(genes):
    my_sequence = gene.extract(rec.seq)
    print '>gene' + str(i)
    print my_sequence
