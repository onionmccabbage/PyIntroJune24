# We will encapsulate a volunteer. Name, hours, sponsor rate
# we could use a tuple, a list or a dict
v_t = ('Edith', 34.2, 6) # a tuple - can't be changed
v_l = ['Edith', 34.2, 6] # a list - we can alter values
v_d = {'name':'Edith', 'hours':34.2, 'rate':6} # a dict
# but we ,ight acidentaly set something daft
v_d['rate']=-88 # oops - there is no way to validate the data

# That is one reason to use a class - classes let us validate and manage the data
class Volunteer: # NB this is a code block so we MUST indent
# class Volunteer(): # the brackets are optional (by default classes inherit from object)
# class Volunteer(object): # we may choose to explicitly inherit from another class
    '''Volunteer will encapsulate name (non-empty string)
    the hours volunteered (positive int or float)
    and the sponsor rate (positive int or float)'''
    # NB all functions in a class MUST take 'self'
    # we MUST use __init__ for the initializer
    def __init__(self, n, hrs, r): # self refers to the instance being created
        '''this runs every time we make an instance of this class'''
        self.name  = n   # this will actually call the name setter method
        self.hours = hrs # we will use getter/setter methods to validate the hours
        self.rate  = r
    # we may write methods of our class
    # A method is something the class can do, (its just a function)
    def totalSponsorship(self):
        return self.hours*self.rate
    @property # this decorator gets the property
    def name(self):
        return self.__name
    @name.setter # this makes the method behave like a property (sets the property)
    def name(self, new_name):
        if new_name != '' and type(new_name) == str:
            self.__name = new_name # we use __ for mangled properties
        else:
            raise TypeError('Name must be a non-empty string')
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, new_hours):
        '''the valuee for new_hours must be a potive int or float'''
        if type(new_hours)==int or type(new_hours)==float:
            self.__hours = new_hours # all good
        else:
            self.__hours = 0 # we may choose to set a sensible default
    # and the same again for the rate...
    @property
    def rate(self):
        return self.__rate
    @rate.setter
    def rate(self, new_rate):
        if type(new_rate) in (int, float): # here we check if the type is in the tuple of permitted types
            self.__rate = new_rate
        else:
            self.__rate = 1

if __name__ == '__main__':
    '''here we can exercise the code'''
    v1 = Volunteer('Edith', 34.2, 6)  #here we have made an instance of our class
    v2 = Volunteer('Deidre', 54.9, 7)
    v2.hours = 83.0 # we can change values stored in class properties
    # we may see any of the properties of this class instance
    print(v1, v1.name, v1.hours) # we can access properties using dot notation
    print(f'Voluneer {v2.name} did {v2.hours} hours at {v2.rate} total: €{v2.totalSponsorship ()}')
    # here we will check that the name validates
    # v1.name = True # this should fail
    v1.name = 'Ede'
    # see what happens if we use invalid data
    v3 = Volunteer('Floella', 'ages', False) # this should default to 0 and 1
    print(f'{v3.name} {v3.hours} {v3.rate}') # Floella 0 1
