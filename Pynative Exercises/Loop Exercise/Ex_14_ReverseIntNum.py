"""
Inverti il numero intero
"""
# Definisco una funzione che prende un solo parametro in input
def rev_int_num(n:int)->int:
    # Variabile in cui salvo il numero invertito
    reverse_num:int = 0
    
    # Fin tanto che il numero originale (in input) è maggiore di zero
    while n>0:
        # Estraggo l'ultima cifra e la salvo in una variabile
        digit:int = n%10
        
        # Aggiorno il valore della variabile *10 + l'ultima cifra estratta
        reverse_num = (reverse_num*10) + digit
        
        # Elimino l'ultima cifra dalla variabile num
        n = n//10
    return reverse_num


def main():
    print(rev_int_num(76542))

if __name__ == "__main__":
    main()