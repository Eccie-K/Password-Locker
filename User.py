import    random
import    string

#Global variables

global users_list
class User:
    '''
    Class to generate user accounts and save their information.
    '''
    #Class Variables
    #global users_list

    users_list = [] #empty User list
    def _init_(self,first_name,last_name,password):
        '''
        Method to define the property that each user object will hold.
        '''

        #creating instance variables
        self.first_name    =    first_name
        self.last_name    =    last_name
        self.password    =    password

        def save_user(self):
            '''
            Function to save a newly created user instance
            '''
            User.users_list.append(self)

class Credential:
    '''
    Class to create account credentials, generate passwords and save user information
    '''
    
