import random
class Die:
    def __init__(self, sides:int = 6):
        self.sides = sides
    def roll_die(self):
        return random.randint(1,self.sides)

print("Lancia il dado a 6 facce:")
die_6 = Die()
for i in range(10):
    print(die_6.roll_die())

print("---------------------------")
print("Lancia il dado a 10 facce:")

die_10:Die = Die(10)

for i in range(10):
    print(die_10.roll_die())


print("---------------------")

print("Lancia il dado a 20 facce:")
die_20:Die = Die(20)

for i in range (20):
    print(die_20.roll_die())


