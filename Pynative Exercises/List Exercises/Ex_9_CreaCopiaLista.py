"""
Crea una copia della lista e modificala.
Stampa l'originale e la copia per dimostrare che sono indipendenti 
"""

import copy

# Definisco funzione principale che prende una lista di interi in input
def create_copyList(numbers:list[int])->None:
    print(f"Lista originaria: {numbers}")
    
    # 1 metodo: creo una copia usando lo slicing
    # Definisco una sotto-funzione che prende come parametro una lista di interi
    # Questa lista in input ha un altro nome per evitare ambiguita, facilitare il debugging ed evitare l'oscuramento(shadowing)
    def slicing_method(lst: list[int])->None:
        
        # Inzializzo un altra lista in cui salvo la shallow copy della lista originaria della funzione
        copied_list:list[int] = lst[:] #lo slicing crea una shallow copy della lista originaria
        
        # Alla nuova lista appendo il numero 40
        copied_list.append(40)
        # Modifico il primo elemento con il numero 100
        copied_list[0] = 100
        
        # Stampo la lista originaria e la sua copia per dimostrare che sono due liste apparte
        print(f"\nUsando lo slicing - Copia modificata: {copied_list}")
        print(f"Usando lo slicing - Originale: {lst}")
    
    
    # 2 metodo: uso il list constructor (list())
    def list_constructor(lst2: list[int])->None:
        # Creo una copia della lista in input tramite il list() constructor
        new_numbers:list[int] = list(lst2) #shallow copy con il costrruttore
        
        # Appendo il numero 50 alla copia 
        new_numbers.append(50)
        
        # Stampo la lista originaria e la sua copia per dimostrare che sono due liste apparte
        print(f"\nUsando il list constructor - Copia modificata: {new_numbers}")
        print(f"Usando il list constructor - Originale: {lst2}")
    
    
    # 3 metodo: con il metodo copy()
    def copy_method(lst3: list[int])->None:
        
        # Inizializzo una nuova lista in cui salvo la copia della lista in input tramite il metodo .copy()
        new_list:list[int] = lst3.copy() #Shallow copy con il metodo .copy()
        
        # Modifico il primo elemento della copia con il numero 99
        new_list[0] = 99
        
        # Stampo la lista originaria e la sua copia per dimostrare che sono due liste apparte
        print(f"\nUsando copy() - Copia modificata: {new_list}")
        print(f"Usando copy() - Originale: {lst3}") 
    
    # Eseguo tutti i diversi metodi di copia 
    slicing_method(numbers)
    list_constructor(numbers)
    copy_method(numbers)
    
    # Vado accapo
    print()
    
    # Dimostro l'immutabilità della lista originaria 
    print(f"Lista originaria finale: {numbers}")


def main()->None:
    create_copyList([10, 20, 30])

if __name__ == "__main__":
    main()