#!/usr/bin/env python
"""
parse the csv supplied file and extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

the first line of the datafile is neither data entry, nor header. It is a line
describing the data source and the name of the station .

The data returned as a list of lists.

"""
import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        dat = f.readline().split(",")
        a = dat[1].strip('"')
        name = a
        header = f.readline().split(",")
        for line in f:            
            fields = line.split(",")
            data.append(fields )
            pass
    # Do not change the line below
    return (name, data)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)
    #print name
   
    
if __name__ == "__main__":
    test()
    
    
    
    
    
    ##################### ALTERNATIVE
    def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        r = csv.reader(f)
        name = r.next()[1]
        header = r.next()
        data = [row for row in r]

    return (name, data)