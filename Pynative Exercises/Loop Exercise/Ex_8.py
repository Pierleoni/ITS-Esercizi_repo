"""
Stampa la lista in ordine inverso usando un loop
"""

def reversed_list(lista:list[int])->None:
    # 1 approccio con  il metodo built-in reversed()
    
    
    # Inzializzo una nuova lista in cui salvo reversed() che restituisce un iteratore che percorre la lista al contrario
    list_2:list[int] = reversed(lista)
    
    # Itero sugli elementi della nuova lista
    for nums in list_2:
        # Stampo i singoli elementi
        print(nums)
    
    


# Secondo approcio con len()
def reverse_lenght_list(lista_2:list[int])->None: 
    # Calcolo l'ultimo indice della lista
    size = len(lista_2) -1
    
    # Itero dall'ultimo indice(size) fino a 0 (incluso), con step -1
    for i in range(size, -1,-1):
        # Stampo l'elemento corrispondente all'indice i
        print(lista_2[i])

def main():
    reversed_list([10, 20, 30, 40, 50])
    reverse_lenght_list([10, 20, 30, 40, 50])

if __name__ == "__main__":
    main()