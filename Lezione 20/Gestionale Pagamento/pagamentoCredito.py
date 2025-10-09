from pagamento import Pagamento
from datetime import date
class PagamentoCartaDiCredito(Pagamento):
    nome_titolare:str
    data_scadenza:date
    credit_number:int 
    def __init__(self, importo_pagamento, nome:str, data:date, num_credit:int):
        super().__init__(importo_pagamento)
        self.setNome(nome)
        self.setData(data)
        self.setNumero_carta(num_credit)
        
        
    
    def setNome(self, nome:str):
        if isinstance(nome, str): 
            self.nome_titolare = nome
        else: 
            raise ValueError('Errore!')
    
    def Nome(self): 
        return self.nome_titolare
    
    def setData(self, data:date): 
        if isinstance(data, date):
            self.data_scadenza = data
        else:
            raise ValueError('Errore!')
    
    def Data(self):
        return self.data_scadenza
    
    def setNumero_carta(self, numero_carta:int):
        if isinstance(numero_carta, int):
            self.credit_number = numero_carta
        else: 
            raise ValueError('Errore!')
    
    def NumeroCarta(self):
        return self.credit_number
    
    
    def dettagliPagamento(self):
        # Richiamo il metodo dettagliPagamento della classe padre con super()
        # per stampare l'importo del pagamento (già definito in Pagamento).
        
        # Poi stampo le informazioni specifiche della carta di credito:
            # 1) Nome del titolare → richiamato tramite il metodo get Nome().
            # 2) Data di scadenza → estraggo mese e anno dall'attributo di tipo date.
        
        # Per il mese uso la formattazione ':02d':
            #! - '02' indica che il numero deve avere almeno 2 cifre.
            #! - se il mese è a una cifra (es. 1 → gennaio), viene formattato come '01'.
            #! - se il mese è già a due cifre (es. 11 → novembre), resta invariato.
            #! - 'd' indica che si tratta di un intero (decimal).
        
        # Per l'anno faccio typecasting da int a string,
        # e con lo slicing [2:] estraggo solo le ultime due cifre
        # (es. '2024' diventa '24').
        super().dettagliPagamento()
        print(f"Nome sulla carta: {self.Nome()}  \
        \nData di scadenza: {self.Data().month:02d}/{str(self.Data().year)[2:]}  \
        \nNumero della carta: {self.NumeroCarta()}")


def main()->None:
    
    
    scadenza = date(2024, 12, 24)
    pcr:PagamentoCartaDiCredito = PagamentoCartaDiCredito(200.00, 'Mario Rossi', scadenza, 1234567890123456 )
    pcr.dettagliPagamento()

if __name__ == "__main__":
    main()