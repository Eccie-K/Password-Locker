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
    #Class Variables
    credentials_list  =  []
    user_credentials_list  =  []

    @classmethod
    def check_user(cls,  first_name,  password):
        '''
        method that checks if the name and password provided match the entries in the users_list
        '''
        current_user = ''
        for user in User.users_list:
            if(user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return  current_user

    def _init_ (self, user_name, site_name, account_name, password):
        '''
        Method to define the properties that will be held by each user
        '''

        #instance variables
        self.user_name  =  user_name
        self.site_name  =  site_name
        self.account_name  =  account_name
        self.password  =  password

    def save_credentials(self):
        '''
        Function to save a newly created user instance
        '''
        #global users_list
        Credential.credentials_list.append(self)

    def generate_password(size=8,  char  =  string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate a 8 character password for every instance
        '''
        
        gen_passwd  =  ''.join(random.choice(char) for _ range(size))
        return  gen_passwd

    @classmethod
    def display_credentials(cls, user_name):
        '''
        Class method to display the list of saved credentials
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credential_list.append(credential)
                return user_credentials_list

    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Method that returns the credentials that match the site name entered
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential 
