class Pagamento: 
    __importo: float
    def __init__(self, importo_pagamento: float)->None:
        self.setImporto(importo_pagamento)
    
    
    def setImporto(self, importo):
        if isinstance(importo, float):
            self.__importo = importo
        else: 
            raise ValueError('Errore!L\'importo inserito deve essere un numero decimale')
        
    def Importo(self): 
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.__importo:.2f}")


def main()->None:
    p1:Pagamento = Pagamento(20.53)
    print(p1.Importo())
    p1.dettagliPagamento()

if __name__ == "__main__":
    main()

