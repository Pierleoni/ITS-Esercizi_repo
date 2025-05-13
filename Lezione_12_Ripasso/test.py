# Dal modulo esercizio Ex_Syst_Gest_Catalog_Film.py importare la classe MovieCatalog
from Ex_Syst_Gest_Catalog_Film import MovieCatalog

# creare un oggetto della Classe Movie catalog
catalog:MovieCatalog = MovieCatalog() #adesso l'init non chiede parametri in input per cui non metto nessun argomento in input

# Aggiungere un regista e dei film al catalogo
catalog.add_movie("Steven Spielberg", ["Casper", "Ritorno al futuro"])

# Visualizziamo il catalogo
print(catalog.getCatalog())

catalog.add_movie("Steven Spielberg", ["E.T."])
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Le Iene", "The Hateful Eight", "Bastardi senza gloria"])
print(catalog.getCatalog())

print("-------------------------------------")
catalog.remove_movie("Steven Spielberg", "E.T.")

print(catalog.getCatalog())

catalog.remove_movie("Steven Spielberg", "Casper")
print(catalog.getCatalog())

catalog.remove_movie("Steven Spielberg", "Ritorno al futuro")
print(catalog.getCatalog())
print("-------------------------------------------------")

catalog.add_movie("Lars Von Trier", ["Dogville", "Nynphomaniac", "Il grande capo"])
catalog.list_directors()
print(catalog.getCatalog())