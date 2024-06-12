# we can use printing to show formatted values
import time

if __name__ == '__main__':
    # print( time.time() ) # a weird number
    # we may need a certain accuracy
    t = time.time()
    # it is a good idea to maintain accuracy right up to the point we print
    print(f'The time numeric is {t:0.2f}') # round to 2dp