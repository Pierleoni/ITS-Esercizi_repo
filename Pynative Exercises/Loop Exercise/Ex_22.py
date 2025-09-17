"""
Trova la cifra numerica più alta e più piccolo in un numero
"""


# Definisco una funzione che prende in input un numero intero
# e restituisce una tupla con la cifra più grande e quella più piccola
def high_small_digit(n:int)->tuple[int,int]:
    
    # prendo il valore assoluto del numero in input(ignoro il segno), lo converto in una stringa e lo salvo in una variabile
    absolute_val:str = str(abs(n))
    
    
    # Inizializzo sia la cifra più grande che quella più piccola con la prima cifra del numero
    largest_val:int = int(absolute_val[0])
    smallest_val:int = int(absolute_val[0])
    
    # Itero sulle cifre rimanenti della stringa (dal secondo carattere in poi)
    for chars in absolute_val[1:]:
        
        # Uso il type casting per convertire il carattere corrente in numero intero
        convert_int:int = int(chars)
        
        # Se la cifra corrente è maggiore della più grande trovata finora,
        # aggiorno largest_val
        if convert_int >largest_val:
            
            # Allora largest_val è uguale a convert_int
            largest_val = convert_int
            
        # Se la cifra corrente è minore della più piccola trovata finora,
        # aggiorno smallest_val
        if convert_int<smallest_val:
            
            # 
            smallest_val = convert_int
        
    # Ritorna i due valori di largest_val e smallest_val come tupla
    return largest_val, smallest_val


def main():
    print(high_small_digit(987654321))
    print(high_small_digit(-50234))

if __name__ == "__main__":
    main()
