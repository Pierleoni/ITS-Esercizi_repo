class Veicolo: 
    nome:str
    chilometraggio:int 
    capacita:int 
    def __init__(self, nome, chilomettraggio, capacita):
        self.nome = nome 
        self.chilometraggio = chilomettraggio
        self.capacita = capacita

class Bus(Veicolo):
    pass 

def main()->None:
    school_bus:Bus = Bus('School Volvo', 12, 50)
    print(type(school_bus))
    




if __name__ == '__main__':
    main()