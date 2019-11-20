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



#Consider the following dictionary. If a know key is passed, the method greeting will return string HI "userid". if key is invalid, the method will throw key error.

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

# namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries. Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. The arguments are the name of the new class and a string containing the names of the elements.

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
