class Veicolo:
    nome:str
    max_speed:int 
    mileage:int
    
    def __init__(self, nome, max_speed, mileage):
        self.nome = nome
        self.max_speed = max_speed
        self.mileage = mileage



class Bus(Veicolo):
    def __init__(self, nome, max_speed, mileage):
        super().__init__(nome, max_speed, mileage)


def main()->None:
    b1:Bus = Bus ('School Volvo', 180, 12)
    print(f"Nome veicolo: {b1.nome} Velocità: {b1.max_speed} Chilometraggio: {b1.mileage}")
    

if __name__ == '__main__':
    main()