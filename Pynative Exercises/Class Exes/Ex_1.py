class Veicolo:
    max_speed: int
    mileage: float
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    # def __str__(self):
    #     return f"La velocità massima è: {self.max_speed} KmH.\nIl chilometraggio è: {self.mileage}"
    
    

def main()->None:
    v1:Veicolo = Veicolo(20, 400.0)
    print(v1.max_speed, v1.mileage)
    

if __name__ == '__main__':
    main()