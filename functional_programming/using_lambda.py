# exploring lambda functions, higher order functions and 'reduce'

def showPower(x,y):
    '''return x to the power of y'''
    return x**y

# lambda functions are useful when you don't whan the bother of writing a whole function
def flip(f):
    '''flip the arguments of the incoming function 'f' '''
    return lambda x, y:f(y, x) # a non-persistent function

if __name__ == '__main__':
    print( showPower(3, 2) ) # 9
    print( showPower(4, 3) ) # 64
    print( showPower(25, 0.5) ) # 5.0
    # see if the flip works...
    s = flip(showPower) # we now have a function that will flip arguments for showPower
    print( s(3, 2) )  # 2**3 which is 8
    print( s(4, 3) )  # 3**4 which is 81
    print( s(25, 0.5) )  # 0.5**25 which is 2.9802322387695312e-08