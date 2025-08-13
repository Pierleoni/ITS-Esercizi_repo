fruit:str = 'banana'
print(fruit[3:3])
print(fruit[:])

greet:str = 'Hello World'

new_greet:str=  'J' + greet[1:]
print(new_greet)


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# Esercizio 3:
# Devo creare una funzione che accetta in input una stringa e un carattere per contare le occorrenze del carattere
def cont(s:str, chars: str):
    # Diciharo un contatore interno per contare il numero di occorenze del carattere
    count = 0
    # per i caratteri nella stringa...
    for char in s:
        
        # ...se il singolo carattere è uguale a il parametro in input
        if char == chars:
            # Aggiorno il contatore, in questo caso il numero di occorenze del carattere
            count +=1
    # Stampo in output il il numero di occorenze e la stringa passata in input
    print (f"Stringa originaria: {s}\nIl carattere da cercare: {chars}\nNumero di occorenze del carattere: {count}")

cont('banana', 'a' )



# Stringa contente un testo con email 
data:str = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# Cerca la posizione del carattere '@' nella stringa data
atpos = data.find('@')
print(atpos)


# Cerca la posizione del primo spazio a partire da atpos(quindi dopo la '@')
sppos = data.find(' ',atpos)
print(sppos) #Stampa la posizione dello spazio vuoto


"""
Estrae la sottostringa compresa tra la posizione subito dopo la '@' (atpos + 1) 
e la posizione dello spazio successivo (sppos).
"""
host = data[atpos+1:sppos]
print(host) #Stampa la sottostringa che corrisponde al nome dell'host o il dominio dell'indirizzo email