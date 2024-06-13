# any class may inherist from any other class
from class_a import Volunteer

# we may choose to inherit from some other class
class VolunteerGroup(Volunteer):
    '''Everything in the volunteer class is now available in this class
    We can extend the base class with additional properties and methods
    Number in group will be a positive integer property
    RaisedPerMember will be a method'''
    def __init__(self, n, hrs, r, num):
        # we typicaly call the __init__ of the parent class
        super().__init__(self, n, hrs, r) # just pass the arguments it needs
        self.num = num # this will call our num setter function
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, new_num):
        if type(new_num)==int and new_num > 0:
            self.__num = new_num
        else:
            raise TypeError('Number of people in volunteer group must be a positive integer')
    def raisedPerMember(self):
        '''Here we divide the total raised by the numbero f group members'''
        tot = self.totalSponsorship()
        perGroupMember = tot/self.num
        return perGroupMember
    
if __name__ == '__main__':
    # here we exercise the code
    # we can still create individula volunteers
    v5 = Volunteer('Gerty', 567, 9)
    grpA = VolunteerGroup('GoGetters', 34624, 33.3, 8)
    print(f'Group called {grpA.name} raised {grpA.raisedPerMember()} each from {grpA.num} volunteers')


