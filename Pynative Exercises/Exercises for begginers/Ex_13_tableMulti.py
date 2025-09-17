"""
Stampa una tabella di moltiplicazioni da 1 a 10
"""
# Dichiaro una funzione 
def multi_table():
    #! Questo loop è l'outer loop: fissa il numero della riga, cioè il moltiplicando 
    # Per i numeri delle righe nel range da 1 a 10 (11 escluso)
    for n in range(1,11):
        
        #! Questo loop è l'inner loop: fissa la colonna, cioè il moltiplicatore
        # Per i numeri delle colonne da 1 a 10 (11 escluso)
        for j in range(1,11):
            
            # Stampa il prodotto tra i numeri delle righe e i numeri delle colonne
            # QUindi in ogni cella della tabella si calcola il prodotto n*j
            """
            Qui la logica è: 
            !In ogni riga, stampo i prodotti tra il numero della riga e tutti i numeri da 1 a 10.
            Esempio: riga 3 → stampo 3*1, 3*2,..., 3*10
            """            
            print(n*j, end=' ')
        
        # Va a capo dopo ogni riga: questo perché il print di default stampa un carattere di newline
        print()
        

"""
La differenza tra questo esercizio è l'esercizio 8 è: 
- Esercizio 8: l'inner loop ripete un numero costante (il numero di riga).
    Difatti l'output è un 'triangolo numerico'
- Esercizio 13: l'inner loop calcola un prodotto diverso a ogni iterazione (dipende dalla riga e dalla colonna).
    Difatti l'output è una tabella con valori variabili
"""

def main():
    multi_table()

if __name__ == "__main__":
    main()