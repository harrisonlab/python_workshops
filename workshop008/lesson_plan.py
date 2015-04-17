'''
boolean logic
binary logic operations
list comprehensions
extracting gene sequences from a genbank file
set exercises
'''

#boolean variable type: True or False
x = True
y = False
type(x)
type(y)

#conversion from other types
bool(0)
bool(1)
bool(2)
bool(0.0)
bool(1.0)
bool("")
bool(" ")
bool("abcd")
bool("0")

#basic boolean logic operators: and, or, not
x and y
x or y
not x
not y and x

#bitwise boolean
#integers are represented as binary numbers in the computer's memory
x = 10
y = 23
bin(x)
bin(y)

#'0b' just means "this is a binary representation", so we can chop it off
bin(x)[2:]
bin(y)[2:]

#format to a fixed width so the columns line up:
print '{:6b}\n{:6b}'.format(x,y)

#bitwise boolean operator: & (and)  | (or)  ^ (xor)
print '{:06b}\n{:06b}\n{:06b}'.format(x,y,x&y)



#list comprehension
list1 = range(10)

#the slow way, find elements >5
list2 = [] #list()
for x in list1:
    if x > 5:
        list2.append(str(x+2))
        
#the fast way
list2 = [x for x in list1 if x > 5]

list2 = [str(x+2) for x in list1 if x > 5]

#exercise: sort a list of random integers by swapping elements
import random
unsorted = [random.randint(0,10) for x in range(100)]
print unsorted
#bubble sort
