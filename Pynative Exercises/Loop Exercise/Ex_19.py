"""
Stampa la tabella di moltiplicazione per i numeri da 1 fino a 10
"""
# Definisco una funzione che prende in input un solo parametro
def multi_table(n:int)->None:
    
    # Outer Loop: controlla quale numero (da 1 a n) useremo come base della tabellina
    for i in range(1,n+1):
        
        
        print(f"\nTabella di moltiplicazione di: {i}")
        
        # Inner Loop: calcola i prodotti di i con tutti i valori da 1 a n
        for j in range(1,n+1):
            # Stampo il risultato della moltiplicazione i * j sulla stessa riga
            print(f"{i*j}", end=' ')
        # Dopo aver stampato tutti i valori della riga, vado a capo
        print()


def main():
    multi_table(10)

if __name__ == "__main__":
    main()
