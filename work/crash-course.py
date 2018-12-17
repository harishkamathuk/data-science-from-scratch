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

for i in (1, 2, 3, 4, 5):

    
    # notice the blank line
    print i


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

y = apply_to_one(lambda x: x + 4) # equals 5
#print y

# lambda argument1, argument2...: expression (returns a single result using argument list)
another_double = lambda x: x * 2 # avoid using lamdas to define functions - use def instead
def yet_another_double(x): return x * 2 # better!


def my_print(message="my default message"):
    print message

my_print("hello")   # prints 'hello'
my_print()          # prints 'my default message'



def subtract(a=0, b=0):
    return a - b

print(subtract(10, 5)) # returns 5
print(subtract(0, 5))  # returns -5
print(subtract(b=5))   # same as previous


single_quoted_string = 'data science' # works
double_quoted_string = "data science" # works

tab_string = "\t"       # represents the tab character
len(tab_string)         # is 1

not_tab_string = r"\t"  # represents the characters '\' and 't'
len(not_tab_string)     # is 2


multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

print(multi_line_string)

try: 
    print 0 / 0
except ZeroDivisionError:
    print("cannot divide by zero")
    
''' List are just like array but they are adrenaline-powered arrays! '''

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

list_length = len(integer_list)     # equals 3
list_sum    = sum(integer_list)     # equals 6

print(list_length, list_sum)

x = range(10)   # is the list [0, 1, ..., 9]
print(x)
zero = x[0]     # equals 0, lists are 0-indexed
print(zero)
one = x[1]      # equals 1
print(one)
nine = x[-1]    # equals 9, 'Pythonic' for last element
print(nine)
eight = x[-2]   # equals 8, 'Pythonic' for next-to-last element
print(eight)
x[0] = -1       # now x is [-1, 1, 2, 3, ..., 9]
print(x)

first_three   = x[:3]               # [-1, 1, 2]
three_to_end = x[3:]                # [3, 4, ..., 9]
one_to_four = x[1:5]                # [1, 2, 3, 4]
last_three = x[-3:]                 # [7, 8, 9]
without_first_and_last = x[1:-1]    # [1, 2, ..., 8]
copy_of_x = x[:]                    # [-1, 1, 2, ..., 9]

print(first_three, three_to_end, one_to_four, last_three, without_first_and_last, copy_of_x)


1 in [1, 2, 3]    # True
0 in [1, 2, 3]    # False

print(1 in [1,2,3])
print(0 in [1,2,3])

x = [1, 2, 3]
print(x)
x.extend([4, 5, 6])     # x is now [1,2,3,4,5,6]
print(x)
x = x + [7, 8, 9]
print(x)

x = [1, 2, 3]
x.append(0)      # x is now [1, 2, 3, 0]
y = x[-1]        # equals 0
z = len(x)       # equals 4

print(x, y, z)

x, y = [1, 2]    # now x is 1, y is 2
print(y)
_, y = [1, 2]    # now x is 1, y is 2
print(y)

'''Tuples are lists’ immutable cousins.'''
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3      # my_list is now [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify a tuple"
    


def sum_and_product(x, y):
    return (x + y),(x * y)

sp = sum_and_product(2, 3)    # equals (5, 6)
s, p = sum_and_product(5, 10) # s is 15, p is 50


print(sp, s, p)

x, y = 1, 2     # now x is 1, y is 2
print(x, y)
x, y = y, x     # Pythonic way to swap variables; now x is 2, y is 1
print(x, y)


''' dictionary, which associates values with keys '''

empty_dict = {}                         # Pythonic
empty_dict2 = dict()                    # less Pythonic
grades = { "Joel" : 80, "Tim" : 95 }    # dictionary literal

print(grades)

joels_grade = grades["Joel"]            # equals 80

print(joels_grade)


try:
    kates_grade = grades["Kate"]
except KeyError:
    print "no grade for Kate!"
    
joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False

print(joel_has_grade, kate_has_grade)

joels_grade = grades.get("Joel", 0)   # equals 80
kates_grade = grades.get("Kate", 0)   # equals 0
no_ones_grade = grades.get("No One")  # default default is None
print(joels_grade, kates_grade, no_ones_grade)

grades["Tim"] = 99                    # replaces the old value
grades["Kate"] = 100                  # adds a third entry
num_students = len(grades)            # equals 3

# print(grades, num_students)


tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# print(tweet)


tweet_keys   = tweet.keys()     # list of keys
tweet_values = tweet.values()   # list of values
tweet_items  = tweet.items()    # list of (key, value) tuples

"user" in tweet_keys            # True, but uses a slow list in
"user" in tweet                 # more Pythonic, uses faster dict in
"joelgrus" in tweet_values      # True

