#how to use a generator function to parse a file
#one record at a time

#the main script has a for loop
#to process each record returned by the parse_file function
for rec in parse_file(fname):
    process record

#this ordinary function implementation
#loads all the data at once into memory
#and then return a list
#which the for main loop will happily iterator through
def parse_file(fname):
    f = open(fname)
    l = []
    for line in f:
        append rec to l
    f.close()
    return l
    
#this generator function implementation
#return each record one at a time
#and does not need them all in memory at once
#and does not need to create a list
#the main for loop will handle this function
#without having to change the main code at all
def parse_file(fname):
    f = open(fname)
    for line in f:
        yield rec
    f.close()

#simple generator function to emulate the xrange(size) function
def myfunc(size):
    i = 0
    while i < size:
        yield i
        i += 1
        
