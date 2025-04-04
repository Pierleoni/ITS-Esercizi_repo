class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age :
    print(alice.name)
else: 
    print(bob.name)
    

carl:Person = Person("Carl M.", 84)

vick:Person = Person ("Vick Van Dick", 29)

daphne:Person = Person ("Daphne S.", 12)

edoardo:Person = Person ("Edoardo P.", 25)


people:list[Person] = [
    Person("Alice W.", 45),
    Person("Bob M.", 36),
    Person("Carl M.", 84),
    Person ("Vick Van Dick", 29),
    Person ("Daphne S.", 12),
    Person ("Edoardo P.", 25)
]

current = people[0]

for person in people[1:]:
    if person.age < current.age:
        current = person

print(f"il più giovane della lista è: {current.name}, {current.age}")








