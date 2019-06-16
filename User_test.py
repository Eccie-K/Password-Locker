import unittest # importing the unittest module
from user_credentials import User # importing the user class

class  TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating testcases
    '''
    def setUp(self):
        '''
        setUp method to run before each test cases
        '''
        self.new_user = User("Ess", "Lay", "passwd") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object initialized properly
        '''
   


