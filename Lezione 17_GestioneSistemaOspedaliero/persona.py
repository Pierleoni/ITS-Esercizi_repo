class Persona:
    __nome:str
    __cognome:str
    __età:int
    
    def __init__(self, first_name, last_name):
        self.setName(first_name)
        self.__cognome = last_name
        self.__età
    
    
    def setName(self, first_name): 
        if isinstance(first_name,str):
            self.__età = 0
        else: 
            self.first_name = None
            self.__età = None 
            return ValueError('Il nome non è una stringa!')
    
    def setLastName(self,last_name): 
        if isinstance(last_name, str): 
            self.__età = 0
        else: 
            self.last_name = None
            self.__età = None