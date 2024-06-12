print(__name__) # what is this module???


# when we import, EVERYTHING imported will run
import using_functions # we now have access to our functions
# or
from using_functions import checkIfEven

if __name__ == '__main__':
    k = 97
    # print(using_functions.checkIfEven(k)) # False
    print(checkIfEven(k)) # False