"""
Esegui la manipolazione della lista
1. Cambiare il secondo elemento della lista con 200 e stampare la lista
2. Aggiungere il numero 600 alla fine della lista e stampare il nuovo numero
3. Inserire l'elemento 300 alla terza posizione (secondo indice) della lista e stampare il risutato
4 Rimuovere l'elemento 600 dalla lista e stampare la lista
5. Rimuovere l'elemento all'indice 0 dalla lista e stampare la lista 
"""

def list_manipulation(my_list:list[int])->None:
    
    def update_list(my_list: list[int])->None:
        my_list[1] = 200
        print(f"Dopo aver cambiato il secondo elemento: {my_list}")
    
    def append_list(my_list: list[int])->None:
        my_list.append(600)
        print(f"Dopo aver appeso il numero 600: {my_list}")
    
    def insert_list(my_list: list[int])->None:
        my_list.insert(2, 300)
        print(f"Dopo aver inserito il numero 300 all'indice 2: {my_list}")
    
    def remove_byValue(my_list: list[int])->None:
        my_list.remove(600)
        print(f"Dopo aver eliminato l'elemento 600 (per valore): {my_list}")
    
    def remove_byIndex(my_list: list[int])->None:
        my_list.pop(0)
        print(f"Dopo aver rimosso l'elemento all'indice 0: {my_list} ")

    
    
    update_list(my_list)
    append_list(my_list)
    insert_list(my_list)
    remove_byValue(my_list)
    remove_byIndex(my_list)


def main()->None:
    lista:list[int] = [10, 20, 30, 40, 50]
    print(f"Lista iniziale: {lista}")
    list_manipulation(lista)

if __name__ == "__main__":
    main()