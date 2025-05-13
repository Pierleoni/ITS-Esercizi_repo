'''
La parola poliforfismo significa avere diverse forme: abbiamo creato un file Persona.py 
che all suo intenro ha un meotdo speak in seguiti abbiamo definito un file alieno.py e dentro il file abbiamo definito la classe Alieno con i vari metodi get e set e abbiamo definito il metodo speak() anche per questa classe che stmapa in otutput un messaggio in ligua aliena.
Abbiamo quindi due classi diverse e differenti ma hanno un metodo con lo stesso nome(speak()) che quindi può essere utiizzato da oggetti di  classe diverse.
Ogni metodo speak() deve fornire una propria versione: quindi entrambi le classi Persona e alieno hanno la proprioa funzione ma 
Il polimorfismo è: metodi di classi diverse con lo stesso nome che fanno cose diverse.

'''
# import sys
# import os
# sys.path.append(os.path.abspath('..'))
from Persona_2 import Persona
from alieno import Alieno

'''
creare un oggetto p della classe persona 
'''
p:Persona = Persona("Antonio", "Scugnizzo", 22)

# Visualizzare le informazioni dell'oggetto p della classe Persona

print(p)

et:Alieno = Alieno("Andromeda")
# Visualizzare le informazioni dell'oggetto et della classe ALieno

print("\n",et)

'''
invocare il metodo speak() della classe Persona
'''

p.speak()

'''
invocare il metodo speak() di un ALieno
'''
et.speak()

'''
in output abbiamo 2 risultati diversi: io primo dico all'oggetto p il metodo speak() he mi fa un'azione specifica relativa alla classe Persona, mentre quando l'oggetto et invoca il metodo speak() che mi fa una azione specidfica per la classe Alieno.
il polimorfismo è quindi avere metodi con lo stesso nome per classi diverse e definito in maniera diversa per ogni classe. 
l'ovverriding abilita il poliformismo, sono due cose correlate ma sono diverse tra loro:
se ad esempio la classe Aleino era la classe genitore e la classe Persona il metodo speak() della classe Perosna andava a overridare il metodo speak() della classe alieno.
Come posso disntinguere i due metodi delle due classi diverse? Dipende dall'oggetto che lo invoca: se l'oggetto p invoca il metodo speak()
allora sto dicendo a Python di invocare il metodo speak() della classe Persona, se l'oggetto et invoca il metodo speak() sto dicendo a Python di invocare il metodo speak() della classe Alieno.
Quindi il polimorfismo lo possiamo definire anche come: ho un metodo con lo stesso nome in classi diverse che ha comportamenti diversi per ogni classe.
''' 

