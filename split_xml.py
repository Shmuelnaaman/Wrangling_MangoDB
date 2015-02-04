#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# 

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    # split the input file into separate files
    # each containing a single patent.
    # each patent declaration starts with the same line that was causing the error
    # The new files saved with filename in the following format:
    # "{}-{}".format(filename, n) where n is a counter, starting from 0.
      n = 0
      with open(filename,'rb') as f1:
          for line in f1:
              if '<?xml version="1.0" encoding="UTF-8"?>' in line:
                  with open("{}-{}".format(filename,n),'wa') as f2:
                        n += 1
                        f2.write(line)
                  
              with open("{}-{}".format(filename,n),'a') as f2:
                  f2.write(line)
             
      pass


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()