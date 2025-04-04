import random

'''
Primo Esercizio:
Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

For example:
Test 	

print(somma_elementi([1,1,1],[1,1,1]))
Risultato
[2, 2, 2]

'''

# def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    
#     b:list[int] = []
    
#     for nums in range(len(x)):
#         b.append(x[nums]+ y[nums])
#     return b

# print(somma_elementi([1,1,1], [1,1,1]))

# print(somma_elementi([1,2,-1], [0,-1,0]))
# print(somma_elementi([1,5], [1,2]))

'''
Secondo Esercizio:
Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.

Un fattore primo di n è un numero primo che divide esattamente n (cioè senza resto), e la cui moltiplicazione in sequenza restituisce n. Un numero può avere lo stesso fattore primo più volte.
Cosa sono i fattori primi?

I fattori primi di un numero sono numeri primi che, moltiplicati tra loro, danno come risultato proprio quel numero.

🔹 Esempio:
Il numero 60 si può scomporre in: 2 × 2 × 3 × 5 → cioè: 2² × 3 × 5

🔎 Suggerimento:
Prova a pensare a come potresti "smontare" un numero dividendolo più volte, iniziando dal numero primo più piccolo possibile. Cosa succede ogni volta che la divisione ha resto 0? E cosa potresti fare quando non lo è più?

For example:
Test 	

print(prime_factors(4))

Result

[2, 2]

Test
print(prime_factors(60))

Result

[2, 2, 3, 5]

'''


# def prime_factors(n:int)->list[int]:
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors


# print(prime_factors(10))


'''
Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

tutti i numeri pari vengano prima di tutti i numeri dispari;

l’ordine relativo tra pari e dispari va mantenuto;

l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

For example:
Test 	

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

Result
[6, 8, 4, 3, 1, 7]
'''

# def even_odd_pattern(numbers:list[int]) -> list[int]:
#     even_list:list[int] = []
#     odd_list:list[int] = []
#     for elems in numbers:
#         if elems%2==0:
#             even_list.append(elems)
#         else:
#             odd_list.append(elems)
    
    
#     return even_list + odd_list
    

# print(even_odd_pattern([1,2,4,3,5,6,7,8,9,10]))


'''
Esercizio 4:
Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista. Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.

Il tuo compito è individuare i numeri mancanti.

Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.

'''

