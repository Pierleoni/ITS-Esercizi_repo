from Persona_2 import Persona
from Studente import Studente


# creo un oggetto della classe Persona
fm:Persona = Persona("Gesù", "Cristo", 33)

# voglio visualizzare le informazioni relative all'oggetto fm
# print(fm)

# creo un oggetto della classe Studente
studente_1:Studente = Studente("Mario", "Paolini", 20, "")
# In questo caso mi da errore perché la matricola è una stringa vuota


studente_2:Studente = Studente("Mario", "Paolini", 20, "012345")
# Adesso funziona

print(studente_2)
'''
siccome studente eredità dalla classe Persona si eredità anche il metodo str della classe Persona, 
quindi Studente evoca il emtodo str della classe Persona e quando printo l'oggetto studente_2 python va a cercare il metodo str nella classe figlia e non trovandolo va a cercare nella classe padre(Persona)

'''
# Controllo se studente_1 sia istanza della classe Studente: per fare ciò uso isistnace(obj,Class) → cotnrolla se l'oggetto obj sia istanza della classe Class
# in caso affermativo -> True
# in caso negativo -> False
if isinstance(studente_1, Studente):
    print("\nstudente_1 è istanza della classe Studente")

# controllo se studente_1 è istanza della classe Persona 
if isinstance(studente_1,Persona): 
    print("\nstudente è anche instanza della classe Persona")
# Rutorna true perché studente_1 è un istanza della classe Studente ma è anche un oggetto della classe Persona poichè studente is-a Persona 

if isinstance(fm, Persona):
    print("\nl'oggetto fm è istanza della classe Persona")

# controllo se l'oggetto fm p anche istanza della classe Studente
if isinstance(m, Studente):
    print("\nl'oggetto della classe Persona ed è anche istanza della classe Studente")
else:
    print("\nl'oggetto fm è istnaza della classe ma non è istanza della classe Studente")

# Come posso stabilire se una classe è una sottoclasse di una classe?
# Cotnrollo che la classe Studente sia sottoclasse della classe Persona
# issubclass(Class1, Class2) -> cotnrolla se Class1 sia sottoclasse della classe Class2
# In caso affermativo ->True 
# In caso negativo -> False

if issubclass(Studente, Persona):
    print("\nla classe Studente è sottoclasse della classe Persona")
