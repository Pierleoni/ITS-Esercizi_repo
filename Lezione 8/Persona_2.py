class Persona:
    def __init__(self, name:str, last:str, age:int):
        self.name = name
        self.lastname = last
        self.age = age
        
    '''
    Mi consente di impostare un valore per self.name
    '''
    def set_name(self, name: str) -> None:
        self.name = name
        
    def __str__(self):
        return f"{self.name} {self.lastname}, {self.age} anni"
        
    '''
    Mi consente di impostare un valore per self.lastname
    '''
    def set_lastname(self, lastname: str) -> None:
        self.lastname = lastname
    
    '''
    Mi consente di impostare un valore per self.age
    '''
    def set_age(self, age: int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
            
    '''
    funzione che mi consente di ritornare il valore di self.Name
    '''
    def getName(self) -> str: 
        return self.name
        
    '''
    funzione che mi consente di ritornare il valore di self.lastname
    '''
    def getLastName(self) -> str:
        return self.lastname
        
    '''
    funzione che mi consente di ritornare il valore di self.age
    '''
    def getAge(self) -> int:
        return self.age
    # Aggiunto metodo display_data che mancava
    def display_data(self) -> None:
        print(f"Nome: {self.name}")
        print(f"Cognome: {self.lastname}")
        print(f"Età: {self.age}") 
        
    def speak(self) -> None:
        print(f"Hello! My name is {self.getName()}")
        



# Crea un oggetto di tipo Persona
m: Persona = Persona("Marco", "Pierleoni", 27)
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