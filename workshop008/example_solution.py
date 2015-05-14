#!/usr/bin/python

'''
(1) as an exercise, take a list of random integers and sort them into ascending
order using your own code
if you cannot think of a way to sort the list into order using python that
you know, do an internet search for "bubble sort algorithm"
the code below gets you started with a list of random unsorted numbers
(2) make a copy of the unsorted list and sort it using the builtin .sort() function
then write code to compare element by element to check that the two lists are identical
(3) run the script several times to check that:
(a) the starting random numbers list produced by the randint function is
different each time and
(b) your sorting method always produces the same order as the built in .sort method
'''

#exercise: sort a list of random integers by swapping elements
import random

#this creates a list of random integers
l1 = [random.randint(0,10) for x in range(100)]

print l1

l2 = l1[:]

def my_sort(l):
    'bubble sort list in place'
    flag = True
    while flag:
        flag = False
        for i in xrange(len(l)-1):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                flag = True

def compare_lists(l1,l2):
    '''
    this is the slow way to compare two lists!
    we only need to do 'assert l1 == l2'
    '''
    if len(l1) != len(l2): return False
    for i in xrange(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True
    

my_sort(l2)
l1.sort()

print l1
print l2

#check the function catches a difference
#l1[3] = -1

print compare_lists(l1,l2)

assert l1 == l2

