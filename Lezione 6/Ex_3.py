class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    
    def set_leg(self, legs:int):
        self.legs = legs
    def getLeg(self):
        return f"Ammount of legs:{self.legs}"
    def print_info(self):
        print (f"Nome: {self.name}, Legs: {self.legs}")

an_1:Animal = Animal("Jaguar", 4)
an_1.set_leg(5)
an_1.set_leg(10)
print(an_1.getLeg())
an_1.print_info()
print("--------------------")
an_2:Animal = Animal("Tiger", 4)
an_2.print_info()
an_2.legs = 6
an_2.set_leg(8)
print(an_2.getLeg())
an_2.print_info()

