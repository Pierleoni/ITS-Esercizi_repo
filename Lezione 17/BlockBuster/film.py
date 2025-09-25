from __future__ import annotations

class Film:
    __id:int
    __titolo:str
    def __init__(self, id:int, titolo:str):
        self.setId(id)
        self.setTitle(titolo)
    
    
    def setId(self, id: int)-> bool:
        if isinstance(id, int):
            self.__id = id 
            return True
        else: 
            self.__id = None
            raise ValueError('Errore! L\'ID inserito deve essere un numero')
    
    def setTitle(self, titolo)-> bool:
        if isinstance(titolo, str):
            self.__titolo = titolo
            return True
        else: 
            self.__titolo = None
            raise ValueError('Errore! Il titolo inserito deve essere una stringa')
    
    
    def ID(self)->int:
        return self.__id
    
    def Title(self)->str:
        return self.__titolo
    
    
    # Metodo che ritorna True se il codice ID di due FIlm è uguale
    def isEqual(self, otherFilm: Film)-> bool:
        # Check: se il valore di self.ID è uguale a al valore otherFilm.ID()
        if self.ID() == otherFilm.ID():
            # Restituisce True
            return True
        else:
            # Altrimenti ritorna False
            return False
    
    """ 
    Il metodo __eq__ compara le istanze della classe (equiparabile all'operatore ==)
    """
    # def __eq__(self, otherFilm: object)-> bool:
    #     # Check: se l'attributo 'otherFilm' non è un istanza di film 
    #         # o i titoli dei film sono uguali 
        
    #     if  isinstance(otherFilm, Film) and self.Title() == otherFilm.Title():
            
    #         # Ritorna False
    #         return False
        
    #     # Altrimenti compara i titoli tra i due oggetti di defualt e restiuisce True se i titoli sono diversi
    #     return self.Title() != otherFilm.Title()



def main()->None:
    f1:Film = Film(0,'Mani Di (S)Burro')
    f2:Film = Film(1,'Alien')
    f3:Film = Film(2,'Predator')
    f4:Film = Film(3,'Mani Di (S)Burro')
    f5:Film = Film(3,'Titanic')
    
    print(f1 == f4)
    print(f1 == f3)
    
    print(f4.isEqual(f5))
    print(f2.isEqual(f3))
    
    print(f1.ID())
    print(f4.ID())
    print(f5.Title())

if __name__ == "__main__":
    main()