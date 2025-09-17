"""
Controlla se il numero è un palindromo
"""

# Primo approccio:
# Definisco una funzione senza parametro
def palindrome1()->int:
    
    # Variabile per fare inserire il numero dall'utente
    number:int = int(input('Enter a number: '))
    
    
    # Converto la variabile number in una stringa e salvo il valore in una variabile
    str_number:str = str(number)
    
    # Check: se il il primo carattere è ugaule all'ultimo carattere della stringa
    if str_number[0::] == str_number[::-1]:
        # Stampa il numero con un f-literal e converte la stringa in un integer
        print(f'Si, il numero {int(str_number)} è un palindromo.')
    
    # Altrimenti se la prima condizione non è verificata
    else: 
        
        # Stampa il numero che non è un palindromo e lo converte in un integer
        print(f"No, il numero {int(str_number)} non è un palindromo.")



# Secondo approccio:

def palindrome2(number)->bool:
    # Salvo il valore di number in un altra variabile
    original_num = number
    reverse_num:int = 0
    
    # Il ciclo continua finche number non diventa 0
    while number >0:
        # Restituisce il resto della divisione per 10, cioè l'ultima cifra del numero
        # Quindi se number = 123, allora reminder = 3
        reminder = number % 10
        
        # Serve per costruire il numero inverso:
        """
        !1) (reverse_num*10): sposta le cifre già trovate di una posizione a sinistra
        !2) +reminder: aggiunge l'ultima cifra del numero 
        ESEMPIO:
        all’inizio reverse_num = 0
        prendi 3 → reverse_num = 0*10 + 3 = 3
        prendi 2 → reverse_num = 3*10 + 2 = 32
        prendi 1 → reverse_num = 32*10 + 1 = 321.
        """        
        reverse_num = (reverse_num * 10) + reminder
        
        # L'operatore //10 fa una divisione intera eliminando l'ultima cifra
        # ESEMPIO: 123 // 10 = 12
        number = number // 10
    
    # Check: se il numero originale è uguale al numero inverso
    if original_num == reverse_num:
        print(True) #Stampa True
    
    else: 
        print(False) #Stampa False


def main():
    # palindrome1()
    palindrome2(121)
    palindrome2(125)

if __name__ == "__main__":
    main()