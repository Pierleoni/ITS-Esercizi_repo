from typing import Any


def binary_search_2(sequence:list[int], element:int) ->int:
    # Assicura che gli elementi della lista vengono riordinati in modo ascendente
    sequence = sorted(sequence)
    # Inizzializzo la variabile che equivale al primo indice di una lista 
    begin_index:int = 0
    # L'ultimo indice equivlae alla lunghezza della lista -1, perché l'indicizzazione è zero based
    # Il metodo sorted assicura che la lista contenga elementi ordinati in modo ascendente
    last_index:int = len(sequence)-1
    
    while begin_index <= last_index:
        # Prende l'indice di mezzo della lista che sta tra begin_index e last_index
        mid_point = begin_index + (last_index - begin_index)//2
        
        # Estrae il valore dell'indice centrale della lista
        mid_point_val = sequence[mid_point]
        # il blocco try-excpet serve per gestire errori di tipo TypeError, quando si confrontano tipi di dato diversi
        try:
            # Se uguali ritorna T
            if mid_point_val == element:
                return True
            elif element<mid_point_val: #Se element e minore de valore dell'indice di mezzo, restringe la ricerca a sinistra della lista
                last_index = mid_point -1
            else:
                begin_index = mid_point +1 #Se element è maggiore di mid_point_val restringe il campo di ricerca a destra
        except TypeError:
            return "Errore: tipi non confrontabili"
    return False



seq_4:list[int] = [26, 3, 5,6,9,1,0]
elem_2 = 0
print(binary_search_2(seq_4, 27))





# def binary_search(sequence:list[Any], element:Any) ->int:
#     # Assicura che gli elementi della lista vengono riordinati in modo ascendente
#     sequence = sorted(sequence)
#     # Inizzializzo la variabile che equivale al primo indice di una lista 
#     begin_index:int = 0
#     # L'ultimo indice equivlae alla lunghezza della lista -1, perché l'indicizzazione è zero based
#     # Il metodo sorted assicura che la lista contenga elementi ordinati in modo ascendente
#     last_index:int = len(sequence)-1
    
#     while begin_index <= last_index:
#         # Prende l'indice di mezzo della lista che sta tra begin_index e last_index
#         mid_point = begin_index + (last_index - begin_index)//2
        
#         # Estrae il valore dell'indice centrale della lista
#         mid_point_val = sequence[mid_point]
#         # il blocco try-excpet serve per gestire errori di tipo TypeError, quando si confrontano tipi di dato diversi
#         try:
#             # Se uguali ritorna T
#             if mid_point_val == element:
#                 return mid_point
#             elif element<mid_point_val: #Se element e minore de valore dell'indice di mezzo, restringe la ricerca a sinistra della lista
#                 last_index = mid_point -1
#             else:
#                 begin_index = mid_point +1 #Se element è maggiore di mid_point_val restringe il campo di ricerca a destra
#         except TypeError:
#             return "Errore: tipi non confrontabili"
#     return None


# sequence_1:list[int] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
# elem_1:int = 8

# print(binary_search(sequence_1, elem_1))




# print(binary_search([4,7,1,3,9], 3))
