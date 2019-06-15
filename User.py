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

    users_list = []
    def _init_(self,first_name,last_name,password):
        '''
        Method to define the property that each user object will hold.
        '''