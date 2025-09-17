class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)
    
    
    # Per le istanze di Bus bisogna aggiungere un 10% alla tariffa totale. 
    # Di conseguenza la tariffa totale di un istanza di Bus dovra essere l'ammontare finale,
    # calcolato come tariffa totale + 10% della tariffa totale 
    
    def fare(self):
        # Ridefinisco il metodo fare() in bus tramite l'overriding 
        """
        amount contiene il valore restituito dal metodo fare() 
        della classe padre (Vehicle), cioè la tariffa base.
        """
        amount = super().fare()
        # Per far si di aggiungere il 10% alla tariffa totale dobbiamo sommare l'amount con se stesso
        # E per applicare il 10% moltplicarlo per 10/100
        amount += amount *10/100
        
        # In Output ritorna la varaibile amount
        return amount


def main():
    v1:Vehicle = Vehicle('Macchina', 12, 4)
    print(v1.name, v1.capacity, v1.mileage)
    print(v1.fare())
    
    
    b1:Bus = Bus ('School Volvo', 180, 50)
    print(b1.name, b1.capacity, b1.mileage)
    print(f"Total bus fare is: {b1.fare()}")


if __name__ == '__main__':
    main()