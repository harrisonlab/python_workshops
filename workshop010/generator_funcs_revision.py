#simple examples of list and dictionary comprehensions

#input data: integers from 0... 9
l1 = range(10)

#now create a new list containing only the even numbers

#the slow way...
l2 = []
for x in l1:
    if x%2 == 0:
        l2.append(x)
#the equivalent list comprehension
l2 = [x for x in l1 if x%2 == 0]

#now create a dictionary for even numbers storing the string
#representation keyed by the integer value

#the slow way...
d2 = {}
for x in l1:
    if x%2 == 0:
        d2[x] = str(x)
        
#the equivalent dictionary comprehension
#NOTE: only available for python version 2.7 or higher
d2 = {x:str(x) for x in l1 if x%2 == 0}
