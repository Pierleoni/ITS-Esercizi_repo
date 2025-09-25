from __future__ import annotations

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
from dottore import Dottore
from paziente import Paziente


class Fattura(): 
    pazienti: list[Paziente]
    dottore:Dottore
    fatture: int
    salary:int
    
    def __init__(self, paxs: list[Paziente],doc:Dottore, fattura:int, salario:int)->None:
        self.dottore = doc
        self.pazienti = paxs
        self.fatture = fattura
        self.salary = salario
        
        
        if self.dottore.isAValidDoctor(): 
            self.fatture = len(self.pazienti)
            self.salary = 0
        else: 
            print('Non è possibile creare la classe fattura poichè il dottore non è valido!')
    
    def getSalary(self)-> int:
        self.salary = self.dottore.parcel *len(self.pazienti)
        return self.salary
    
    
    def getFatture(self)-> int: 
        self.fatture = len(self.pazienti)
        return self.fatture
    
    
    def addPatient(self,new_patient:Paziente)->str: 
        
        self.pazienti.append(new_patient)
        self.getFatture()
        self.getSalary()
        
        print(f"Alla lista del dottore {self.dottore.getLastName()} è stato aggiunto il paziente {new_patient.getIdCode()}")
        
    
    
    # Metodo per rimuovere un paziente dalla lista 
    def removePatient(self, idCode: str)-> str: 
        # Itero sui singoli elementi della lista pazienti
        for paziente in self.pazienti: 
            # Check : richiamo il metodo get della lista paziente che restiuisce il codice del paziente
            # Se il codice identificativo è uguale al codice in input del metodo
            if paziente.getIdCode()==idCode: 
                
                # Rimuovo il paziente dalla lista
                self.pazienti.remove(paziente)
                # Richiamo i metodi get per la fattura e il salario 
                self.getFatture()
                self.getSalary()
                print (f"Alla lista Dottore {self.dottore.getLastName()} è stato rimosso il paziente {idCode}")
                # Il return in questo caso permette di interropmere il ciclo: 
                # il return di defualt torna None, di conseguenza quando python lo trova dentro un ciclo interropme automaticamente il flusso ed esce fuori dal ciclo
                return



def main()->None:
    doc1: Dottore = Dottore('Marina', 'Massironi', 'Medico Base', 450.00)
    doc2: Dottore = Dottore ('Roberto', 'Provenzano', 'Chirurgo', 600.00)
    
    pax:Paziente = Paziente ('Aldo', 'Baglio', '1236ABC4')
    pax1:Paziente = Paziente ('Giovanni', 'Storti', '2567DJF2')
    pax2:Paziente = Paziente ('Giacomo', 'Poretti', '4591SFK3')
    
    lista_paz1:list[Paziente] = [pax, pax1, pax2]
    paz:Paziente = Paziente ('Andrea', 'Pazienza', '5698ERT0')
    lista_paz2:list[Paziente] = [paz]
    
    doc1.setAge(50)
    doc2.setAge(69)
    doc1.doctor_greet()
    doc2.doctor_greet()
    
    
    
    fatt: Fattura = Fattura(lista_paz1, doc1, 4000, 2500 )
    fatt2:Fattura = Fattura(lista_paz2, doc2, 3500, 3700)
    print(f"Salario Dottore1: {fatt.getSalary()}euro!")
    print(f"Salario Dottore2: {fatt2.getSalary()}euro!")
    
    fatt.removePatient('4591SFK3')
    fatt2.addPatient(pax2)
    tot:int = fatt.getFatture() + fatt2.getFatture()
    print(f"In totale, l'ospedale ha incassato: {tot} euro!")
    

if __name__ == "__main__":
    main()