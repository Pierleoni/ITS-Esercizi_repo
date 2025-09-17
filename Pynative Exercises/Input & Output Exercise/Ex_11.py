"""
Prendi in input dall'utente due numeri e calcola la percentuale e visualizzala
con 2 decimali seguiti da un segno di percentuale
"""

# Definisco una funzione che accetta due parametri numerici
def percentuale(numeratore:float|int, denominatore:float|int)-> float: 
    
    #  Calcolo la percentuale: (numeratore ÷ denominatore) × 100
    res = (numeratore/denominatore)*100
    # :.2f formatta il numero a 2 cifre decimali
    print(f"La percentuale è :{res:.2f}%")



"""
Acquisisco i valori dall'utente con input(), al di fuori della funzione.
Questo approccio aumenta la riusabilità della funzione, 
che resta indipendente dalla modalità di acquisizione dei dati.

Gestisco inoltre i possibili errori con un blocco try-except:
- ValueError se l'utente inserisce un valore non numerico.
- ZeroDivisionError se il denominatore è uguale a zero.
"""
try:
    
    n1:float = float(input("Inserisci il numeratore: "))
    n2: float = float (input("Inserisci il denominatore: "))
    
    if n2 == 0: 
        
        raise ZeroDivisionError ('Il denominatore non può essere zero!')

except ValueError: 
    print ("Input non valido")



def main():
    percentuale(n1, n2)

if __name__ == "__main__":
    main()
