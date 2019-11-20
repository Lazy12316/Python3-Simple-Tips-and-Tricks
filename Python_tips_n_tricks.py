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
"""
# How to sort a python dictionary by value (== get a representation sorted by value)
"""

# Method-1
xs = {'a':4,'b':3,'c':2,'d':1}

print("Method - 1")
print(sorted(xs.items(), key = lambda x : x[1]))


print("Method - 2")
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
