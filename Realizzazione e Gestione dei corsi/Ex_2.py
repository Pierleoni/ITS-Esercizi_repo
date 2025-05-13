class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None
    def set_group(self, group):
        self.group = group
        



class Lecturer(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        

class Group:
    def __init__(self,name:str, limit:int):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
    def get_name(self):
        return self.name
    def get_limit(self):
        return self.limit
    def get_students(self):
        return self.students
    def get_limit_lecturers(self):
        '''
        len(self.students): conta quanti studenti ci sono nella lista self.student
        len(self.students)//10: divide il numero di elementi presenti nella lista degli studenti 
        e divide quel numero per 10 e mantiene la parte intera.
        max(1, len(self.students) // 10): confronta il risultato della divisione intera con 1 e prende il vlaore massimo tra i due, 
        garantendo che il risultato sia almeno 1, anche se ci sono meno di 10 studenti
        '''
        
        max_lecturers = max(1,len(self.students)//10)
        return max_lecturers
    def add_student(self, student):
        if len(self.students)<self.limit:
            self.students.append(student)
            student.set_group(self)
            return True 
        return False
    def add_lecturer(self, lecturer):
        if len(self.lecturers)<self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True 
        return False


p_1:Person = Person("CF123", "John", "Doe", 30)
stud_1:Student = Student("CF456", "Jane", "Smith", 20)
lect_1:Lecturer = Lecturer("CF789", "Dr. Emily", "Brown", 45)




print("Test della classe Person:")
print(f"CF: {p_1.cf}")
print(f"Name: {p_1.name}")
print(f"Surname: {p_1.surname}")
print(f"Age: {p_1.age}")

print("\nTest della classe Student:")
print(f"CF: {stud_1.cf} ")
print(f"Name: {stud_1.name} ")
print(f"Surname: {stud_1.surname}")
print(f"Age: {stud_1.age}")
print(f"Gruppo iniziale: {stud_1.group}")

group1:Group = Group ("Group A", 10)
stud_1.set_group(group1)
print("\nDopo set_group di stud_1:")
print(f"Gruppo di studenti: {stud_1.group.get_name()}")


