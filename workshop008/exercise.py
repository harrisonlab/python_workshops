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
unsorted = [random.randint(0,10) for x in range(100)]

print unsorted

