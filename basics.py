# Python comments look like this
# All python code is written in a module like this
# Variables, data types and collections

a = 3   # this is an integer data type
b = 7.4 # this is a floating point data type

print(a, type(a) ) # NB Python is case-sensitive so keep an eye out...
print(b, type(b) ) 

print( a/b , a*b, a+b, b-a )
# NB Epsilon is the small margin of error ALL computers will encounter

s = 'changed'
s = 'is it coffee yet?' # a string data-type
print(s, type(s), len(s) ) # string is an immutable collection of characters

# we can use slicing to access members of a string collection
print(s[4])# we expect t - all collections in Python are zero-based
print(s[4:16:2]) # slicing is [start:stop-before:step]