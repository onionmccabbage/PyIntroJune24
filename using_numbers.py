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
i = int(float(input('enter an integer ')))
print(f'You entered {i}')