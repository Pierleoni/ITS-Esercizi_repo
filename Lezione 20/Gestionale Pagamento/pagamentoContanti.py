from __future__ import annotations

from pagamento import Pagamento

class PagamentoContanti(Pagamento):
    def __init__(self, importo_pagamento):
        super().__init__(importo_pagamento)
    
    def dettagliPagamento(self):
        super().dettagliPagamento()
        print(f"Il pagamento in contanti è di: €{self.Importo():.2f}")
    
    def inPezziDa(self):
    # Salvo l'importo del pagamento, arrotondato a 2 decimali.
    # L'arrotondamento serve per evitare errori di precisione con i float
        importo:float = round(self.Importo(), 2)
        
        # Inizializzo una lista di numeri con i diversi tagli delle banconote
        tagli:list[float] = [
            500, 200, 100, 50, 20, 10, 5,
            2, 1,
            0.50, 0.20, 0.10, 0.05, 0.01
        ]
        
        # Itero sugli elementi della lista 'tagli'
        for t in tagli:
            # Calcolo quante banconote o monete di questo taglio posso usare.
            # Uso l'operatore "//" che fa la divisione intera (quoziente senza resto).
            num = int(importo//t)
            
            # Se con questo taglio posso usare almeno 1 banconota/moneta
            if num > 0:
                # Ulteriore check: e se il taglio della banconota è maggiore o ugale a 5
                if t >= 5:
                    
                    # Allora stampo il numero di quante banconote servono e di quale taglio per pagare l'importo
                    print(f"{num} banconota/e da €{t:.2f}")
                else:
                    # In caso contrario, se il taglio della banconota è minore di 5
                    # Stampo il numero dei centesimi che servono e il loro taglio per pagare l'importo
                    print(f"{num} moneta/e da €{t:.2f}")
                
                
                # Aggiorno l'importo rimanente da pagare:
                # tolgo l'importo già coperto moltiplicando il taglio * il numero di pezzi usati.
                # Poi arrotondo nuovamente a 2 decimali per evitare errori con i float.
                importo = round(importo - num * t, 2)

def main()->None:
    pc1:PagamentoContanti = PagamentoContanti(150.00)
    pc1.dettagliPagamento()
    pc1.inPezziDa()
    
    pc2:PagamentoContanti = PagamentoContanti(95.25)
    pc2.dettagliPagamento()
    pc2.inPezziDa()

if __name__ == "__main__":
    main()