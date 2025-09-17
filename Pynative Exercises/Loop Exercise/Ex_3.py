"""
Calcola la somma di tutti i numeri da 1 al numero dato dall'utente
"""
# Definisco una funzione che prende un parametro in input
def calc(n:int)->str:
    # Inzializzo una variabile somma dove andare a salvare il risultato della somma dei numeri naturali da 1 a n
    somma = 0
    # itero sui singoli numeri a partire da 1 fino a n+1 (cosi da sommare anche l'estremo di n), con lo step = 1
    for i in range(1,n+1,1):
        # salvo nella variabile 'somma' l'addizione iterativa tra somma + i
        somma:int = somma + i
    # Stampo la stringa formatta 
    print(f"La somma dei numeri naturali da 1 a {n} è : {somma}")


number:int = int(input('Enter a number: '))

def main():
    calc(number)

if __name__ == "__main__":
    main()