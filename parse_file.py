'''# YHere I read the input DATAFILE line by line, and for the first 10 lines 
# (not including the header) I split each line on "," and then for each line, create
# a dictionary where the key is the header title of the field, and the value is the 
# value of that field in the row.
# The function parse_file returns a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values dose not contain extra whitespace, like spaces or newline 
# characters.'''


import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    ii=0
    with open(datafile, "r") as f:
        for line in f:            
            dat = line.strip().split(",")
            if dat[0] == 'Title':
                 header=dat
            else :
                ii+=1
                if ii<11 :
                     data.append(dict(zip(header, dat)))
           
    print data            
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()