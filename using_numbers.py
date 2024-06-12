# Python includes many functions built in, e.g. range, print, for etc.
# Python also includes a 'standard library'
# we can import useful stuff from the standard library
import time # this comes with Python
from random import randint # here we pick just one part of the 'random' library

# there are other mathematical operators beyond + / * -
print( 10//3 ) # the integer number of times we can divide ten by three (modulo)
print(10%3)    # the remainder when we divide ten by three (remainer)

a = 7.6
b = int(a)
print(b) # 7 (integer)
c = float(b) # 7.0 (float)
print(c)
t = (5,4,3,2)
l = list(t) # convert it to a list
# remember, every input is a string... so if we need an int...
try: # we should use try around any dodgy code
    i = int(float(input('enter an integer ')))
    print(f'You entered {i}')
except ValueError as ve: # we may choose to handle specific faults
    print('That is not an integer!!')
except Exception as err: # here we handle any exception
    print(f'Something went wrong {err}')
finally: # this is optional - but can be handy
    print('All done') # finally will ALWAYS run (even if ther is an exception)

print(time.time()) # now!!
print(time.localtime()) # now in a human friendly format

# use randint
r = randint(0,10) # a random integer between 0 and 10 (or any values)
print(f'The random integer is {r} at {time.localtime()}')
