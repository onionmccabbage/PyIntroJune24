# there is a data structure called a 'range'
r = range(0,11) # start, stop-before. The values do NOT persist in memory
print(r)
for i in r:
    print(i)
# this is handy e.g. for even numbers only
e = range(-1000, 1001, 2) # start, stop-before, step
for _ in e: # we can use anything for our iterable, Python often uses _
    print(_) # we get just event numbers

# we can make a list using a range
# Here is a list of square numbers
squares = [i*i for i in range(0,11)] # we have a list
print(squares, type(squares))

# using conditional logic
# EVERY input is ALWAYS a string (never anything else)
r = input('Enter something: ') # stop and get the user to type something (this is I/O bound)
r = r.lower() # force the string to lower case (or upper)
if r == 'hello': # we use == to check equality. Also != for not equal <, > <=, >= also
    print('and hello to you too!')
elif r =='greetings':
    print('Well hi there')
elif 'hi' in r: # we often use 'in' to check if a mamber is in a collection
    print('I think you said hi')
else:
    print(f'Well I dont understand {r}')