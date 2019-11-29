# Date:27-Nov-2019

# [🐍PyTricks]: Trick - 21
"""
# Python 3 allows unicode variable names

import math
π = math.pi
class Spin̈alTap: pass
print(Spin̈alTap())
# <Spin̈alTap object at 0x10e58d908>

# Only letter-like characters work
"""

# [🐍PyTricks]: Trick - 22
"""
# Awesome Python built-ins: globals() and locals()

# "globals()" returns a dict
# with all global variables
# in the current scope:

print(globals())
# >>> {...}

# "locals()" does the same
# but for all local variables
# in the current scope:

print(locals())
# >>> {...}]
"""

# [🐍PyTricks]: Trick - 23

"""
# Python 3.3+ has a new "faulthandler" std lib module
# Python 3.3+ has a std
# lib module for displaying
# tracebacks even when Python
# "dies", e.g with a segfault:

import faulthandler
faulthandler.enable()

# Can also be enabled with
# "python -X faulthandler"
# from the command line.

# Learn more here:
# https://docs.python.org/3/library/faulthandler.html
"""

# [🐍PyTricks]: Trick - 24
"""
# "for" (and "while") loops can have an "else" branch?!
# Python's `for` and `while` loops
# support an `else` clause that executes
# only if the loops terminates without
# hitting a `break` statement.

def contains(haystack, needle):
    
    #Throw a ValueError if `needle` not in `haystack`.
    
    for item in haystack:
        if item == needle:
            break
    else:
        # The `else` here is a
        # "completion clause" that runs
        # only if the loop ran to completion
        # without hitting a `break` statement.
        raise ValueError('Needle not found')


print(contains([23, 'needle', 0xbadc0ffee], 'needle'))
# >>> None

print(contains([23, 42, 0xbadc0ffee], 'needle'))
# >>> ValueError: "Needle not found"


# Personally, I'm not a fan of the `else`
# "completion clause" in loops because
# I find it confusing. I'd rather do
# something like this:
def better_contains(haystack, needle):
    for item in haystack:
        if item == needle:
            return
    raise ValueError('Needle not found')

# Note: Typically you'd write something
# like this to do a membership test,
# which is much more Pythonic:
if needle not in haystack:
    raise ValueError('Needle not found')
"""
# Date:28-Nov-2019
# [🐍PyTricks]: Trick - 25
"""
# Pythonic ways of checking if all
# items in a list are equal:

lst = ['a', 'a', 'a']

print(len(set(lst)) == 1)
# >>> True

print(all(x == lst[0] for x in lst))
# >>> True

print(lst.count(lst[0]) == len(lst))
# >>> True

# I ordered those from "most Pythonic" to "least Pythonic" 
# and  "least efficient" to "most efficient". 
# The len(set()) solution is idiomatic,  but constructing 
# a set is less efficient memory and speed-wise.
"""
# [🐍PyTricks]: Trick - 26

"""
# Forced keyword-only parameters in Python 3.x
# In Python 3 you can use a bare "*" asterisk
# in function parameter lists to force the
# caller to use keyword arguments for certain
# parameters:

def f(a, b, *, c='x', d='y', e='z'):
    return 'Hello'

# To pass the value for c, d, and e you 
# will need to explicitly pass it as 
# "key=value" named arguments:

print(f(1, 2, c='p', d='q',e='v'))
# >>> 'Hello'

print(f(1, 2, 'p', 'q', 'v'))
# >>> TypeError: 
#      "f() takes 2 positional arguments but 5 were given"
"""

# [🐍PyTricks]: Trick - 27

"""
# Multiple sets of kwargs in Python 3.5+.
# Python 3.5+ allows passing multiple sets
# of keyword arguments ("kwargs") to a
# function within a single call, using
# the "**" syntax:

def process_data(a, b, c, d):
	print(a, b, c, d)

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}

print(process_data(**x, **y))
# >>> 1 2 3 4

print(process_data(**x, c=23, d=42))
# >>> 1 2 23 42
"""




