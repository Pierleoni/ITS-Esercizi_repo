class Student:
    def __init__(self, name:str, study_program:str, age:int, gender:str):
        self.name = name
        self.study_program = study_program
        self.age = age
        self.gender = gender
    def print_info(self):
        print(f"Nome dello studente: {self.name}. \n\nEtà: {self.age}. \n\nGenere: {self.gender} \n\nProgramma di Studio: {self.study_program}. ")



myself:Student = Student("Marco", "Full Stack Developer", 26, "Maschia")

lefty:Student = Student("Leonardo", "Full Stack Developer", 22, "based Male")

right:Student = Student ("Popa", "Full Stack Developer", 21, "Rossi")

myself.print_info()

lefty.print_info()

right.print_info()



class Person:
    personCount = 0
    def __init__(self, name):
        self.name = name
        self.update()
    @classmethod #é una direttiva che va ad indicare che stai andando ad accedere agli attributi di classe, senza di esso il cls sotto verrebbe interpretato come un self
    def update(cls):
        cls.personCount += 1
        
        
alice = Person("Alice W.")
bob = Person("Bob M.")
print("------------------")
print(Person.personCount)