# from formaGenerica import FormaGenerica
from rettangolo import Rettangolo
'''
creaimo un oggetto della classe shape FormaGenrica
'''
# shape:FormaGenerica = FormaGenerica()

'''
se runnano il codice da un errore che dice che impossibile creare un oggetto della classe Froma generica perché questa classe è una classe Astratta quindi non posso creare istanze di questa classe senza aver definito un implementazione del metodo draw()
Per costruire degli oggetti della FormaGenerica devo definire l'implementazione del metodo draw()
Quindi devo costruire classi derivate di FormaGenerica per implementare il metodo draw(), tuttavia se la classe è astratta non tutti i suoi metodi possono o devo essere astratti:
se all'intenro della classe astratta ho un metodo che so come definirlo ed implemtarlo allora quel metdo diventa concreto 
'''

'''
una volta importato la classe rettangolo creo un oggetto della classe Rettangolo
'''


'''
se provo ad eseguire il codice ottengo lo stesso tipo di errore di prima questo perché la classe rettangolo eredità da FormaGwenerica che è una classe astratta, 
in più non ho definito l'implemtatzipne del metodo astratto draw() Python mi rappresenterà la classe Rettangolo come una classe astratta poiché eredita da una classe Astratta.
Qyindi se io ho una classe astratta tutte le sottoclassi che non implementano il metodo astratto diventerano anch'esse classi astratte, quindi quello che devo fare e tornare sul file Rettangolo.py per implentare il metodo draw()
'''
r:Rettangolo = Rettangolo()

'''
adesso che abbiamo implementato il metodo draw nella calsse Rettangolo printiamo un oggetto r
'''
r.draw()

