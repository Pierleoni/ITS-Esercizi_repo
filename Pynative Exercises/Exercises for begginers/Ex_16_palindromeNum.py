"""
Controlla il numero palindromo
"""

def palindromo(number:int)->bool:
    # Salvo il numero originale per poterlo confrontare a fine ciclo
    original = number
    # Inzializzo variabile rev che andrà a contenere il numero invertito
    rev:int = 0
    
    # Fint tanto che il parametro number è maggiore di 0...
    while number >0:
        
        # Inzializzo variabile che serve per estrarre l'ultima cifra del numero (modulo 10)
        digit = number %10 
        # Aggiorno il numero invertito, ad ogni iterazione moltiplico rev per 10 e aggiungo la cifra estratta
        rev = (rev*10)+ digit 
        
        # Aggiorno la variabile number tramite la divisione per 10 del numero
        # In questo rimuovo l'ultima cifra dal numero
        number = number//10
        
    # Confronto il numero originale con quello invertito
    return original == rev
    
    


def main():
    print(palindromo(121))
    print(palindromo(5005))
    print(palindromo(123))

if __name__ == "__main__":
    main()