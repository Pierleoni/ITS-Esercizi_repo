# Diagrammi a blocchi 1 modulo


#Esercizio 1: 
'''
Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo,
conoscendo quelle dell’ipotenusa a e dell’altro cateto b.
'''  
'''
import math
a= int(input("aggiungi un numero: "))
b= int(input("aggiungi un altro numero: "))
if a>b:
    c= math.sqrt(a**2-b**2)
    print(c)
else:  
    print("errore")
    
'''



#Esercizio 2 
''' Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''
''''
maximum = 0
cont = 1
while cont < 4:
    cont= cont+1
    n = int(input("inserire un numero:"))
    if n > maximum:
        maximum = n

print(maximum)
'''
#ciclo for ex 2
'''
maximum = 0
i= 0 
for i in range(4):
    
    n = int(input("inserire un numero:"))
    if n > maximum:
        maximum = n
    # in questo caso mi printa il valore massimo ogni volta che inserisco un numero 
    #     print(maximum)
    # else:
    #     print(maximum)
print(maximum)
'''


# Ex 3: Calcolo della somma di numeri positivi
'''
Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente.
Quindi, se un numero è negativo o zero, ignora quel valore nella somma.
'''
# sum = 0 
# cont = 1 
# while cont<=5:
#     n = int(input("inserire un numero:"))
#     if n>0:
#         sum = sum +n
#     cont = cont +1
# print(sum)


#Ex 4: Controllo della parità di un numero
'''
Progetta un algoritmo utile a determinare se un numero inserito dall'utente è pari o dispari.
'''


# n = int(input("Insert a number:"))
# if n %2==0:
#     print("il numero è pari")
# else: 
#     print("il numero è dispari")
    



#Ex 5: Verifica se un numero è primo
'''
Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo.
'''
# n = int(input("Inserire numero primo: "))
# primo: bool = True
# if n == 2:
#     print("Il numero è primo!")
# if n>2:
#     div = 2 
#     while div<n:
#         if n %div==0:
#             print("il numero non è primo!")
#             primo = False
#             break
#         div += 1
        
#     if primo:
#         print("Il numero è primo!")     
# else:
#     print("Il numero non è primo!")


# Ex 6:
'''
Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente
'''
# n= int(input("inserire numero positivo:"))
# if n>0:
#     fattoriale = 1 
#     i = 1 
#     while i!=n: 
#         fattoriale = fattoriale*1
#         i += 1 
#     else: 
#         print(fattoriale)
# else: 
#     print(f"{n} deve essere positivo")


# Ex 7
'''
Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.
'''
# pari = 0
# dispari = 0 
# cont = 0 

# for i in range(10):
#     n = int(input("inserire il numero in input:"))
#     if n%2==0:
#         pari +=1
#     if n%2==1:
#         dispari+=1

# print(pari)
# print(dispari)


#Ex 8 
'''
Progetta un algoritmo che dati 7 numeri, 
trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.

'''
# soglia = int(input("inserire la soglia:")) 
# # n = int(input("inserisci il numero:")) 
# cont = 0
# while cont != 7: 
#     n = int(input("inserisci il numero:")) 
#     if n > soglia: 
#         print(n)
#     cont += 1



#Ex 10 
'''
Progettare un algoritmo che, richiesto allo studente il reddito familiare e la media dei voti, 
se il reddito è inferiore a 20.000 € e la media è superiore a 27 approva la borsa di studio, altrimenti rifiuta la richiesta visualizzando il messaggio "Borsa di studio rifiutata. 
(Motivo: reddito o media insufficiente)".
'''

# r = int(input("inserire il reddito familiare:"))
# m = int(input("Inserire media dei voti:"))
# if r < 20000 and m > 27:
#     print("Borsa di studio approvata")
# else:
#     print("Borsa di studio rifiutata. Motivo: reddito o media")


#Ex 11 
'''
Progetta un algoritmo per gestire la prenotazione dei posti in una sala che contiene 20 sedie libere. 
L'utente può inserire una delle seguenti opzioni "prenota", "libera", "visualizza", "esci". Per ogni opzione:
    se l'utente inserisce "prenota", se ci sono ancora sedie libere, decrementa di uno il numero di posti liberi;
    se l'utente inserisce "libera", incrementa di uno il numero di sedie libere;
    se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.

Torna all'inserimento di una opzione finché l'utente non seleziona "esci".
'''

liberi = 20 
opzione = ""
while opzione != "esci":
    opzione = input("Inserire l'opzione: ")
    if opzione == "prenota":
        if liberi > 0:
            liberi -= 1
        else: 
            print("Non ci sono posti disponibili!")
    elif opzione == "libera": 
        if liberi < 20: 
            liberi += 1 
        else:
            print("I posti sono già disponibili!")
    elif opzione == "visualizza": 
        print(liberi)
        print(20 - liberi)

