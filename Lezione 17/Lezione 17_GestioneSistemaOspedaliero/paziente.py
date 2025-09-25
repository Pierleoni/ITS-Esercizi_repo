from persona import Persona

class Paziente(Persona):
    __idCode:str
    
    def __init__(self,first_name, last_name, idCode: str):
        super().__init__(first_name, last_name)
        self.setIdCode(idCode)
        
        
        
    def setIdCode(self,idCode: str):
        if isinstance(idCode, str):
            self.__idCode = idCode
            return True
        else: 
            self.__idCode = None
            raise ValueError('Errore! L\'ID inserito non è una stringa')
        
    
    def getIdCode(self):
        return self.__idCode
    
    
    def patientInfo(self)->str:
        print(f"Paziente: {self.getName()} {self.getLastName()}\nID: {self.getIdCode()}")
        
    def __str__(self):
        return f"{self.getName()} {self.getLastName()} {self.getIdCode()}"
    def __repr__(self):
        return f"{self.getName()} {self.getLastName()} {self.getIdCode()}"



def main()->None:
    pax:Paziente = Paziente('Giovanni', 'Storti','123AB04')
    print(pax.getName())
    print(pax.getLastName())
    print(pax.getIdCode())
    print(pax.setIdCode('231BJ25'))
    # print(pax.setIdCode(True))
    # print(pax.setIdCode(5))
    pax.patientInfo()
    
    

if __name__ == "__main__":
    main()