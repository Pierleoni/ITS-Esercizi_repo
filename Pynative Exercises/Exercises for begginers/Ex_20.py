"""
Stampa un pattern invertito di numeri
"""

# Definisco una funzione
def rev_pattern(n:int):
    
    #! Outer loop: decide quale numero stampare (cioè la riga corrente)
    # In questo caso per ogni numero su cui si itera nel range che va da 1 a n+1:
    # Quindi parte da 1 e arriva fino a n poichè sommando n+1 si esclude il parametro di stop del metodo range
    
    for i in range (1,n+1):
        #! Inner loop: Determina quante colonne stampare in quella riga
        # Quindi serve a decidere quante volte ripetere il numero i
        """
        In questo caso:
        la forma usata è range(stop) cioè parte da 0 e arriva fino a stop-1,
        quindi il numero di iterazioni = stop.
        In questo caso stop = n-i+1 signfica che:
        !- quando i = 1 → n -1 + 1 = n quindi 1 si ripete n volte 
        !- quando i = 2 → n - 2 + 1 = n-1 quindi il 2 si ripete n-1 volte 
        !- quando i = 3 → n - 3 + 1 = n-2 quindi il 3 si ripete n - 2 volte
        !- ...
        !- quando i = n → n -n +1 = 1 quindi il numero n si ripete 1 volta 
        """  
        # La variabilie '_' viene usata per indicare una variabile non utilizzata(variabile placeholder) 
        for _ in range(n-i+1):
            
            print(i, end=' ')
        print(' ')


def main():
    rev_pattern(5)

if __name__ == "__main__":
    main()