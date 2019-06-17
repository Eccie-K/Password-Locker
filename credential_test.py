import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """


def setUp(self):
    """
    set up method to run before  each test cases
    """
    self.new_credential = Credential("Instagram", "0000")


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.account, "Instagram")
    self.assertEqual(self.new_user.password, "0000")


def test_save_credential(self):
    '''
    test_save_credential test case to test if the credential object is saved into
     the credential list
    '''
    self.new_credential.save_credential()  # saving the new credential
    self.assertEqual(len(Credential.credential_list), 1)

# setup and class creation up here


def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    Credential.credential_list = []


def test_save_multiple_credential(self):
    '''
    test_save_multiple_credential test checks to test if the user can save multiple credential to our user_list
    '''
    self.new_credential.save_credential("Instagram", "0000")
    self.assertEqual(len(Credential.credential_list), 2)


def test_confirm_credential(self):
    '''
    Function to confirm login details to current credential
    '''
    self.new_credential = Credential("Instagram", "0000")
    self.new_credential.save_credential()
    self.test_credential = Credential("Instagram", "0000")
    # test_credential.save_credential()
    # active_credential = Credential.confirm_credential("Instagram", "2000")
    # self.assertTrue(active_credential)


def test_display_all_credentials(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()