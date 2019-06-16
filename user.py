class User:
    """
    class that generates new instance of users
    """
    
    user_list = []  # empty Users list

    def save_user(self):
        '''
        save_user method that saves user objects into user_list
        '''
        User.user_list.append(self)

    

    def __init__(self, username, password, email):
        '''
        defining the structure of the user object
        '''

        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def confirm_user(cls, username, password, email):
        '''
        Method to check if the name, password and email entered match entries in the users_list
        '''
        current_user = ''
        for user in User.user_list:
            if (user.username == username and user.password == password):
                current_user = user.username
        return current_user

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list


    
