#!/usr/bin/python

'''
read in every line from a csv file into a list
calculate the sum of each column
'''

import sys

inp = sys.argv[1]

data = []

f = open(inp)

#read in column headings
header = f.readline().strip().split(',')
for line in f:
    #split into columns
    cols = line.strip().split(',')
    
    #convert data into floats
    for i,val in enumerate(cols):
        cols[i] = float(val)
        
    #append to list of data
    data.append(cols)

f.close()

data[row_number][col_number]

total = [0.0] * len(header)

for row in data:
    for i,val in enumerate(row):
        total[i] += val
        
for i,x in enumerate(total):
    print header[i],total[i],total[i]/len(data)

#calculate the sum of each column and display it
for i,col_name in enumerate(header):
    total = 0.0
    for row in data:
        total += row[i]
        
    print col_name,total,total/len(data)
