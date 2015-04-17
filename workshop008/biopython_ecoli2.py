#!/usr/bin/python

'''


https://github.com/peterjc/biopython_workshop
'''

import Bio
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

import sys
#from os import path

#get input / output file name from command line
input_file = sys.argv[1]
output_file = sys.argv[2]


#use stdout as output file, i.e. print to screen unless redirected

filetype = "genbank"

#read in E coli genbank file, there is only one record
rec = SeqIO.read(input_file, filetype)

#print rec.id,len(rec.seq),len(rec.features)

#get all the genes using a list comprehension
genes = [x for x in rec.features if x.type == 'gene']

#print 'genes:',len(genes)

fout = open(output_file,"wb")

#get the sequence of a single gene
#for gene in genes:
for i,gene in enumerate(genes):
    uid = gene.qualifiers['gene'][0] + ' ' + str(i)
    #print type(uid)
    desc = ' '.join(gene.qualifiers['db_xref'] + gene.qualifiers['gene_synonym'])
    
    seq = gene.extract(rec.seq)
    
    #create new SeqRecord object
    newrec = Bio.SeqRecord.SeqRecord(seq, id=uid, name=uid, description=desc)

    #write out to file
    SeqIO.write(newrec,fout,"fasta")

fout.close()
