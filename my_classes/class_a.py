# We will encapsulate a volunteer. Name, hours, sponsor rate
# we could use a tuple, a list or a dict
v_t = ('Edith', 34.2, 6) # a tuple - can't be changed
v_l = ['Edith', 34.2, 6] # a list - we can alter values
v_d = {'name':'Edith', 'hours':34.2, 'rate':6} # a dict
# but we ,ight acidentaly set something daft
v_d['rate']=-88 # oops - there is no way to validate the data

# That is one reason to use a class - classes let us validate and manage the data
class Volunteer: # NB this is a code block so we MUST indent
    '''Volunteer will encapsulate name (non-empty string)
    the hours volunteered (positive int or float)
    and the sponsor rate (positive int or float)'''
    # NB all functions in a class MUST take 'self'
    def __init__(self, n, hrs, r): # self refers to the instance being created
        '''this runs every time we make an instance of this class'''
        self.name  = n
        self.hours = hrs
        self.rate  = r

if __name__ == '__main__':
    '''here we can exercise the code'''
    v1 = Volunteer('Edith', 34.2, 6)  #here we have made an instance of our class
    v2 = Volunteer('Deidre', 54.9, 7)
    v2.hours = 83.0 # we can change values stored in class properties
    # we may see any of the properties of this class instance
    print(v1, v1.name, v1.hours) # we can access properties using dot notation
    print(f'Voluneer {v2.name} did {v2.hours} hours at {v2.rate}')
