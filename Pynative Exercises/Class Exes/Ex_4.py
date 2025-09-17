class Veicolo:
    nome:str
    velocita:int
    chilometraggio:int
    
    def __init__(self, nome:str, velocita:int, chilometraggio:int):
        self.nome = nome
        self.velocita = velocita
        self.chilometraggio = chilometraggio
    
    def num_sedili(self, capacita):
        return f"Il numero di sedili di un {self.nome} è di {capacita} passegeri" 
    


class Bus(Veicolo):
    def __init__(self, nome, velocita, chilometraggio):
        super().__init__(nome, velocita, chilometraggio)
    
    def num_sedili(self, capacita = 50):
        return super().num_sedili(capacita)
    
    

def main()->None:
    b1:Bus = Bus('bus', 180, 20)
    print(b1.num_sedili())

if __name__ == '__main__':
    main()