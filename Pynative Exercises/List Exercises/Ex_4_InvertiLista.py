"""
Inverti una lista
"""

def reverse_list(my_list: list[int])->None:
    print(f"Lista originaria: {my_list}")
    
    # Primo metodo: uso il reverse() method
    def reverse_method(lst: list[int])->None:
        lst.reverse()
        print(f"Con il metodo reverse(): {lst}")
    
    
    # Secondo metodo: uso lo slicing negativo
    def neg_slicing(lst: list[int])->None:
        reversed_list = lst[::-1]
        print(f"Con lo slicing negativo: {reversed_list}")
    
    
    # Terzo metodo: uso il reversed method
    def reversed_method(lst: list[int])->None:
        rev_list = list(reversed(lst))
        print(f"Con il metodo reversed(): {rev_list}")
    
    
    reverse_method(my_list.copy()) #!Il metodo copy() crea una copia superficiale (shallow copy) della lista
    # Senza di esso solo il primo sotto-metodo eseguirebbe la vera inversione degli elementi della lista andando pero a modificare permanentemente la lista stessa
    # Di conseguenza la lista viene cambiata in modo permanente e le altre funzioni invertono la lista già invertita
    neg_slicing(my_list)
    reversed_method(my_list)
    
    print(f"Lista originale invariata: {my_list}")


def main()->None:
    
    
    reverse_list([100, 200, 300, 400, 500])

if __name__ == "__main__":
    main()