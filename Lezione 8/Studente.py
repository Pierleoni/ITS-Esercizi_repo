# Importo dal file Persona_2 importo la classe Persona 
from Persona_2 import Persona 
class Studente(Persona):
    '''
    Attributi della classe Persona(in quanto Studente è una Persona)
    self.name:str
    self.lastname:str
    self.age:int
    
    Attributi della calsse Studente
    slef.matricola:str
    '''
    # Init prende in input name, last, age(un intero) e matricola che è una stringa
    def __init__(self, name:str, last:str, age:int, matricola:str):
        # devo inizializzare una classe Persona perchè uno studente è una persona
        # la finzione super permette di ereditare gli attributi della classe Padre(Persona)
        # Quindi quando ho a che fare con le ereditarietà devo prima di scrivere init devo inizializzare la classe Persona richiamando il emtodo init della classe Padre
        # Quindi per inizializare la classe Persona nella classe Studente ho bisongo di un nome,cognome ed età
        super().__init__(name, last, age)
        # istruzioni che inizilizano uno oggetto della classe Studente
        self.setmatricola(matricola)
        # metodo che imopsta il valore dell'attributo self.matricola
        def setMatricola(self, matricola:str)->None:
            if matricola:
                self.matricola = matricola
            else:
                print("Errore!La matricola non può essere rappresentata da una stringa vuota")
        # Scriviamo il corrispetiovo metodo getter che ritorna il vlaore dell'attributo self.matricola
        def getMatricola(self) -> str:
            return self.matricola
        def __str__(self)->str:
            return f"\nNome: {self.name}. \nCognome: {self.getlast()}.\nMatricola: {self.getMatricola()}"
        

'''
ovverridding: 
ridefinisco il metodo str, ridefinaimo il metodo str della classe studente quindi quando printo l'oggetto di studente stampo le informazioni della classe Studente


'''
