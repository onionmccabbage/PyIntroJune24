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
r = input() # stop and get the user to type something (this is I/O bound)
if r == 'hello':
    print('and hello to you too!')