#!/usr/bin/python

'''
test gff parsing using biopython
easy_install --upgrade --prefix /home/vicker/python_modules distribute
easy_install --upgrade --prefix /home/vicker/python_modules bcbio-gff
'''

import sys,argparse
from Bio import SeqIO
from BCBio import GFF

ap = argparse.ArgumentParser()
ap.add_argument('--inp_fasta',required=True,type=str,help='input FASTA file')
ap.add_argument('--inp_gff',required=True,nargs='+',type=str,help='input GFF file(s)')
conf = ap.parse_args() #sys.argv

#read in vesca pseudomolecules as a dictionary name:seqrecord
print 'reading pseudomolecules...'
f = open(conf.inp_fasta)
seq_dict = SeqIO.to_dict(SeqIO.parse(f, "fasta"))
f.close()

print 'read in the following sequences:'    
for k,v in seq_dict.iteritems():
    print k,len(v.seq)

#load each GFF, add feature info to seq_dict
gff_list = []
for gff_file in conf.inp_gff:
    print 'reading gff %s...'%gff_file
    f = open(gff_file)
    for rec in GFF.parse(f, base_dict=seq_dict):
        print 'parsed %s'%rec.id
        gff_list.append(rec)
    f.close()

print gff_list
for lg in gff_list:
    print len(lg.features)
    
    for x in lg.features:
        if x.type != 'gene': continue
        print 
        print
        print '  ===>'
        print x
    
