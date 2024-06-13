from functools import reduce

# 'reduce' means we repeatedly apply a function to the result of a previous function call
#  in other words, we reduce a bunch of values to end up with one result
def addThem(a,b):
    '''return the sum of a plus b'''
    return a+b

def useReduce(values_tup):
    total = reduce( addThem, values_tup )
    return total

if __name__ == '__main__':
    v = [i for i in range(0,11)] # remember - this is called comprehension
    r = useReduce(v)
    print(r) # 55
    print(f'The mean of {v} is {r/len(v)}') # 55/11 is 5.0