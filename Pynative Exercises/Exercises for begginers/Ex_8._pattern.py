"""
Stampa il seguente pattern

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
# Dichiaro una funzione che prende in input il numero di righe dell pattern che andro a stampare
def print_pattern(rows:int):
    """

    Il numero delle colonne è cruciale per stampare un pattern.
    Per fare ciò si devono utilizzare 2 loops:
    !1)un outer loops; va ad iterare sul numero di righe  
    !2)un loop nestato; va ad iterare sul numero delle colonne per stampare il pattern 
    
    Stampa un pattern numerico con 'rows' righe.
    In ogni riga viene stampato lo stesso numero, ripetuto tante volte
    quanto è l'indice della riga corrente.
    
    Esempio per rows=6:
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    
    """    
    
    #! L'outer loop:  decide quale numero stampare (cioè la riga corrente)
    #! Parte da 0 fino a rows (escluso l'ultimo valore, quindi se rows = 5 stampa fino a 4 righe per 4 colonne)
    # i va da 0 a rows-1   
    for i in range(rows): #utilizzo il metodo range() e come parametro metto il parametro rows
        
        #! Inner loop: decide quante volte stampare i (cioè quante colonne)
        # ! le iterazioni sul numero delle colonne dipende dal valore dell'outer loop
        # Qui va j va da 0 a i-1
        for j in range(i): #difatti come parametro del metodo range metto la variabile 'i' definita nell'outer loop
            
            #! Questo print essendo dentro il loop innestato stampa il numero della riga (i), ripetuto
            print(i, end=' ')
            # Si stampa SEMPRE i(il numero delle riga)
            
            """
            Prima iterazione (i=1)
                Inner loop: j=0 → stampa 1
                Output riga: 1
            Seconda iterazione (i=2)
                Inner loop: j=0 → stampa 2
                Inner loop: j=1 → stampa 2
                Output riga: 2 2
                Terza iterazione (i=3)
                Inner loop: j=0 → stampa 3
                Inner loop: j=1 → stampa 3
                Inner loop: j=2 → stampa 3
                Output riga: 3 3 3
            Quarta iterazione (i=4)
                Stampa 4 per j=0,1,2,3
                Output riga: 4 4 4 4
            Quinta iterazione (i=5)
                Stampa 5 per j=0,1,2,3,4
                Output riga: 5 5 5 5 5
            
            In sintesi:
            per riga i, il numero i viene ripetituto i volte.
            
            QUindi la logica è:
            In ogni riga, stampo lo stesso numero tante volte quanto è il numero della riga
            Esempio: per la riga 3 → stampo 3 3 3
            """              
            
            
        #! Vai a capo dopo aver completato una riga
        print('')


def main():
    print_pattern(6)

if __name__ == "__main__":
    main()