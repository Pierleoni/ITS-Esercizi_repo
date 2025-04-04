# First Class
class User:
    def __init__(self, first_name:str, last_name:str, username:str, email:str):
        self.name = first_name
        self.last = last_name
        self.user = username
        self.email = email
    
    # describe_user method: describe the info about the users
    def describe_user(self):
        print(f"Nome: {self.name}. \nCognome: {self.last}. \nUsername:{self.user}. \nEmail:{self.email}")
    
    # greet_user method: prints a message for the login
    def greet_user(self):
        print(f"Welcome, {self.name} {self.last}!")

# second class
class Priviliges: 
    def __init__(self, priviliges_list:list[str])->list:
        self.priviliges = priviliges_list
    
    # show_priviliges method: prints a list of a priviliges 
    def show_priviliges(self):
        print(f"The list of priviliges is: {self.priviliges}")

# Third Class

class Admin:
    def __init__(self, user:User, priviliges:Priviliges):
        self.user = user
        self.priviliges = priviliges
        
    def show_info(self):
        self.user.describe_user()
        self.priviliges.show_priviliges()
        
        