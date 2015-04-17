#!/usr/bin/python

'''
script to count word frequencies
in a text file using a dictionary
'''

import sys

#get the input file name
input_file = sys.argv[1]

#open input file
f = open(input_file)

#create an empty dictionary, could also have used: counts = dict()
counts = {}

#for each line in the file
for line in f:
    #split into "words"
    words = line.strip().split()
    
    #count the word frequencies
    for word in words:
        word = word.lower()
        if not word in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            
f.close()

#sort by frequency and print
word_list = counts.keys()
word_list.sort(key=lambda x:counts[x],reverse=False)
    
for word in word_list:
    print word,counts[word]
