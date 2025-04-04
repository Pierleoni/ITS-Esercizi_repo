class User:
    def __init__(self, name:str, last_name:str, age:int, password:str, id_user:str, login_attempts:int):
        self.name = name
        self.last = last_name
        self.age = age
        self.pwrd = password
        self.id = id_user
        self.login = login_attempts
    def describe_user(self): 
        print(f"Nome: {self.name}. \nCognome: {self.last}. \nAge: {self.age} \nPassword: {self.pwrd}. \nID User: {self.id}.")
    def greet_user(self): 
        print(f"Welcome, {self.name} {self.last}")
    def increment_login_attempts(self): 
        self.login += 1
        print(f"Number of attempts: {self.login}")
    def reset_login_attemps(self):
        self.login-=1
        print(self.login)




user_1:User = User("Giacomo", "Rossi", 23, "AG)38?22!aD", "@0001AB", 0)

user_2:User = User ("Davide", "Mancini", 33, "D833rT?!", "@0002AC", 0)

user_3:User = User ("Carlo", "Conti", 22, "S1Lvini9nf1me19)!", "@0002AD", 0)

print("------------------")
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.reset_login_attemps()
print("------------------")
user_2.describe_user()
user_2.greet_user()
user_2.increment_login_attempts()
user_2.reset_login_attemps()
print("------------------")
user_3.describe_user()
user_3.greet_user()
user_3.increment_login_attempts()
user_3.reset_login_attemps()




