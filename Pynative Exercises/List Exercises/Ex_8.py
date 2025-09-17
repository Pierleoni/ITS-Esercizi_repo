"""
Ordina una lista di numeri
"""

def sort_list(numbers:list[int])->None:
    print(f"Lista originaria: {numbers}")
    def sorted_method(numbers:list[int])->None:
        lista:list[int] = sorted(numbers) #Crea una lista ordinata
        print(f"Lista ordinata in senso ascendente con il metodo sorted(): {lista}")
    
    def sort_method(numbers:list[int])->None:
        numbers.sort()#modifica la lista esistente (lavora in-place)
        print(f"Lista ordinata in senso ascendete con il metodo .sort(): {numbers}")
    
    
    # copy() in questo caso serve per mostrare sorted() su la lista originale 
    # Vedi esercizio 4
    sorted_method(numbers.copy())
    
    # Dopodiché modifico la lista originale con il metodo .sort() 
    sort_method(numbers)

def main()->None:
    sort_list([5, 2, 8, 1, 9])

if __name__ == "__main__":
    main()

