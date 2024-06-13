# we can handle strings in many ways
my_words = '''Python is     a stonking \t tool with 
loads of\n handy uses'''
# we can make it web-compatible (or DB etc)
words_bytes = bytes(my_words,encoding='UTF8') # bytes are handy...
# alternative
web_str = my_words.encode() # either method makes a URL friendly string of text
# NB there is also decode()

c = ['feedback', 'Skillnet', 'EasyRetro']
t = ' - '.join(c) # take all the members of c and join them using this separator
print(t)

s = '        this contains whitespace           '
print(s)
print(s.strip())

u = my_words.upper() # force al the characters to upper case (aler lower())

if __name__ == '__main__':
    print(words_bytes, web_str)