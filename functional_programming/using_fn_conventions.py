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

if __name__ == '__main__':
    # execise the code
    print( sumDiff(44, 55) ) # (99, -11)
    print( sumDiff('44', 55) ) # (99, -11)
    print( sumDiff(True, 55) ) # 
    print( sumDiff('no', 'oops') ) # (1, -1)