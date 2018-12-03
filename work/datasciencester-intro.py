# -*- coding: utf-8 -*-
"""
All the code from the Data Science from Scratch book

Chapter 1. Introduction

"""
# [] = list
# () = tuple
# {} = dict
# ?? = set - a dict with unique values

from __future__ import division                   # integer division is lame
from collections import Counter

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

#print(users)

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

print(friendships)

for user in users:
    user["friends"] = []

    
for i, j in friendships:   
# this works because users[i] is the user whose id is i    
    users[i]["friends"].append(users[j]) # add i as a friend of j    
    users[j]["friends"].append(users[i]) # add j as a friend of i    
    
# print(users)

def number_of_friends(user):    
    """how many friends does _user_ have?"""    
    return len(user["friends"]) # length of friend_ids list

connections = [number_of_friends(user) for user in users]
#print("Connections (v1):", connections)

connections = [(user["id"], number_of_friends(user))
                for user in users]
#print("Connections (v2):", connections)

total_connections = sum(number_of_friends(user)                        
                                 for user in users) # 24
#print("Total connections: ", total_connections)


num_users = len(users)                            # length of the users list
avg_connections = total_connections / num_users   # 2.4

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

#print(num_friends_by_id)

#print(sorted(num_friends_by_id,                                  # get it sorted
#       key = lambda (user_id, num_friends): num_friends,   # by num_friends
#       reverse=True))                                       # largest to smallest

def num_friends(nfbi):
    '''return the number of friends for user'''
    return nfbi[1]
    
print(sorted(num_friends_by_id, # get it sorted
       key = num_friends,       # by num_friends
       reverse=True))           # largest to smallest


## def double(x):
##    return x * 2
## Program to show the use of lambda functions
#double = lambda x: x * 2
#print(double(5)) # Output: 10
#
#
#
## Program to filter out only the even items from a list
#my_list = [1, 5, 4, 6, 8, 11, 3, 12]
#new_list = list(filter(lambda x: (x%2 == 0) , my_list))
#print(new_list) # Output: [4, 6, 8, 12]
#
## take second element for sort
#def takeSecond(elem):
#    print(elem)
#    return elem[1]
#
#random = [(2, 2), (3, 4), (4, 1), (1, 3)] # random list
#
## sortedList = sorted(random)
## sortedList = sorted(random, key=takeSecond) # sort list with key
#sortedList = sorted(random,
#                    key = lambda elem: elem[1]) # sort list with key
#print('Sorted list:', sortedList) # print list


def friends_of_friend_ids_bad(user):
    # foaf is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]       # for each of the user's friend
                for foaf in friend["friends"]]  # get each of _their_ friends
   
# print(friends_of_friend_ids_bad(users[0])) # [0, 2, 3, 0, 1, 3]

  
#print [friend["id"] for friend in users[0]["friends"]]
#print [friend["id"] for friend in users[1]["friends"]]
#print [friend["id"] for friend in users[2]["friends"]]
    
def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in the users["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])
    


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]        # for each of my friends
                   for foaf in friend["friends"]        # count *their* friends
                   if not_the_same(user, foaf)     # who aren't me 
                   and not_friends(user, foaf))         # and aren't my friends
    
#print(friends_of_friend_ids(users[3]))

                    