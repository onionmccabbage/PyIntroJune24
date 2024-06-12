# Python comments look like this
# All python code is written in a module like this
# Variables, data types and collections

a = 3   # this is an integer data type
b = 7.4 # this is a floating point data type

print(a, type(a) ) # NB Python is case-sensitive so keep an eye out...
print(b, type(b) ) 

print( a/b , a*b, a+b, b-a ) # we can print an unlimited number of variables
# NB Epsilon is the small margin of error ALL computers will encounter

s = 'changed'
s = 'is it coffee yet?' # a string data-type
print(s, type(s), len(s) ) # string is an immutable collection of characters

# we can use slicing to access members of a string collection
print(s[4])# we expect t - all collections in Python are zero-based
print(s[4:16:2]) # slicing is [start:stop-before:step]

# Other collections: list, tuple
l = ['hello', 432, True, a, b, s, 42] # this makes a list collection (like an array) - zero-based mutable collection of any data types
print(l[0:5:2], type(l))
t = (67456, False, 'ummmm', 54.32, l, b, 9) # a tuple is an immutable zero-based collection of any data types
print(t[3:6:3], type(t))