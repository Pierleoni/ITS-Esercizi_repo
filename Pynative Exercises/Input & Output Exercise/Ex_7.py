"""
Accetta 3 stringhe da una sola chiamata del metodo input()
"""

"""
Questo viene detto unpacking: 
unpacking significa “spacchettare” gli elementi di una sequenza (lista, tupla, stringa, ecc.) 
e assegnarli a più variabili contemporaneamente.

È l’operazione opposta al “packing” (impacchettare elementi in una lista o tupla).


Come funziona: 
!1. input('Digita 3 stringhe: ') → prende una stringa dall’utente.
Esempio: Marco Rossi 25.

!2. '.split()' → divide la stringa in una lista di sottostringhe separandole sugli spazi.
Risultato: ["Marco", "Rossi", "25"].

!3. nome, cognome, eta = ... → assegna automaticamente ogni elemento della lista a una variabile (unpacking).

    nome = "Marco"

    cognome = "Rossi"

    eta = "25"

!4. Infine, la print usa un f-string per mostrare i valori.

"""

def one_call():
    
    nome, cognome, eta = input('Digita 3 stringhe: ').split()
    print('\n')
    print(f'Dettagli dell\' utente: {nome}, {cognome}, {eta}')
    



def main():
    one_call()

if __name__ == "__main__":
    main()