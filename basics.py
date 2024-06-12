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

# we may mutate a list
l[0] = 'coffee time' # here we change the content of the item at position zero in the list
l.append(False) # place the item on the end of the existing list
l.insert(3, 'three') # insert at position 3
print(l)

# iterating over collections
for letter in s:
    print(letter)
for item in l:
    print(item)
for item in t:
    print(item)

# Some other data types: dict, set and none
n = None # this is a handy type, it means none
my_set = {2,3,3,5,7.0,'any',3,8,2} # a set is a mutable collection of any types. Unique members only
my_set.add(4) # we can mutate a set
print(my_set, type(my_set))
# dictionary is a non-indexed mutable collection of key:value pairs of any data type
d = {'n':'Floella', 'level':'Admin', 'auth':True, 'age':64, 'age':99} # the last key-value persist
d['def'] = None # add to the dict
d['auth'] = False # mutate an existing member
print(d, type(d))
# dict has no numeric index, so we iterate like this:
for (k,v) in d.items(): # k will be the keys, v will be the values
    # we can use formatted strings for pretty printing
    print(f'we have {k} with {v}') # inject any variable using {}
    # print(k, v)

# we can print a csv like this
for i in l: # iterate over our list
    print(i,end=', ') # by default print will end with a new line. Wecan put anything we like instead

# ooo whats this...?
print(__name__) # we get __main__ when this module is run directly