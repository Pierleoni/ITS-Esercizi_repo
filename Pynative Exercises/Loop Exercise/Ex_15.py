"""
Stampa gli elementi agli indici dispari di una lista 
"""

# 1 approccio:
# Definisco una funzione che prende come parametro una lista di interi
def odd_index_enum(lista:list[int])->list[int]:
    # Inzializzo una lista vuota
    new_list:list[int] = list()
    # Itero sugli indici e sugli elementi della lista in input
    for idx,elem in enumerate(lista):
            # Se l'indice dell'elemento non è pari
            if idx%2!=0:
                # Aggiungo l'elemento alla nuvoa lista
                new_list.append(elem)
            else:
                
                pass
    # Stampo la nuova lista con gli elementi agli indici dispari
    print(new_list)



def odd_index(lista_2:list[int])->list[int]:
    new_lista:list[int]= lista_2[1::2]
    print(new_lista)

def main():
    odd_index_enum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    odd_index([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

if __name__ == "__main__":
    main()