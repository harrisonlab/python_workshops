#!/usr/bin/python

'''
use a function to load two genetic maps
and merge them

usage: merge_maps.py map1 map2 > outputfile
'''

#load the sys module so we can assess command line arguments
import sys

#get the filenames
fname1 = sys.argv[1]
fname2 = sys.argv[2]

#ensure modules can be loaded from the current directory
sys.path.append('.')

#import the load function
from load_function import load_csvr

#load both maps
names1,data1 = load_csvr(fname1)
names2,data2 = load_csvr(fname2)

#check everything looks good
assert names1 == names2

#find maximum lg number in data1
#using a list comprehension
max_lg = max([row[1] for row in data1])

#increment all the lg numbers in data2
for row in data2:
    row[1] += max_lg

#combine both data sets
data_out = data1 + data2

#print file header to stdout
print 'markers,,,' + ','.join(names1)

#print each data row using a list comprehension
for row in data_out:
    full_row = row[0:3] + row[3]
    print ','.join([str(item) for item in full_row])
