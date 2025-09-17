"""
Mergia 2 liste un in una nuova lista
"""

# Definisco una fuzione che prende input due liste di numeri interi
def merge_list(lista1:list[int], lista2:list[int])->list[int]:
    # Creo una lista vuota
    list_merge:list[int] = list()
    
    # Itero sui singoli elementi della prima lista in input alla fuzione
    for i in lista1:
        
        # Se il numero non è divisibile di due, quindi è dispari...
        if i %2 !=0:
            # ... lo appendo alla nuova lista
            list_merge.append(i)
    # Itero su ciascun elemento della seconda lista in input
    for j in lista2:
        
        # Se il numero della seconda lista è divisibile per 2...
        if j %2==0:
            
            # ...lo appendo alla nuova lista
            list_merge.append(j)
    # Ritorno la nuova lista 
    return list_merge


def main():
    print(merge_list([10,20, 25, 30, 35], [40, 45, 60, 75, 90]))

if __name__ == "__main__":
    main()