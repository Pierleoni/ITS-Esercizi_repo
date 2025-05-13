import Ex_1 
import Ex_2
class Course:
    def __init__(self, name:str):
        self.name = name
        self.groups = []
    def register(self, student): 
        '''
        Trova il primo gruppo disponibile 
        '''
        for group in self.groups:
            # usa il metodo add_student della classe Group
            if group.add_student(student):
                return True #Ritorna True se trova un gruppo disponibile
        return False #Ritorna falso se nessun gruppo è disponibile
    def get_groups(self):
        return self.groups
    def add_group(self, group):
        self.groups.append(group)
