from persona import Persona



# Creo la classe Dottore che eredità da persona
class Dottore(Persona): 
    
    # Attributi della classe, inizializzati tramite i setter nel costruttore
    specialization: str
    parcel: float
    
    # ostruttore: prende nome, cognome, specializzazione e parcella
    def __init__(self, first_name, last_name, specialization, parcel):
        
        
        # Tramite il metodo super()__init__() eredito il nome e il cognome dalla classe padre
        # e tutta la logica contenuta nel costruttore della classe Persona
        # Difatti posso anche non ridefinire i metodi self.setName e self.LastName in questo costruttore
        super().__init__(first_name, last_name)
        # self.setName(first_name)
        # self.setLastName(last_name)
        
        """ 
        Inzializzo specializzazione e parcella usando i metodi setter per assicurarmi che sono
        rispettivamente una stringa e un float
        """
        
        self.setSpecialization(specialization)
        self.setParcel(parcel)
        
        
        
        
    
    # Metodo setter per la specializzazione
    def setSpecialization(self, specialization)->bool: 
        # Check: se la specializzazione è una istanza di stringa 
        if isinstance(specialization, str):
            
            # salvo l'attributo specialization nella variabile annotata a monte della classe
            self.specialization = specialization
            
            # e retituisco True
            return True
        else: 
            
            # Altrimenti setto la variabile specialization come None
            self.specialization = None
            
            # E sollevo un errore di valore
            raise ValueError('La specializzazione inserita non è una stringa!')
    
    
    
    # Metodo setter per la parcella
    def setParcel(self, parcella): 
        
        # Check: se parcella è istanza di float 
        if isinstance(parcella, float): 
            
            # Salvo il valore dell'attributo parcella nella variabile parcel annotata a monte
            self.parcel = parcella
            
            # E restituisco True
            return True
        else: 
            
            # Altrimenti setto la variabile parcel a None
            self.parcel = None
            
            # E sollevo un errore di ValueError
            raise ValueError ('La parcella inserita non è un float!')
    
    
    
    # Metodo getter per restituire il valore dell'attributo specialization in sola lettura
    def getSpecialization(self): 
        return self.specialization
    
    
    # Metodo getter per restituire il valore dell'attributo parcel in sola lettura 
    def getParcel(self): 
        return self.parcel
    
    
    
    # Metodo per verificare la validità del dottore
    def isAValidDoctor(self): 
        
        
        # richiamo il metodo getAge() definito nella classe padre
        # Check: se il valore dell'età è maggiore di 30
        if self.getAge() > 30: 
            
            # Stampo messaggio per dire che il dottore è valido
            # richiamo i getter di name e lastname definiti nella classe padre poichè gli attributi nome e congnome in Persona sono privati
            print(f"Il Dottore {self.getName()} {self.getLastName()} è un dottore valido")
            return True
        
        
        else: 
            # Altrimenti stampo il messaggio per dire che il dottore non è valido 
            # uso i getter di name e lastname definiti nella classe padre poichè gli attributi nome e congnome in Persona sono privati
            print(f"Il Dottore {self.getName()} {self.getLastName()} non è un dottore valido")
            return False
    
    
    # Metodo per stampare un messaggio di saluto
    def doctor_greet(self):
        
        # Richiamo il metodo greet() definito nella classe Persona con dentro la sua logia
        super().greet()
        
        # Stampo un messaggio di saluto
        print(f"Sono un medico {self.specialization}")



def main()->None:
    doc:Dottore = Dottore('Antonio', 'Marchetti', 'Odontoiatra', 450.000)
    print(doc.setSpecialization('Odontoiatra'))
    print(doc.getSpecialization())
    print(doc.getParcel())
    doc.setAge(31)
    doc.isAValidDoctor()
    doc.doctor_greet()
    

if __name__ == "__main__":
    main()