from typing import Any
"""
Operazioni basiche su una lista
1. Accedi al terzo elemento e stampalo
2. Stampa la lunghezza della lista
3. Constrolla se la lista è vuota
"""
# Definisco una funzione che prende come parametro una lista di interi
def basic_ops_list(my_list:list[int])->None:
    
    
    # Funzione per accedere al terzo elemento della lista
    def access_ele(my_list:list[int])->None:
        print(f"Terzo elemento: {my_list[2]}")
    
    
    # Funzione che stampa la lunghezza della lista
    def lenght_list(my_list:list[int])->None:
        print(f"Lunghezza della lista: {len(my_list)}")
    
    
    # Funzione per controllare se la lista è vuota
    def check_empty_list(my_list:list[int])->None: 
        
        # Se la lunghezza della lista è diversa da zero
        if len(my_list)!=0: 
            print('la lista non è vuota')
        
        
        else: 
            print('La lista è vuota')


    # Avendo usato lo stack della chiamate: 
    # Richiamo in sequenza le sotto-funzioni, ciascuna con il parametro my_list
    access_ele(my_list.copy())
    lenght_list(my_list.copy())
    check_empty_list(my_list.copy())
    


def main():
    
    # Inzializzo una lista
    lista:list[int] = [10, 20, 30, 40, 50]
    
    # Invoco la funzione principale che a sua volta richiama le sotto-funzioni
    basic_ops_list(lista)
    

if __name__ == "__main__":
    main()