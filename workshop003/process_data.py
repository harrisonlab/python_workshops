#!/usr/bin/python

'''
read in data from a tab-separated-value file
output only a subset of the data to a new file
count number of items output
'''

import sys

#read the input and output filename from the command line
#make sure you get these the right way round, or the script will
#DELETE the input file!!
inputfile = sys.argv[1]
outputfile = sys.argv[2]

#open both files
f = open(inputfile)
fout = open(outputfile,'wb')

#read in just the first line of the input file
header = f.readline()

#write the header to the output file
fout.write(header)

#split header into separate columns
header_cols = header.strip().split('\t')

#find out number of each column
#for offset,value in enumerate(header_cols):
#    print offset,value

counter = 0

for line in f:
    cols = line.strip().split('\t')
    
    #retain only 'PolyHighResolution' data
    if cols[15] == 'PolyHighResolution':
        fout.write(line)
        counter += 1
        
fout.close()
f.close()

print counter
