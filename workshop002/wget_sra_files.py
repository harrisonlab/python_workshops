#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
download all the Reikou SRA files

PRJDB1445
http://www.ncbi.nlm.nih.gov/bioproject/268159
http://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=268159
sendtofile => accession list => SraAccList.txt
example HTTP download URL
wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/DRR/DRR013/DRR013876/DRR013876.sra
'''

import os

#file listing SRA ids saved from ncbi through browser
inp = 'SraAccList.txt'

f = open(inp)
for line in f:
    uid = line.strip()
    #print uid
    
    id_list = [uid[:3], uid[:6], uid, uid + '.sra']
    
    cmd = 'wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/'
    cmd += '/'.join(id_list)
    
    print cmd
    #os.system(cmd)
f.close()
