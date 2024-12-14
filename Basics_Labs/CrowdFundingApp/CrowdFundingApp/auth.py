
import json             # for save_user function
from utils import validate_name, validate_phone, validate_password, validate_email


class User:   # represent a user and handle user-related attributes.
    def __init__(self,first_name,last_name,email,password,phone):  #  initialize the following attributes when creating a new User object.
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
    
    # store user data in an object notation format "json", data then will be used by save_user() function to be stored in a json file
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone
        }




"""
Why keeping register() function outside class User ?
 register(), it’s not directly tied function to a specific user instance. 
Instead, it’s a process that gathers data before a user object exists in the system

Methods that are specific to a user’s actions after they’re created, like "viewing or editing profile details"  make great instance methods within the User class.
 
The User class is responsible for defining what a user is, 
it stores attributes like first_name, last_name, email, etc... in a unified datastructure blueprint
The register() function, on the other hand, is a process or action that involves multiple steps like validation and user input. 
By separating them, we keep the User class focused on data, while register() handles the logic.

Don't forget that "class is a bluprint" mainly so you just need to make a unified data structure for a specific object properties

"""

def register():
    print("Please Register your Account:")


    first_name = validate_name("First Name: ")
    last_name = validate_name("Last Name: ")
    email = validate_email("Email: ")
    password = validate_password("Password: ", "Confirm Password: ")
    phone = validate_phone("Mobile Phone: ")

    # Create a new User instancet 
    new_user = User(first_name, last_name, email, password, phone)
    
    # call the save_user function to save user data to a file
    save_user(new_user)     
    
    print("Registration successful!")


# Recieve data retured from to_dict() class method and append it to the json file
def save_user(user):
    try:
        with open('users_data.json', 'r') as file:      # open file for read
            users = json.load(file)                     # load file with the current stored data to a variable
    except Exception as e:
        print(e)
        return False
    else:
        users.append(user.to_dict())                        # append data to users var from to_dict() function return, user here is the user parameter which passed at first and holds new_user object data

        with open('users_data.json', 'w') as file:          # save variable data to json file with specific indentation
            json.dump(users, file, indent=4)                


def login():
    print("Please Login to your Account:")
    email = validate_email("Email: ")
    password = input("Password: ")          # often does not require syntax validation like email

    # call authenticate_user() function to check user existence against the database (which here is the json file)
    user = authenticate_user(email, password)
    if user:                                # if user return is true 
        print("Login successful!")
        return user
    else:                                # Executed only if the try condition is true, use "finally" instead if you want to execute this block in all cases even if there was an error
        print("Invalid email or password.")
        return None

def authenticate_user(email, password):
    try:    
        with open('users_data.json', 'r') as file:  # open file for read
            users = json.load(file)                 # load data into variable
    except FileNotFoundError:
        users = []

    for user in users:                  # loop over users data inside users var 
        if user['email'] == email and user['password'] == password:     # check if the provided mail and password exist eaxactly for one user
            return user
    return None
