
# Definisco classe Persona
class Persona:
    
    # Attributi privati annotati che inzializzero in seguito nel costruttore tramite i controlli con i setter
    __nome:str
    __cognome:str
    __età:int
    
    
    """Nel costruttore uso i metodi set per il nome e cognome 
    Per assicurarmi che entrambi siano stringhe
    
    """
    def __init__(self, first_name, last_name)->None:
        self.setName(first_name)
        self.setLastName(last_name)
        
        if self.setName(first_name) == True and self.setLastName(last_name) == True:
        
            self.__età = 0
        else:
            self.__età = None
    
    
    # Setter per il nome 
    def setName(self, first_name): 
        
        # Condizione: se first_name è istanza di str()
        if isinstance(first_name,str):
            # salvo l'attributo first_name in __nome
            self.__nome = first_name
            
            return True
            
        else: 
            # Nel caso contrario imposto None per l'età e per il nome
            self.first_name = None
            self.__età = None
            
            # Restiruisco un errore di Value Error
            raise ValueError('Il nome non è una stringa!')
    
    
    # Setter per il cognome
    def setLastName(self,last_name): 
        
        # Condizione: se l'oggetto last_name è istanza di str()
        if isinstance(last_name, str): 
            
            # Salvo l'attributo last_name in __cognome
            self.__cognome = last_name
            
            return True
            
        else: 
            
            # In caso contrario setto last_name e __età a 0
            self.last_name = None
            self.__età = None
            
            # E restituisco un errore di ValueError
            raise ValueError('Il cognome non è una stringa!')
    
    
    # Setter per l'età
    def setAge(self,age):
        
        # Condizione: Se l'oggetto age è istanza di int()
        if isinstance(age, int): 
            # Salvo l'attributo age in __età
            self.__età = age 
        else: 
            
            # Altrimento restituisco un messaggio di errore
            return ValueError('L\'età deve essere un numero intero')
    
    
    # Getter per il nome
    def getName(self): 
        
        # Restiuisco self.__nome
        return self.__nome
    
    
    # Getter per il cognome
    def getLastName(self):
        
        # Restituisco self.__cognome
        return self.__cognome
    
    
    # Getter per l'età
    def getAge(self):
        
        # Restiuisco l'istanza dell'attributo __età
        return self.__età
    
    
    # Definisco metodo greet che ritorna una stringa
    def greet(self)->str:
        # Stampa una f-literal di saluto in cui richiamo i metodi getter della classe Persona per le sue istanze
        print(f"Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni")


def main()->None:
    p:Persona = Persona('Marco', 'Pierleoni')
    print(p.setName('Marco'))
    print(p.setLastName('Pierleoni'))
    p.setAge(26)
    p.greet()
    
    
    
    

if __name__ == "__main__":
    main()
    