print(tweet_keys, tweet_values, tweet_items)

# tweet = {
#     ["user", 'username'] : "joelgrus",
#     "text" : "Data Science is Awesome",
#     "retweet_count" : 100,
#     "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
# }


# another_tweet = {
#     ["user", "username"] : ["joelgrus", 45],
#     "text" : "Data Science is Awesome",
#     "retweet_count" : 100,
#     "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
# }
# print(another_tweet)

    
yatt = {
    ("user_username", "age") : ("joelgrus", 45),
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

print(yatt)

document = ['This', 'is', 'a', 'test']

# brute force check if the key exists - add one - if it does not exist - create key and initialize counter to 1
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
# “forgiveness is better than permission” 
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1        

# Use get() to handle for missing keys        
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
    
    
# defaultdict - it first adds a value for it using a zero-argument function you provided when you created it.
from collections import defaultdict
word_counts = defaultdict(int)          # int() produces 0
for word in document:    
    word_counts[word] += 1
    
dd_list = defaultdict(list)             # list() produces an empty list
print(dd_list)
dd_list[2].append(1)                    # now dd_list contains {2: [1]}
print(dd_list)

# dd_list_2 = {}
# dd_list_2[2].append(1)

#     dd_list_2[2].append(1)
# KeyError: 2

dd_dict = defaultdict(dict)             # dict() produces an empty dict
print(dd_dict)
dd_dict["Joel"]["City"] = "Seattle"     # { "Joel" : { "City" : Seattle"}}
print(dd_dict)

dd_pair = defaultdict(lambda: [0, 0])
print(dd_pair)
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0,1]}    
print(dd_pair)

from collections import Counter
c = Counter([0, 1, 2, 0])          # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }
print(c)

word_counts = Counter(document)
print(word_counts)

for word, count in word_counts.most_common(10):
    print word, count
    

s = set()
print(s)

s.add(1)       # s is now { 1 }
s.add(2)       # s is now { 1, 2 }
s.add(2)       # s is still { 1, 2 }
x = len(s)     # equals 2
y = 2 in s     # equals True
z = 3 in s     # equals False

print(s, x, y, z)

hundreds_of_other_words = ["This", "is", "a", "test"]
stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list     # False, but have to check every element
stopwords_set = set(stopwords_list)
"zip" in stopwords_set      # very fast to check


item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)                # 6
item_set = set(item_list)                 # {1, 2, 3}
num_distinct_items = len(item_set)        # 3
distinct_item_list = list(item_set)       # [1, 2, 3]

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
    
print(message)

    
x = 3
parity = "even" if x % 2 == 0 else "odd"
print(parity)

x = 0
while x < 10:
    print x, "is less than 10"
    x += 1
    
for x in range(10):
    print x, "is less than 10"
    
    
    
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     # quit the loop entirely
    print x
    
    
one_is_less_than_two = 1 < 2          # equals True
true_equals_false = True == False     # equals False

print(one_is_less_than_two, true_equals_false)


#  None =  NULL
x = None
print x == None    # prints True, but is not Pythonic
print x is None    # prints True, and is Pythonic


def some_function_that_returns_a_string():
    return "Data Science rocks"
    
s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

print(first_char)    

first_char = s and s[0]
print(first_char)

safe_x = x or 0


print(all([True, 1, { 3 }]))  # True
print(all([True, 1, {}]))      # False, {} is falsy
print(any([True, 1, {}]))      # True, True is truthy
print(all([]))                 # True, no falsy elements in the list
print(any([]))                 # False, no truthy elements in the list




#  The Not-So-Basics


x = [4,1,2,3]
y = sorted(x)     # is [1,2,3,4], x is unchanged
x.sort()          # now x is [1,2,3,4]

print(x, y)

# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True)  # is [-4,3,-2,1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
            key=lambda (word, count): count,
            reverse=True)
            
print(wc)            



even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares      = [x * x for x in range(5)]            # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]

print(even_numbers, squares, even_squares)


square_dict = { x : x * x for x in range(5) }  # { 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set  = { x * x for x in [1, -1] }       # { 1 }




item_list = [1, 2, 3, 1, 2, 3]
item_set = {1, 2, 3, 1, 2, 3}
print(item_list, item_set)

zeroes = [0 for _ in even_numbers]      # has the same length as even_numbers

pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0,0) (0,1) ... (9,8), (9,9)
         
# print(pairs)         

increasing_pairs = [(x, y)                       # only pairs with x < y,
                    for x in range(10)           # range(lo, hi) equals
                    for y in range(x + 1, 10)]   # [lo, lo + 1, ..., hi - 1]
                    
print(increasing_pairs)                    




