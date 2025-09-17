
"""
Controlla che il file sia vuoto o no
"""

# il modulo os fornisce funzioni per interagire con il sistema operativo (file, cartelle, processi, ecc.).

import os


"""
os.stat("new_test.txt") restituisce un oggetto che contiene varie informazioni 
sul file new_test.txt (dimensione, permessi, data di modifica, ecc.).

.st_size è un attributo di quell’oggetto che indica la dimensione del file in byte.

"""

# La variabile size contiene un intero: il numero in bit di byte del file
size = os.stat("new_test.txt").st_size
# Se il valore di size è 0...
if size == 0:
    # ... stampa il messaggio: 'il file è vuoto'
    print('Il file è vuoto')
# Altrimenti stampa la grandezza in bit del file
else: 
    print(size)






