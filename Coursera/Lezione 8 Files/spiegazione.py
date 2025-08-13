# Il tipo 'TextIO' indica un oggetto in modalità testo
from typing import TextIO
"""
In Python, per aprire un file si utilizza la funzione open().
Questa funzione restituisce un file handle:
    cioè un oggetto (o variabile) che rappresenta il file aperto 
    e che può essere utilizzato per eseguire operazioni di lettura, 
    scrittura o modifica sul file stesso.
    Tutto ciò è simile al comando File>Apri in un programma come Word:
        il file viene localizzato e aperto,
        si ottiene un “collegamento” al file,
        da quel momento è possibile interagire con il suo contenuto 
        tramite comandi specifici (read(), write(), ecc.).
"""

"""
TODO: La Sintassi è: open(nomeFile, modalità).
    nome_file → una stringa che rappresenta il percorso e il nome del file.

    modalità (opzionale) → specifica il tipo di operazioni da eseguire sul file.

Modalità principali:
    'r' (read): modalità di sola lettura (default se non specificata).

    'w' (write): modalità di scrittura.
    ! In questa modalità, se il file esiste già e contiene dati, il contenuto viene cancellato e sostituito con il nuovo.
"""
fhand:TextIO = open(r'C:\Users\Project Lead\Desktop\Esercizi Programazzione ITS\Progetti_Py\Coursera\Lezione 8 Files\mbox.txt')
print(fhand)
# Cosi facendo non stampa le righe presenti nel file, restiruisce l'oggetto handle in memoria

"""
Un file handle è come una “finestra” che il programma apre verso un file esterno.
Attraverso l’handle possiamo comunicare con il file: leggerlo, scriverlo, scorrerlo riga per riga, ecc.
L’handle non contiene il contenuto del file, ma è un wrapper che fornisce le funzioni e le informazioni necessarie per accedervi.
Quando apriamo un file in Python con open(), otteniamo un oggetto che rappresenta questo handle.
Ad esempio:

<_io.TextIOWrapper name='C:\\Users\\Project Lead\\Desktop\\Esercizi Programazzione ITS\\Progetti_Py\\Coursera\\Lezione 8 Files\\mbox.txt' mode='r' encoding='cp1252'>

    !name → percorso e nome del file

    !mode → modalità di apertura ('r' = lettura predefinita)

    !encoding → codifica usata per interpretare i caratteri (es. cp1252, UTF-8)
    Una volta chiuso il file con .close(), anche l’handle viene chiuso, interrompendo la connessione tra programma e file.
"""




"""
open(...) apre il file e restituisce un file handle (xfile in questo caso).

Il for lines in xfile: itera riga per riga sul contenuto del file.

print(cheese) stampa ogni riga letta.
"""
xfile:TextIO = open(r'C:\Users\Project Lead\Desktop\Esercizi Programazzione ITS\Progetti_Py\Coursera\Lezione 8 Files\mbox.txt')
for lines in xfile:
    print(lines, end="")

print("\n--------------------------------------")
"""
Contare il numero di righe in un file
"""
# Creo un file .txt nella directory padre di questa cartella
file:TextIO= open("test.txt")
# Per contare il numero di righe nel file inizializzo una varibile cont_words a 0 
cont:int = 0 
# Per ciauscuna riga nel file...
for line in file: 
    # ... aggiorno il contatore ogni volta che incontro una nuova riga
    cont+=1

# Stampo in output conteggio massimo di righe nel file 
print(f"Line Count: {cont}")

print("-------------------------------")

"""
Leggere tutto il contenuto del file  
"""

#! Apro il file e assegno l'handle alla variabile f

f:TextIO = open('test.txt')

# Leggo tutto il contenuto del file e lo salvo nella variabile inp
inp = f.read() #! read() legge l'intero contenuto del file come stringa

# Stampo il contenuto del file e la lunghezza in caratteri della stringa letta
print(f"Contenuto del file:\n{inp}\nLunghezza del contenuto del file : \n{len(inp)}")

# Stampo i primi 20 (il 21 escluso) caratteri del contenuto del file usando slicing
print(f"\n{inp[:21]}")


"""
cercare parole in un file 
"""
# Creo un oggetto handle con tipizzazione TextIO
ffiles:TextIO = open('test.txt')

try:
    # Per ciascuna riga nell'oggetto ffiles...
    for line in ffiles:
        # ...Se la riga inizia con la parola 'Lorem'
        #! (startswith() restituisce True se la stringa inizia con il valore specificato, altrimenti False)
        if line.startswith('Lorem'): 
            # stampa quella riga
            print(line)
finally:
    # Chiudo il file per liberare le risorse
    ffiles.close()
    

