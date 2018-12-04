# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 06:38:04 2018

@author: harish
"""
#for i in [1, 2, 3, 4, 5]:
#    print "i = ", i
#    for j in [1, 2, 3, 4]:
#        print "j = ", j
#        print "i + j =", i + j
#    print "i = ", i
#print("done looping")


long_winded_computation = (1 + 2 + 3 + 4 + 5
                           + 6 + 7 + 8 + 9)
#print long_winded_computation

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_lol = [ [1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]


two_plus_three = 2 + \
                 3
# print two_plus_three

#for i in (1, 2, 3, 4, 5):
#
#    
#    # notice the blank line
#    print i


import re
my_regex = re.compile("[0-9]+", re.I)

import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

#import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

#match = 10
#from re import * # re has a match function
#print match # <function match at 0x0000000003114A58>

#print 5 / 2 # integer division
#from __future__ import division
#print 5 / 2 # fractional division
#print 5 // 2 # integer division after import 

def double(x):
    '''this function multiplies its input by 2'''
    return x * 2

#print double(4)

def apply_to_one(f):
    '''calls the function f with 1 as its argument'''
    return f(1)

my_double = double
x = apply_to_one(my_double)
#print x

y = apply_to_one(lambda x: x + 5)
#print y

# lambda argument1, argument2...: expression (returns a single result using argument list)

another_double = lambda x: x * 2 # avoid
def yet_another_double(x): return x * 2 # better!


