"""
Rimuovi gli elementi da una lista usando il while loop
senza creare una copia della lista
"""
# La lista di interi su cui iterare
number_list:list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Dichiaro variabile 'size' che punta alla lunghezza della lista 
size:int = len(number_list)

# Variabile contatore 
cont = 0

# Itera sulla lista finché cont è più piccolo di size
while cont<size: 
    
    # Controllo se il numero è più grnade di 50 
    if number_list[cont]>50:
        # In caso cancello l'indice dalla lista
        del number_list[cont]
        
        # Decremento la lista
        size -=1 
    else: 
        # Aggiorno il contatore e mi muovo sul prossimo elemento
        cont +=1
        
print(number_list)
