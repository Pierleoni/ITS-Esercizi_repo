#Definisco una classe
class Persona:
    '''
    Di una prsona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe Persona).
    Le informazioni sono:
    - nome della persona
    - cognome della persona
    - età della persona.
    Un volta definita una classe dobbiamo definire il costruttore della classe: costruisce una variabile di tipo classe; 
    es: se io ho una classe PErsona il costruttore permettere di costruire una variabile di tipo persona che in questo caso deve avere un nome, cognome ed età.
    Come rappresento gli attributi in Python?
    self.name:str (attributo di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (Attributo di tipo int)
    '''
    
    
    
    '''
    il metodo init è un costruttore ma funziona come una funzione
    '''
    # Costruttore della classe Persona
    '''
    il self permette di  
    '''
    def __init__(self, name:str, lastname:str, age:int ) : #Definisco gli attributi della classe
        # Inizializzo gli attributi
        '''
        Il self mi sta dicendo che quella variabile name appartiene alla classe Persona e di conseguenza, 
        posso inizializzare una variabile di tipo Persona passandogli una stringa generica.
        Il self si riferisce alla classe che noi stiamo implementando, in questo caso la classe Persona.
        '''
        self.name:str = name
        self.lastname:str = lastname
        self.age:int = age 
    # Funzione che mostri in output tutti i dati di una persona 
    def display_data(self): #Indica che questa funzione appartiene alla classe Persona
        print(f"Nome: {self.name}\nCognome: {self.lastname} \nEtà: {self.age}") #Output: mi stampa i valori passati come arogmenti nell'istanza della classe

'''
Sto instanziando un oggetto di tipo Persona, 
cioè sto creando un oggetto di tipo Persona, 
difatti m può essere chiamato oggetto della classe Persona o istanza della classe Persona
'''

m:Persona = Persona("Marco", "Pierleoni", 26)
print(m) # Output: <__main__.Persona object at 0x0000023EE89F5E50>, stampa la posizione in memoria

# Richiamo la funzione display_data per mostrare i dati di una persona 
m.display_data()
'''
print(f"Nome: {self.name}\nCognome: {self.lastname} \nEtà: {self.age}")
Per stampare gli attibruti devo richiamre attributo per attributo nel print, 
se voglio accedere algi attributi tutti insieme fare riferimento alla funzione display_dat
'''