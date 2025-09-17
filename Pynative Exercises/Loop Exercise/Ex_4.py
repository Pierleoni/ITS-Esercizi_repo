"""
Stampa la tabella della moltiplicazione del numero dato dall'utente
"""
# Definisco una funzione che prende in input un parametro int
def multi(n:int):
    # Variabile che conterrà di volta in volta il risultato della moltiplicazione
    res:int = 0
    
    # Itero i da 1 a 10 (incluso)
    for i in range(1, 10+1, 1): 
        
        # Calcolo la moltiplicazione tra 'n' e 'i' e la salvo in 'res'
        res = n*i
        
        # Stampo il risultato 
        print(res)

num:int = int(input('Digita il numero per calcolare la tabellina: '))

def main():
    multi(num)

if __name__ == "__main__":
    main()