"""
Visualizza i numeri da una lista usando un loop secondo i seguenti criteri:
- il numero deve essere divisibile per 5
- se il numero è maggiore di 150 allora saltalo e vai al prossimo numero
- Se il numero è maggiore di 500, interrompi il ciclo
"""
# Definisco una funzione che accetta in input una lista di numeri interi
def display_nums(num_list:list[int])->int|list[int]: 
    # Inzializzo una lista vuota (non richiesto dall'esercizio originale)
    new_list:list[int] = list()
    
    # Itero sui singolo elementi della lista in input
    for numbers in num_list: 
        # Se l'elemento è divisibile per 5 e minore o uguale a 150
        if numbers % 5==0 and numbers<=150:
            # Stampo l'elemento
            print(numbers)
            
            # e appendo i singoli elementi alla lista vuota
            new_list.append(numbers)
        
        # Altrimenti se il numero è maggiore di 500
        elif numbers>500:
            # Esco dal ciclo
            break
    
    # Stampo il risultato della lista vuota con gli elementi appessi
    print(new_list)

def main():
    display_nums([12, 75, 150, 180, 145, 525, 50])

if __name__ == "__main__":
    main()