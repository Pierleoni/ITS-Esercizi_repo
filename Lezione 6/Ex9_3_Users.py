class User:
    def __init__(self, name:str, last_name:str, age:int, password:str, id_user:str):
        self.name = name
        self.last = last_name
        self.age = age
        self.pwrd = password
        self.id = id_user
    def describe_user(self): 
        print(f"Nome: {self.name}. \nCognome: {self.last}. \nAge: {self.age} \nPassword: {self.pwrd}. \nID User: {self.id}.")
    def greet_user(self): 
        print(f"Welcome, {self.name} {self.last}")


user_1:User = User("Giacomo", "Rossi", 23, "AG)38?22!aD", "@0001AB")

User_2:User = User ("Davide", "Mancini", 33, "D833rT?!", "@0002AC")

user_3:User = User ("Carlo", "Conti", 22, "S1Lvini9nf1me19)!", "@0002AD")

user_1.describe_user()


user_1.greet_user()

print("--------------")
User_2.describe_user()
User_2.greet_user()

print("--------------")
user_3.describe_user()
user_3.greet_user()

