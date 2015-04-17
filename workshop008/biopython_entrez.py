#!/usr/bin/python

'''

'''

from Bio import Entrez
import time

Entrez.email = "robert.vickerstaff@emr.ac.uk"

handle = Entrez.esearch(db="gene", retmax=10, term="Fragaria[Orgn] AND resistance")
record = Entrez.read(handle)

id_list = record['IdList'][:10]
uid = id_list[0]

handle = Entrez.efetch(db="gene", id=uid, retmode="xml")
print handle.read()
    
