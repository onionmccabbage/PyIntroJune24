# there are many ways to create a string of characters
s1 = 'here is a sting'
s2 = "this is also a string"
s3 = '''and this is a string
the triple quotes lets us preserve
 whiteapace such as new lines and           tabs'''
s4 = """also possible like this"""

# Functions let us write reusable code

def checkIfEven(n): # we may choose to pass arguments into our functions
    '''we may write a docstring here
    This function checks to see if a value is an even number'''
    if n%2 == 0: # ...then it is an even integer
        return True
    else:
        return False

# def lets us define a function
def getNum():
    '''ask the user for an even number'''
    g = input('tell us an even number: ') # remember: input ALWAYS returns a string
    g_int = int((float(g))) # we are after an integer
    # we can use our other function to check
    if checkIfEven(g_int): # here we call our reuseable checker function
        return g_int # return will end hte function by returning a value
    else:
        return 'not an even integer'

# we can use rthe function like this
result = getNum() # we invoke the function
print(result)

# we can acces the docstring like this
print(  getNum.__doc__  )
# Fact: anything with leading and trailing double underscore is a part of Python (dunder)

