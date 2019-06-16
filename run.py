#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(account, password):
    """
    Function to create a new user
    """
    new_user = Credential(account, password)
    return new_user


def save_user(username, password, email):
    """
    saving the user
    """
    User.save_user


def display_user():
    return User.display_user()


def save_credential(self):
    '''
    save_credential method saves credential objects into credential_list
    '''
    Credential.credential_list.append(self)


def confirm_user(username, password, email):
    '''
    Method that checks if the name, password and email entered match entries in the users_list
    '''
    current_user = ''
    for user in User.user_list:
        if (user.username == username and user.password == password):
            current_user = user.username
    return current_user


def main():
    print('Welcome to password-locker')
    while True:
        print("-"*10)
        print("Use these short codes : cc - create a new user, du - display users, fu -find a user, ex -exit the user list ")
        short_code = input('choose any of the above:').lower().strip()
        if short_code == 'ex':
            exit

        elif short_code == 'cc':
            print("-"*10)
            print(' ')
            print('create new account:')

            print("username")
            username = input()

            print("password")
            password = input()

            print("email")
            email = input()

            save_user(username, password, email)
            # creates and saves new user
            print('\n')
            print(f"New User {username} {email} created")
            print('\n')

        elif short_code == 'du':
            if display_user():
                print("Here is a list of users")

                for user in display_user():  # loops through the user object to get each user
                    print(f"{user.username} {user.email}")
                    print('\n')

                else:
                    print('\n')
                    print("No users saved yet")
                    print('\n')

        elif short_code == 'cu':
                print("Enter user to confirm existance")
                search_username = input()
                if confirm_user(username, password, email):
                    print(f"{search_username}")
                else:
                    print("Sorry,user does not exist")

        elif short_code == "ex":
            print("Thanks and nice time!")


if __name__ == '__main__':
    main()