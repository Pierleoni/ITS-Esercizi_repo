from film import Film

class Action(Film):
    __genre:str
    __penale: float
    def __init__(self, id, titolo, genre:str, penale: float):
        super().__init__(id, titolo)
        self.setGenere(genre) 
        self.setPenale(penale)
    
    
    def setGenere(self, genere: str): 
        if isinstance(genere, str): 
            self.__genre = genere
            return True
        else: 
            self.__genre = None
            return False
    
    def getGenere(self):
        return self.__genre
    
    def setPenale(self, penale: float)-> bool:
        if isinstance(penale, float):
            self.__penale = penale
            return True
        else: 
            self.__penale = None
            return False
    
    def getPenale(self)-> float:
        return self.__penale 
    
    
    # Metodo per calcolare l'ammontare della penale
    def calcolaPenaleRitardo(self, days:int)-> float:
        # Salvo in una variabile il prodotto tra il valore della penale e il numero di giorni di ritardo
        tot_penale = self.getPenale()*days
        # Restituisco il prodotto finale e lo passo come arogmento del metodo round()
        # Approsimandolo di 3 decimali dopo la virgola 
        return round(tot_penale, 3)


class Comedy(Film):
    __genre:str
    __penale: float
    def __init__(self, id, titolo, genre:str, penale: float):
        super().__init__(id, titolo)
        self.setGenere(genre) 
        self.setPenale(penale)
    
    
    def setGenere(self, genere: str): 
        if isinstance(genere, str): 
            self.__genre = genere
            return True
        else: 
            self.__genre = None
            return False
    
    def getGenere(self):
        return self.__genre
    
    def setPenale(self, penale: float)-> bool:
        if isinstance(penale, float):
            self.__penale = penale
            return True
        else: 
            self.__penale = None
            return False
    
    def getPenale(self)-> float:
        return self.__penale 
    
    
    # Metodo per calcolare l'ammontare della penale
    def calcolaPenaleRitardo(self, days:int)-> float:
        
        # Salvo in una variabile il prodotto tra il valore della penale e il numero di giorni di ritardo
        tot_penale = self.getPenale()*days
        
        # Restituisco il prodotto finale e lo passo come arogmento del metodo round()
        # Approsimandolo di 3 decimali dopo la virgola
        return round(tot_penale, 3)


class Drama(Film):
    __genre:str
    __penale: float
    def __init__(self, id, titolo, genre:str, penale: float):
        super().__init__(id, titolo)
        self.setGenere(genre) 
        self.setPenale(penale)
    
    
    def setGenere(self, genere: str): 
        if isinstance(genere, str): 
            self.__genre = genere
            return True
        else: 
            self.__genre = None
            return False
    
    def getGenere(self):
        return self.__genre
    
    def setPenale(self, penale: float)-> bool:
        if isinstance(penale, float):
            self.__penale = penale
            return True
        else: 
            self.__penale = None
            return False
    
    def getPenale(self)-> float:
        return self.__penale 
    # Metodo per calcolare l'ammontare della penale
    def calcolaPenaleRitardo(self, days:int)-> float:
        
        # Salvo in una variabile il prodotto tra il valore della penale e il numero di giorni di ritardo
        tot_penale = self.getPenale()*days
        
        # Restituisco il prodotto finale e lo passo come arogmento del metodo round()
        # Approsimandolo di 3 decimali dopo la virgola 
        return round(tot_penale, 3)


def main()->None:
    print('Test per gli oggetti della classe Action')
    a1:Action = Action(4, 'Die Hard', 'Azione', 3.00)
    print(a1.setPenale(3.00))
    print(a1.getPenale())
    print(a1.calcolaPenaleRitardo(3))
    print()
    print('Test per gli oggetti della classe Comedy')
    c1: Comedy = Comedy(6, 'Blues Brothers', 'Commedia', 2.50 )
    print(f'Test per setGenere():{c1.setGenere('Drammatico')}')
    print(f'Test per getGenere():{c1.getGenere()}')
    print(f'Test per setPenale(): {c1.setPenale(2.50)}')
    print(f'Test per getPenale():{c1.getPenale()}')
    print(f'Test per calcolaPenaleRitardo(): {c1.calcolaPenaleRitardo(11)}')
    print()
    print('Test per gli oggetti della classe Drama')
    d1:Drama = Drama (17, 'Brokeback Mountain', 'Drammatico', 2.00)
    print(d1.setGenere('Drammatico'))
    print(d1.getGenere())
    print(d1.setPenale(2.00))
    print(d1.getPenale())
    print(d1.calcolaPenaleRitardo(13))
    

if __name__ == "__main__":
    main()