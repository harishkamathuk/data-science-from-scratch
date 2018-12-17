# -*- coding: utf-8 -*-
"""
All the code from the Data Science from Scratch book

Chapter 1. Introduction

"""
# [] = list - mutable
# () = tuple - immutable
# {} = dict - hashes (key - value pairs)
# {} = set - a list with unique values - use key set() or  

from __future__ import division                   # integer division is lame
from collections import Counter
from collections import defaultdict

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

# print(users)

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# print(friendships)

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
print("Connections (v1):", connections)

connections = [(user["id"], number_of_friends(user))
                for user in users]
print("Connections (v2):", connections)

total_connections = sum(number_of_friends(user)                        
                                 for user in users) # 24
print("Total connections: ", total_connections)


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
# double = lambda x: x * 2
# print(double(5)) # Output: 10
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


interests = [    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),    (3, "statistics"), (3, "regression"), (3, "probability"),    (4, "machine learning"), (4, "regression"), (4, "decision trees"),    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),    (6, "probability"), (6, "mathematics"), (6, "theory"),    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),    (9, "Java"), (9, "MapReduce"), (9, "Big Data")]


def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
            
print data_scientists_who_like('Hadoop')            


# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    

print user_ids_by_interest['Java']

# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
print interests_by_user_id[2]


def most_common_interests_with(user):
    return Counter(interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"])
        
print(most_common_interests_with(users[2]))        


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]
                        
# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}                        

print(average_salary_by_tenure)

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
        
# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
print(salary_by_tenure_bucket)    

# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
  tenure_bucket : sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}


print(average_salary_by_bucket)



# 0.7 paid
# 1.9 unpaid
# 2.5 paid
# 4.2 unpaid
# 6   unpaid
# 6.5 unpaid
# 7.5 unpaid
# 8.1 unpaid
# 8.7 paid
# 10  paid

def predict_paid_or_unpaid(years_experience):
  if years_experience < 3.0:
    return "paid"
  elif years_experience < 8.5:
    return "unpaid"
  else:
    return "paid"
    


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
                           
print(words_and_counts)                           

for word, count in words_and_counts.most_common():
    if count > 1:
        print word, count
        
        