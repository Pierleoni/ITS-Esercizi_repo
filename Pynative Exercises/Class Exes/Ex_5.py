class Veicolo:
    nome:str
    velocita_max:int
    chilometraggio:int
    
    
    colore:str = 'Bianco'
    
    def __init__(self,  nome, velocita, chilometraggio):
        
        self.nome = nome
        self.velocita_max = velocita
        self.chilometraggio = chilometraggio
    
    def __str__(self):
        return f"Colore: {self.colore} Nome Veicolo: {self.nome} Velocita: {self.velocita_max} Chilometraggio: {self.chilometraggio}"
    


class Bus(Veicolo):
    
    pass
    

class Macchina(Veicolo): 
    pass
    


def main()->None:
    b1:Bus = Bus('School Volvo', 180, 12)
    print(b1)
    
    c1:Macchina = Macchina('Audi Q5', 240, 18)
    print(c1)


if __name__ == '__main__':
    main()