"""
Un altro modo di scrivere ciò è usando lo statement 'with':
il with è un 'context manager statement:
!è un struttura del linguaggio che permette di eseguire del codice dentro un contensto gestito automaticamente,
!dove all'ingresso e all'uscita vengono eseguiti operazioni predefinite

La sintassi è:
?with <espressione che restituisce un context manager> as <variabile>: codice da eseguire nel contesto

Funzionamento tecnico

Quando Python esegue un with:

    Valuta l’espressione dopo with (es. open("test.txt")).

    Chiama il metodo __enter__() dell’oggetto restituito → il suo valore di ritorno viene assegnato alla variabile dopo as.

    Esegue il blocco di codice indentato.

    Alla fine (anche in caso di eccezione) chiama __exit__() dell’oggetto → 
    qui si fanno operazioni di chiusura, rilascio risorse, cleanup, ecc.
    
?Esempio: 
    with open("test.txt") as f:
    print(f.read())
#! Qui il file è già chiuso, anche se dentro il blocco fosse stato sollevato un errore

In breve:
!with serve per gestire automaticamente setup e teardown di risorse, garantendo la chiusura/rilascio anche in caso di errore.
"""
# Apro il file 'test.txt' assengandolo a un oggetto handle chiamato ffile
with open('test.txt') as ffile:
    # Per ciascuna riga del contentuto del file...
    for line in ffile: 
        
        # Se la riga inizia con 'From'
        if line.startswith('From'):
            # Stampo la riga
            print(line)

    """
    Da notare come in questo caso non serva un blocco try-finally ne un blocco try-except per gestire l'apertura e 
    la chiusura automatica del file poichè lo statement with gestisce in automatico:
        !L'apertura e chiusura del file
        !E la gestione di eventuali errori
    """

# In entrambi i metodi, specialmente nel secondo, il testo stampato
# presenta spazi o interruzioni di riga indesiderate.  
# Questo accade perché nel file di testo ogni riga termina con un carattere
# di newline (\n).  
# Per eliminare questi caratteri, possiamo usare il metodo rstrip().
with open('test.txt') as ffile:
    for line in ffile:
        
        """
        !Il metodo .rstrip() rimuove solo i carattteri alla fine della riga, 
        !ed evita che il print(line) vada a capo due volte (una per il '\n' del file e una per il print() stesso 
        (di defualt il print aggiunge un carattere di newline alla fine di ciò che stampa) )
        """        
        line = line.rstrip() #!a differenza del metodo .strip() rimuove i caratteri solo alla fine della stringa
        
        if line.startswith('From'):
            print(line)
            



"""
Skippare con il continue statement
"""
# # In questo caso si vuole cercare una riga che inizi on un carattere specifico skippando tutte le altre
# #  Apre il file 'test.txt' in modalità lettura e lo assegna alla variabile 'sp_ch'.
# # L'uso di 'with' garantisce la chiusura automatica del file al termine del blocco.
# with open('test.txt') as sp_ch:
    
#     # Itera su ogni riga del file.
#     for line in sp_ch:
        
#         # Rimuove eventuali caratteri di newline (\n) o spazi bianchi a destra della stringa.
#         line = line.rstrip()
        
#         # Se la riga NON inizia con la stringa 'From:', salta l'iterazione corrente e passa alla successiva.
#         if not line.startswith('From:'):
#             continue
        
#         # Stampa la riga che inizia con 'From:' preceduta dalla scritta 'Risultato:'.
#         print(f"Risultato:{line}")




"""
Usare l'operatore 'in' per selzionare le linee

"""
# Apro il file in sola lettura e uso lo statement with per chiudere in automatico il file alla fine
with open('test.txt') as in_file:
    # Itero per ogni riga presente nel file
    for l in in_file:
        
        # Rimuovo gli spazi bianchi finali dalla riga
        l = l.rstrip()
        
        # Check se la stringa '@utc.ac.za' non è presente tra le righe del file
        if not '@utc.ac.za' in l:
            
            # Se non è presente si passa alla prossima iterazione
            continue
        
        # Stampa la riga solo se contiene '@utc.ac.za'
        print(f"Res:{l}")
        


"""
Prompt per nome del file
"""
fname:str = input("Digita il nome del file:")
with open(fname) as f_hand:
    cont_words:int = 0
    for line in f_hand:
        if line.startswith('From'):
            cont_words+=1
    print(f"Ci sono {cont_words} righe della parola \'From\' in {fname}")


"""
Gestire errori di input con i nomi dei file
"""
# Talvolta gli utenti sbagliano a mettere  

try:
    hand:TextIO = open(fname)
except: 
    print(f'Il file {fname} non può essere aperto ')
    quit() 

contatore: int = 0
for words in hand:
    if words.startswith('amet'):
        contatore+=1
print(f"Ci sono {contatore}, della parola \'amet\' in {fname}")






import readline

# Memorizza la cronologia in un file
histfile = ".py_history"
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    pass

while True:
    try:
        cmd = input(">>> ")
        print(f"Hai digitato: {cmd}")
    except KeyboardInterrupt:
        break

# Salva la cronologia
readline.write_history_file(histfile)
