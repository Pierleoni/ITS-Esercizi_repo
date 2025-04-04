class Persona:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last = last_name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.last}, {self.age}"
    
    def setName(self, name):
        self.name = name
        return name
    def setLast(self, last_name):
        self.last = last_name
        return last_name
    def setAge(self, age):
        self.age = age
        return age
    def __call__(self):
        if self.age<18:
            print(f"{self.name} {self.last} è minorenne")
        elif 18<= self.age <30:
            print(f"{self.name} {self.last} è maggiorenne")
        elif 30<=self.age <80:
            print(f"{self.name} {self.last} è vecchio")
            



