# we tend to put imports at the top
import random

# we tend to gather function at the top
def makeRandInt():
    '''return another random integer'''
    return random.randint(0,10) # between 0 and 10

# we often write a 'main' function like this
def main():
    # if we need to keep running, we can use a run-loop like this
    while True:
        '''generate random numbers 0-10, print them and stop when we get to 5'''
        r = makeRandInt()
        print( r )
        if r == 5:
            break # this will break out of our loop

# we tend to check if this module is being run directly (rather than imported)
if __name__ == '__main__':
    main()