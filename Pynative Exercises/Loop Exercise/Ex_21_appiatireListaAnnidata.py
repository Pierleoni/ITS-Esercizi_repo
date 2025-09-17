"""
Appiattire una lista annidata utilizzando dei cicli
"""
# Definisco una funzione che prende un solo parametro in input e restiruisce una lista di interi
def flatten_list(nested_list:list[list[int]])->list[int]:
    
    # Inizializzo lista vuota dove appendero gli elementi delle liste annidate e non annidate
    flattened_list:list[int]= list()
    
    # Outer loop: itero sulle sotto-liste nella lista annidate in input
    for lists in nested_list: 
        
        # Check se gli elementi della lista annidata sono istanze dell'oggetto list (quindi sono sotto-liste)
        if isinstance(lists,list):
            # Inner Loop: itero sugli elementi delle sotto-liste
            for items in lists:
                
                # Appendo gli elemeti delle sotto-liste alla lista vuota
                flattened_list.append(items)
        # Se gli elementi della lista annidata non sono sottoliste,
        else:
            # Li appendo direttamente alla lista vuota  
            flattened_list.append(lists)
    print(flattened_list)



def main():
    flatten_list([1, [2, 3], [4, 5, 6], 7, [8, 9]])

if __name__ == "__main__":
    main()