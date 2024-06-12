# file input and file output

def printTofile(s):
    '''write the string s to a text file'''
    # we need a file access object
    fout = open('my_log.txt', 'at') # 'at' will append text
    print(s, file=fout) # we can send any print ot a file access object!!!
    fout.close() # always a good idea to tidy up (release resources)


if __name__ == '__main__':
    words = 'here is some data to be written'
    printTofile(words)