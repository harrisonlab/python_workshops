#define the map loading function
def load_csvr(fname):
    '''
    load csvr style R/qtl map file
    
    return column names and data
    '''
    
    #open the file in default mode (read only)
    f = open(fname)

    #get the first line, containing column headings, split at commas
    header = f.readline().strip().split(',')
    
    #check the header looks like a, R/qtl csvr file
    assert header[0] == 'markers'
    assert header[1] == ''
    assert header[2] == ''
    assert header[3] != ''
    
    #these column heading contain the names of the samples
    names = header[3:]

    #start an empty list to receive the actualy data
    data = []

    #load in marker data one line at a time
    for line in f:
        #split (into "tokens") at commas
        tok = line.strip().split(',')
        
        #change data as appropriate, give meaningful names
        marker = tok[0]
        lg = int(tok[1])
        cm = float(tok[2])
        genotype_calls = tok[3:]
        
        #pull the info together into a list
        #and append to the growing list of lists
        data.append([marker,lg,cm,genotype_calls])
    f.close()
    
    #return the sample names and marker data
    return names,data
