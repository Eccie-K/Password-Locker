#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(username, password,email):
    """
    Function to create a new user
    """
    new_user = User(username, password,email)
    return new_user



def display_user():
    return User.display_user()


def save_user(self):
    '''
    save_user method saves credential obUser user_list
    '''
    User.user_list.append(self)


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
    print("-"*20)
    while True:
        
        print("Use these short codes : cc - create a new user, du - display users, fu -find a user, ex -exit the user list ")
        short_code = input('choose any of the above:').lower().strip()
        

        if short_code == 'cc':
            print("-"*10)
            print('create new account:')

            print("username")
            username = input()

            print("password")
            password = input()

            print("email")
            email = input()

            save_user(create_user(username, password, email))
            # creates and saves new user
            print('\n')
            print(f"New User {username}.... {email} created")
            print('\n')

        elif short_code == 'du':
            if display_user():
                print("Here is a list of users")
                print("-"*20)

                for user in display_user():  # loops through the user object to get each user
                    print(f"{user.username}....... {user.email}")
                    print('\n')

                else:
                    print('\n')
                    print("No users saved yet")
                    print('\n')

        elif short_code == 'fu':
                print("Enter user to confirm existance")
                print("-"*20)
                search_username = input()
                print("-"*20)
                if confirm_user(username, password, email):
                    print(f"Username...{search_username}")
                    
                    
                else:
                    print("Sorry,user does not exist")

        elif short_code == "ex":
            print("Thanks and nice time!")
            break


if __name__ == '__main__':
    
         main()