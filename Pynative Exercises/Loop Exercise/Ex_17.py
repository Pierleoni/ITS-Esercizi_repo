"""
Trovare la somma di una serie di un numero fino a n termini
"""

# Definisco una funzione che prende in input 2 parametri (il numero e la serie)
def terms(n:int, terms:int)->int:
    # Inizializzo a zero la variabile in cui salverò la somma della serie
    somma:int = 0
    
    # Itero sui numeri da zero fino al parametro terms
    for _ in range(0,terms):
        
        
        # Aggiorno la variabile somma 
        somma+=n
        
        # Aggiorno il parametro n
        n=(n*10)+2
        
        # Stampo la serie di n 
        print(n, end=' ')
    print(f"\nLa somma della serie sopra è: {somma}")

def main():
    terms(2,5)

if __name__ == "__main__":
    main()
