# the big idea is we can re-use a function again and again

def util(tup):
    a = tup[0] + tup[1]
    b = tup[0] - tup[1]
    return (a, b) # return a tuple with the results

# here is a function to validate we have two numeric values, 
# then return a tuple containing the total and the difference
def sumDiff(x, y):
    if type(x) in (int, float) and type(y) in (int,float):
        # all good, go ahead
        result = util( (x,y) )
    else:
        try:
            x = float(x) # try to cast to a number
            y = float(y)
        except Exception as err:
            # just set some sensible defaults
            x=1
            y=2
        result = util( (x,y) )
    return result

# we can extend this idea of reuseability to map and filter...
def useMap():
    # we can repeatedly apply a function across a bunch of values using 'map'
    my_values = range(-9, 10) # start, stop-before
    results_l = map(sumDiff, my_values, my_values)
    return results_l

def isOdd(n):
    '''return True if odd, False otherwise'''
    if n%2 !=0:
        return True
    else:
        return False

def useFilter():
    # filter lets us repeatedly use a function to filter the results
    r = range(-9,10)
    odds = filter(isOdd, r)
    return odds

if __name__ == '__main__':
    # execise the code
    print( sumDiff(44, 55) ) # (99, -11)
    print( sumDiff('44', 55) ) # (99, -11)
    print( sumDiff(True, 55) ) # Here the value True is being cast to a float...
    print( sumDiff('no', 'oops') ) # (1, -1)
    # try using the map in 'useMap'
    print( useMap() )
    r = useMap()
    for _ in r: # iterate over the map object - see eahc value that has been calculated
        print( _ )
    o = useFilter() # call our filter function
    for item in o:
        print(item)