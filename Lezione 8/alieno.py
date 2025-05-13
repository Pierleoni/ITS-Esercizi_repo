class Alieno:
    '''
    Di un alieno ci interessa di sapere la galassia di provenienza:
    avremo un attributo di tipo self.galaxy:str
    avremo anche un init che ci consente di inizializzare un oggetto della classe alieno
    il self.setGalaxy serve per impostare il vlaore di galaxy sia un vlaore valido
    '''
    
    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)
        
    '''
    definire un metodo per impostare il valore dell'attributo self.galaxy
    '''
    def setGalaxy(self, galaxy:str)->None:
        if galaxy:
            self.galaxy=galaxy
        else:
            print("Errore! La galassia non può essere una stringa vuota")
    '''
    definire un metodo per restituire il valore dell'attributo self.galaxy
    '''
    def getGalaxy(self) ->str:
        return self.galaxy
    '''
    definire un metodo speak(), come l'abbiamo chiamato nella classe persona
    non ritorna nulla perchè stampa in output il messaggio
    '''
    def speak(self)->None:
        print("hfdhfdjhfjhdfdfidshfdjkfh")
    def __str__(self)->str:
        return f"Alieno proveniente dalla galassia {self.getGalaxy()}"