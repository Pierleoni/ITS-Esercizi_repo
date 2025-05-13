PATH: str = "Progetti_Py\Lezione15\example.txt"
mode: str = "w"
endcoding: str = "utf-8"


'''
mai usare path assoluto a meno che non li costruisce il progammatore nel programma in modo dinamico, 
usare sempre il path relativo
'''

file = open(PATH, mode=mode, encoding=endcoding)
print(file)
"""
il wrapper prendo una cosa e la incapsulo in un altra: posso memorizzare informazini extra che nell'informazione orginale non ci sono.
I wrapper possono estendere le funzionalità di una classe facendola circordare da un altra, non c'entra l'ereditarietà
In questo caso il wrapper è io.TextIOWrapper name='Progetti_Py\\\Lezione15\\example.txt' mode='r' encoding='cp1252'
"""
# output:str = file.read() 
"""
questa funzione read mi permette di puntare al primo byte in memoria relativo a quel file, in questo caso mi prende dal primo byte del file fino alla fine.
se volgio leggere una porzione del file tipo i primi 20 caratteri scrivo file.read(20), di defualt legge tutto il file
"""
"""
se voglio scrivere il contentuto 
"""
output: str = file.write("Ciao")
# Da notare come sul terminale mi riporti il numero di caratteri scritti, nel caso di Ciao sono 4 caratteri
print(output)

file.close()
"""
è current working directory è la cartella in cui mi torvo con il temrianle in quel momento da cui sto lanciando Python.
Quindi quando sto lanciando il programma indicandogli "Lezione15/example.txt" sto dicendo al programma di lanciare il file contenuto dentro la lezione15 dentro la cartella Progetti Py e dnetor la cartella Lezione15 di lanciare il file example.txt
Io ho altre 2 variabili è mode e encoding: occhio perché può capitare un erroe literal perché magari proviamo a lanciare il file magari in cinese e usando l'encoding utf-8 
il mode: i file possono essere letti in tre modi soprattuto con r(read) e w(write), quindi scirvendo r dico che posso solo leggere ma non scrivere.
C'è una terza modlaita a(append): appende l'ultima informazione alla fien del file spostando l'EOF più in là.

"""