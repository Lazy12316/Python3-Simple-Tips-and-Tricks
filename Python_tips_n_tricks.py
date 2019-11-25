# Date:19-Nov-2019

"""
# Different ways to test multiple flags at once in python

x,y,z = 0,1,0

# Method-1
if x==1 or y==1 or z==1:
	print("Passed-Method1")

# Method-2
if 1 in (x,y,z):
	print("Passed-Method2")

# Method-3
if any((x,y,z)):
	print("passed-Method3")


"""
#Trick-2	
"""
# How to sort a python dictionary by value (== get a representation sorted by value)

# Method-1
xs = {'a':4,'b':3,'c':2,'d':1}

print("Method - 1")
print(sorted(xs.items(), key = lambda x : x[1]))


print("Method - 2")
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))

"""

#Date:20-Nov-2019
#Trick-3
"""
# Using get() to return a default value from a pthon dict

# Python dictionaries have a "get" Method to lookup a key while providing a fallback value. 
# https://dbader.org/blog/python-dict-get-default-value 



# Consider the following dictionary. If a know key is passed, the method greeting will return string HI "userid". 
# if key is invalid, the method will throw key error.

name_for_userid = {382:"Alice", 950:"Bob", 590:"Dilbert"}
def greeting(userid):
	return "Hi %s!" % name_for_userid[userid]
	

def greeting_2(userid):
	return "Hi %s!" % name_for_userid.get(userid, "Key Invalid")
	
print(greeting(382))
print(greeting_2(950))
print(greeting_2(39999990))
print(greeting(4000)) # Throws key error
"""

#Trick-4
"""
# Python's Namedtuples can be a great alternative to defining a class manually.

# namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries. 
# Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. 
# The arguments are the name of the new class and a string containing the names of the elements.

# Method: namedtuple
# Syntax: namedtuple('','[param1, param2, param3, ....]')
# Library: collections
# https://www.geeksforgeeks.org/namedtuple-in-python/
# https://pymotw.com/2/collections/namedtuple.html


from collections import namedtuple

Car = namedtuple('Car', 'color mileage year speed')

# Out new "Car" class works as below
my_car = Car('red', 3812.4, 1984, 45)
print(my_car.color)
print(my_car.mileage)
print(my_car.year)
print(my_car.speed)

print(my_car)

# namedtuple is immutable

"""

#Date:21-Nov-2019
#Trick-5
"""
# Method: Timeit Module
# Library: Timeit
# Syntax: timeit.timeit(stmt, setup, timer, number)
# * stmt - The statement whose time execution you want to measure
# * setup - which is the code that you run before running the stmt; it defaults to ‘pass’.
# * timer - timer object of timeit.Timer(). It has default value.
# * number - Number of iterations you want to run the statement through

# The "timeit" module lets you measure the execution
# time of small bits of Python code


 
import timeit

# Example - 1

t = timeit.timeit('"-".join(str(n) for n in range(100))',
                  number=10000)

print(t)

# Example - 2

# binary search function 
def binary_search(mylist, find): 
    while len(mylist) > 0: 
        mid = (len(mylist))//2
        if mylist[mid] == find: 
            return True
        elif mylist[mid] < find: 
            mylist = mylist[:mid] 
        else: 
            mylist = mylist[mid + 1:] 
    return False

# compute binary search time 
def binary_time(): 
    SETUP_CODE = ''' 
from __main__ import binary_search 
from random import randint'''
  
    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
binary_search(mylist, find)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('Binary search time: {}'.format(min(times)))

binary_time()

"""

#Trick - 6

"""
# In-place value swapping


# Let's say we want to swap
# the values of a and b...
a = 23
b = 42

# The "classic" way to do it
# with a temporary variable:
# tmp = a
# a = b
# b = tmp

# Python also lets us
# use this short-hand:
a, b = b, a

print(a, b)

"""
# Date:22-Nov-2019
# Trick - 7

"""

# "is" vs "=="

a = [1, 2, 3]
b = a

print(a is b)

print(a == b)

c = list(a)

print(a == c)
print(a is c)


# • "is" expressions evaluate to True if two 
#   variables point to the same object

# • "==" evaluates to True if the objects 
#   referred to by the variables are equal

# If the address of a and b are printed 
# i.e, id(a) & id(b), they both point to the same address.
# a "is" pointing to the same address as b also, a is equal to b.
# But when the address of c is printed, it is pointed different from address pointed by a.
# This indicates, c is pointed to different address than a, 
# therefore resulting in a boolean false as output. While the value of a and c are equal.
"""
 

