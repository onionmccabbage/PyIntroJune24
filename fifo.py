# file input and file output

def printTofile(s):
    '''write the string s to a text file'''
    # we need a file access object
    fout = open('my_log.txt', 'at') # 'at' will append text
    # print will default to adding a NEW LINE AT THE END
    print(s, file=fout) # we can send any print to a file access object!!!
    fout.close() # always a good idea to tidy up (release resources)

def writeToFile(s):
    '''commit text to a file using with'''
    with(open('my_log.txt', 'at') as fout):
        fout.write(s) # this will write the string to the file access object
        fout.write('\n') # we may choose to add a new line character
        # NB when you use 'with' it will automatically close the file when done

def readFromFile():
    '''read content back in from a text file'''
    with(open('my_log.txt', 'rt') as fin): # 'rt' will read text
        r = fin.read() # read back everything in the file
        return r

if __name__ == '__main__':
    words = 'here is some data to be written'
    # printTofile(words)
    writeToFile(words) # write will NOT add a new line at the end
    print( readFromFile() )