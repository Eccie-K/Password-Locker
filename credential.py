class Credential:
    """"
    A class that generates new instances of credentials
    """
    credential_list = []


    def __init__(self, account, password):
        '''
        __init__method that helps us with the properties of the  user object
        Args:
            account: new credential account
            password: new credential password
        '''
        self.account = account
        self.password = password


    def save_credential(self):
            '''
            save_credential method saves credential objects into credential_list
            '''
            Credential.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user list
        '''
        return cls.credential_list


    # def confirm_credential(cls, username, password):
    #         '''
    #         Method that checks if the account and password  entered match entries in the credential_list
    #         '''
    #         current_credential = ''
    #         for credential in Credential.credential_list:
    #             if (credential.account == account and credential.password == password):
    #                 current_user = credential.username
    #         return current_credential