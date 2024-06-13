# the arguments passed in to a function may be positional or keyword arguments
# without a default, the argument is 'positional'
# with a default, the argument is 'keyword'
def fn(x, y, z=10):
    av = (x+y+z)/3
    return av

# there is nothing special about the term args or kwargs - they are convetions
def usePositional(*args): # * gathers positonal arguments
    '''any and every positional argument can be gathered into a tuple'''
    print(args, type(args), len(args))
    for i in args:
        print(i)

def useKeyword(**kwargs): # ** gathers keyword arguments
    '''any and every keyword argument can be gatherd into a dict'''
    print(kwargs, type(kwargs))
    for (k,v) in kwargs.items():
        print(f'item {k} is {v}')

if __name__ == '__main__':
    r = fn(2, 6) # call our function (use defaults if available)
    print(r)
    s = fn(5, 5, 5) # we override the default
    print(s) # 5.0
    # exploring positional arguments
    usePositional(5,4,3,2,1)
    useKeyword(x=3, y=4, n=True, f=fn)