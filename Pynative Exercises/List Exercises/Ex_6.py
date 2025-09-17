"""
Trova il massimo e il minimo degli elementi della lista
"""

def max_min(numbers: list[int])->None:
    print(f"Lista originaria: {numbers}")

    print(f"Il numero più grande: {max(numbers)}\nIl numero più piccolo: {min(numbers)}")
    
    # Definisco sotto funzione che prende una lista di interi in input
    def for_max_min(numbers: list[int])->None:
        # Inializzo il numero più grande e più piccolo come primo elemento della lista
        largest_digit:int = numbers[0]
        smallest_digit:int = numbers[0]
        
        # Itero sulle cifre della lista a partire dal secondo elemento
        for num in numbers[1:]: 
            
            # Check: se il numero è maggiore del primo elemento
            if num>largest_digit:
                
                # Aggiorno il valore di largest_num con il valore di num
                largest_digit = num
            
            # Check: se il numero è minore del primo elemento
            if num<smallest_digit:
                
                # Aggiorno il valore di smallest_num con il valore di num
                smallest_digit = num
                
                
        # Stampo l'elemento più grande e più piccolo della lista
        print(f"Il numero più grande usando il for loop: {largest_digit}")
        print(f"Il numero più piccolo usando il for loop: {smallest_digit}")
    
    
    for_max_min(numbers)

def main()->None:
    max_min([8, 2, 15, 1, 9])

if __name__ == "__main__":
    main()