# Trick - 8
"""
# Functions are first-class citizens in Python.

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def myfunc(a, b):
	return a + b

funcs = [myfunc]
print(funcs[0])
# <function myfunc at 0x107012230>

print(funcs[0](2, 3))

"""

# Trick - 9
"""
# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_if('mul', 2, 8))
print(dispatch_dict('mul', 2, 8))
print(dispatch_if('unknown', 2, 8))
print(dispatch_dict('unknown', 2, 8))
print(dispatch_if('add', 2, 8))
print(dispatch_dict('add', 2, 8))
"""

#Date:23-Nov-2019
# Trick - 10
"""
# Python's list comprehensions are awesome.

# vals = [expression 
#        for value in collection 
#        if condition]

# This is equivalent to:

# vals = []
# for value in collection:
#    if condition:
#        vals.append(expression)

# Example:

even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)
"""

# Trick - 11
"""
# Type hint and type-check using tool call mypy-lang
# More about this at https://www.youtube.com/watch?v=2xWhaALHTvU
# https://dev.to/dstarner/using-pythons-type-annotations-4cfe

def add_sum(a: int, b: int) -> int:
	return a + b

print(add_sum(3,7))
"""

# Date: 24-Nov-2019
# Trick - 12
"""
# Python's list slice syntax can be used without indices
# for a few fun and useful things

# https://www.programiz.com/python-programming/shallow-deep-copy

# You can clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
print(lst)
print("--------------------------------------")
# You can replace all elements of a list
# without creating a new list object:
a = lst
lst[:] = [7, 8, 9]
print("Original list is:", lst)
print("Copied list is", a)
print("a is lst ?:", (a is lst))

print("--------------------------------------")

# You can also create a (shallow) copy of a list:
b = lst[:]

print("Shallow Copied list b is",b)
print("id of lst is :",id(lst))
print("id of b is :",id(b))
print("b is lst? :",(b is lst))

print("--------------------------------------")

"""

# Trick - 13

"""

# collections.Counter lets you find the most common
# elements in an iterable:

import collections
c = collections.Counter('helloworld')
print(c)
print(c.most_common(3))

"""

#Date:25-Nov-2019
# Trick - 14
"""
# itertools.permutations() generates permutations 
# for an iterable. Time to brute-force those passwords ;-)

import itertools
for p in itertools.permutations('ABCD'):
    print(p)
"""

# Trick - 15
"""
# When To Use __repr__ vs __str__?
# Emulate what the std lib does:
import datetime
today = datetime.date.today()

# Result of __str__ should be readable:
print(str(today))
# >>> '2017-02-02'

# Result of __repr__ should be unambiguous:
print(repr(today))
# >>> 'datetime.date(2017, 2, 2)'

# Python interpreter sessions use 
# __repr__ to inspect objects:
print(today)
# >>> datetime.date(2017, 2, 2)

# Can get the timestamp using the datetime library
today = datetime.datetime.now()

print(today)
# >>> datetime.datetime(2019, 11, 25, 7, 43, 40, 776480)
# The first arg is year followed by month, date, hour, minute, seconds, milliseconds

print(str(today))
# >>> '2019-11-25 07:43:40.776480'

# If you want time in microseconds, then just run the below line, it will return time in microseconds
print(today.microsecond)

print(today.month) # To get the month from now() api
print(today.year) # To get the year from now() api 
print(today.day) # To get the day from now() api 
print(today.hour) # To get the hour from now() api 
print(today.minute) # To get the minute from now() api 
print(today.second) # To get the seconds from now() api 

"""

# Trick - 16
"""
# You can use Python's built-in "dis"
# module to disassemble functions and
# inspect their CPython VM bytecode:

def greet(name):
    return 'Hello, ' + name + '!' 

greet('Dan')
# >>> 'Hello, Dan!'

import dis
dis.dis(greet)

# 2   0 LOAD_CONST     1 ('Hello, ')
#     2 LOAD_FAST      0 (name)
#     4 BINARY_ADD
#     6 LOAD_CONST     2 ('!')
#     8 BINARY_ADD
#    10 RETURN_VALUE
"""




































