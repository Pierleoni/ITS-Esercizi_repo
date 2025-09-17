"""
Stampa una primaide verso il basso fatta di asterischi
"""

# Definisco una funzione
def ast_pyramid(rows:int)->None:
    #! Outer loop: determina quante righe stampare e in quale ordine 
    """
    parte da rows e scende fino a -1 (0 incluso) con 0 step.
    Quindi se rows = 6 i valori di i saranno 6,5,4,3,2,1 
    """    
    for i in range(rows, 0, -1):
        
        #! Inner loop: determina quante colonne (cioè quanti '*') stampare nella riga corrente
        
        """
        Itera da 0 a i-2 incluso, quindi esegue esattamente i-1 iterazioni.
        Quindi: 
        i = 6 stampa 5 asterischi
        i = 5 stampa 4 asterischi
        E cosi via fino a 1 quando i = 2
        """        
        for j in range(0, i - 1):
            
            """
            Stampa un asterisco seguito da uno spazio e non va a capo(end = ' ').
            Quindi ripetendo questa istruzione i-1 volte, si ottiene la riga con
            il numero desiderato di asterischi
            """            
            
            print("*", end=' ')
        
        """
        Chiude la riga corrente andando a capo.
        Qui si stampa anche uno spazio extra prima del newline di defualt del print.
        Nel caso si volesse andare a capo in modo 'pulito', si può usare il semplice print()
        """        
        print()
        


def main():
    ast_pyramid(6)

if __name__ == "__main__":
    main()


