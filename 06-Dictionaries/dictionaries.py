#!/usr/bin/env python3

"""
    __author__  : Codelocked
    __date __   : Since September 2023
    __desc__    : Dictionaries
"""

# Dictionaries allow us to work with key-value pair
# In other languages you may heard about hamp-map or associative arrays

"""
Dictionaries
-------------
    - Key-value pairs these are linked values
    - Key is a unique identifier for data where we can find our data
        and value is that data 

    - Real dictionry where we look up for defination of each word we lookup
        
superhero = {
        'batman'        : 'Bruce Wayne',
        'flash'         : 'Berry Allan',
        'superman'      : 'Clark Kent',
        'wonder women'  : 'Diana Prince',
        'cyborg'        : 'Victor Stone'
}

print(superhero)

"""

student = {'name': 'codelocekd', 'age': 1, 'skills': ['python','ML','DS','ExaCC','GCP']}

# print(student)

# print items

# print keys

# print values

# print items

# print dict['key']

# print dict['NOTEXISTED_KEYS']


student_stuff = {1: 'codelocekd', 'age': 1, 'skills': ['python','ML','DS','ExaCC','GCP']}

# print numeric key


# Dictionaries get() method   ->> default return to None

print(student.get('phone', 'Not exists'))

student['phone'] = '91-99999-99999'

print(student.get('phone', 'Not exists'))
