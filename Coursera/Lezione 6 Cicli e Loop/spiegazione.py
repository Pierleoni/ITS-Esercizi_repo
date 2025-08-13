# while True:
#     line = input('>')
#     if line[0]== '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# lista:list[int] = [5,4,3,2,1,0]

# for n in lista:
#     print(n)
# print('Done!')


# friends:list[str] = ["Mario", "Rebecca", "Giona"]

# for friend in friends:
#     print(f"Hello, {friend}")



lista1: list[int] = [9, 41, 12, 3, 74, 15]
tot = 0
for nums in lista1:
    # print(nums)
    tot +=nums 
    # print(tot)
    avg = tot/len(lista1)
print(f"Totale:{tot}\nMedia: {avg}\n")


"""
Torvare il numero più grande e il più piccolo
"""
# Inizializzare una variabile che punta all'indice 0 della lista 
largest_so_far:int = lista1[0]
# Altra variabile con valore 'None', serve per trovare il numero più piccolo nella lista
smallest_so_far:int = None
print(f'Before: {largest_so_far}\n{smallest_so_far}')

# Per ogni singolo elemento il lista1...
for num in lista1:
    
    # Se il valore di 'num' è maggiore del valore di 'largest_so_far
    
    if num>largest_so_far:
        # Allora il valore di 'largest_so_far' equivale al valore di 'num'
        
        largest_so_far = num 
    # Oppure se il valore si smallest_so_far è None → cattura il valore di 'num'
    
    # L'operatore is o is not serve in questo caso per assicurare la comparazione successiva del blocco elif poiché non è possbile comparare un valore di tipo None con un integer
    elif smallest_so_far is None:
        smallest_so_far = num 
    # Oppure se il valore del singolo elemento è minore del valore di smallest_so_far
    
    elif num<smallest_so_far:
        # Allora il valore di smallest_so_far cattura il valore del singolo elemento
        smallest_so_far = num 
    
    # Printa il numero più grande a ciascun iterazione e il singolo elemento di ciascuna iterazione
    print(largest_so_far, num)
    print("---------------------")
    print(smallest_so_far, num)
    

print(f"After: {largest_so_far}\n{smallest_so_far}")





"""
Per contare quanti numeri sono presenti in lista1 
"""
# Settiamo una variabile contatore
# cont:int = 0
# print(f"Before: {cont}")
# # Per ognui numero (n) in lista1...
# for n in lista1:
#     # ...aggiorniamo il contatore
#     cont+=1
#     # Stampiamo il numero di iterazioni e il valore corrente
#     print(cont, n)
    
# # Stampiamo in output il numero totale di iterazioni fatte, in questo caso sono 6 poichè ci sono 6 valori interi nella lista1
# print(f"The total of iterations: {cont}\n")



"""
Per sommare il totale degli elementi in lista1

"""
# Settiamo una variabile contatore a zero: serve per immagazinare il valore della somma totale dei singoli elementi nella lista
# count:int = 0
# print(f'Before: {count}')

# Per ogni elemento/numero nella lista1...
for elem in lista1:
    # sommiamo il numero di iterazioni (cont) con i singoli elementi della lista
    count += elem
    print(f"la somma totale dentro il loop: {count}, il singolo elemento: {elem}")
    # Se vogliamo aggiungere la media degli elementi(facoltativo)...
    # Inizializziamo una variabile 'average'(media in italiano):
    # Questa variabile punta alla divisione tra la somma totale degli elementi (count), diviso la lunghezza della lista
    average:int = count/len(lista1)
print(f"After:\n\
La somma totale degli elementi fuori dal loop: {count}\nMedia: {average}")

"""
Trovare la media numerica usando un loop
"""

# # Inizializziamo due variabili:
# # La vairaibile contatore
# cont = 0
# # La variabile somma
# somma = 0

# print(f'Before: {cont}, {somma}')

# # Per ogni singolo elemento in 'lista1'...
# for el in lista1:
#     # ..il valore della variabile 'somma' si somma con il valore della variabile 'el' per ogni iterazione 
#     somma += el
#     # Aggiorno il contatore ad ogni iterazione altrimenti viene eseguita una sola iterazione
#     cont+=1
#     # Questo print stampa il numero di iterazioni, la somma degli elementi nella lista e il singolo elemento di ogni iterazione
#     print(f"{cont}, {somma}, {el}")


# print(f"Numero di iterazioni: {cont}\n\
# Somma di totale di ciascun elemento: {somma}\nMedia numerica degli elementi: {somma/cont}") 
    




"""
Filtrare gli elementi di una lista usando un loop
"""
# # Se volgiamo trovare i valori più grandi in lista1 senza scorrere tutta la lista
# # Per ogni singolo valore in lista1...
# for value in lista1:
#     # ... se il valore o i valori sono maggiori di 20
#     if value > 20:
#         # Stampiamo i numeri più grnadi di 20 dentro lista1
#         print(f'\nLarge numbers: {value}')


"""
Cercare un elemento nella lista usando una variabile booleana
"""

# # Inizializzo una variabile con valore False
# trova:bool = False
# print(f"Before: {trova}")

# # Per ogni valore in lista1...
# for val in lista1: 
#     # Se il valore della variabile 'val' è uguale a 15
#     if val == 15:
#         # Il valore di 'trova' diventa True, altrimenti rimane False
#         trova = True
    
#     print(f"Valore della vaiabile booleana: {trova}\nValore dell'elemento della lista: {val}")
# print(f"After: {trova}")

