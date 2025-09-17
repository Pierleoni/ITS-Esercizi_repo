class Veicolo:
    name:str
    chilometraggio:int 
    capacita:int 
    def __init__(self, nome, chilomettraggio, capacita):
        self.nome = nome
        self.chilometraggio = chilomettraggio
        self.capacita = capacita
    

class Bus(Veicolo):
    pass

def main():
    school_bus:Bus = Bus ('School Volvo', 12, 50)
    print(isinstance(school_bus, Veicolo))

if __name__ == "__main__":
    main()