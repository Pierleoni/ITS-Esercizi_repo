class Persona:
    def __init__(self,name,last,age):
        self.name = name
        self.lastname = last
        self.age = age
        
    '''
    Mi consente di impostare un valore per self.name
    '''
    def set_name(self, name:str ) -> None:
        self.name = name
        
        def __str__(self):
            pass
        
    
    '''
    Mi consente di impostare un valore per self.lastname
    '''
    def set_lastname(self, lastname:str ) -> None:
        self.lastname = lastname
    
    '''
    Mi consente di impostare un valore per self.age
    '''
    def set_age(self, age:int ) -> None:
        if age <0 or age>130:
            self.age = 0
        else:
            self.age = age
    # Mi ritorna il vlaore di self.name
    def getName(self)->str: 
        return self.name
    def getLastName(self) -> str:
        return self.lastname
    def getAge(self) -> int:
        return self.age


# Crea un oggetto di tipo Persona
m:Persona = Persona ("Marco", "Pierleoni", 27)
# Imposta i nomi di una Persona
m.set_name("Marco")

# Imposta i cognomi di una persona 
m.set_lastname("Pierleoni")

# Imposta l'età di una persona 
m.set_age(29)
# Stampa i dati della persona creata
m.display_data()
print("-----------")
print(m.getName(), m.getLastName(), m.getAge())