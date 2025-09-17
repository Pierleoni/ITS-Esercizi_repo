"""
Stampa il seguente pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
# Definisco una funzione con un solo parametro in input
def pattern(rows:int):
    
    #! Ciclo esterno: controlla il numero di righe del pattern
    # i va da 0 fino a rows (incluso)
    for i in range(0, rows+1):
        
        #! Ciclo interno: genera i numeri da (rows - i) fino a 1 in ordine decrescente
        for j in range(rows-i,0,-1):
            
            # Stampo il valore di j su una riga, separato da spazi
            print(j, end=' ')
        
        # A fine riga vado a capo
        print(' ')


def main():
    pattern(5)

if __name__ == "__main__":
    main()