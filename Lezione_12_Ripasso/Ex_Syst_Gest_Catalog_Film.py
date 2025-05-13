class MovieCatalog:
    '''
    Attributi della classe Catalog:
    1.L'attributo set.catalog(un dizionaro):dict[str,list[str]]
    '''
    def __init__(self)->None:
        '''
        il parametro initi non deve prendere nessun parametro in input, questo perché:
        quando creiamo il parametro catalog deve essere vuoto all'inzio e poi con i metodi add() e remove() aggiungo e rimuovo i fil dal catalogo
        '''
        self.setCatalog()
        
    '''
    andiamo ad impostare un metodo setter,
    in questo caso imposta il valore dell'attributo self.catalog
    '''
    def setCatalog(self)->None:
        self.catalog:dict[str, list[str]] = {}
    
    """
    Metodo getter che ritorna il vlaore dell'attributo catalo
    """  
    # def __str__(self):
    #     return f""
    def getCatalog(self) ->dict[str, list[str]]:
        return self.catalog
    
    """
    Metodo della classe MovieCatalog:
    
    metodo che aggiunge una lista di film al catalogo
    """    
    def add_movie(self,director_name:str, movies:list[str])->None: 
        """
        dobbiamo controllare se director name non sia una stringa vuota:
        se scrivo if director_name: sto dicendo che se la stringa è vuota allora esegui quel codice,
        ma se scrivo if not director_name sto dicendo che se la stringa non è vuota allora esegui quel codice
        """ 
        # Check valore valido di director_name
        if not director_name:
            print("Fornire un nome valido per il regista")
        # Check valore valido di movies
        elif not movies:
            print("Fornire una lista di film che non sia vuota")
        # Se i dati inseriti sono validi
        else:
            # Se il regista è presente nel catalogo, aggiungi i film
            if director_name in self.catalog:
                # Aggiungere film al catalogo
                for movie in movies:
                    # Controlliamo se i film della lista movies siano già stati inseriti dentro al catalogo
                    """
                    Sto dicendo che se il film generico è all'interno della lista movies dato uno specifico regista(cioè la key del dizionario),
                    ci sta dicendo che è la lista di tutti i film prodotti attraverso la key del dizionario del nome del regista
                    dizionario[key] -> ritorna il valore corrispondente alla chiave key
                    dove self.catalog è un dizionario,
                    director_name è la chiave
                    self.catalog[director_name] è il valore corrispondente alla chiave directory_name
                    """ 
                    if movie in self.catalog[director_name]: #self.catalog[director_name] è la lista dei film prodotti dal regista director name
                        print(f"Il film {movie} è gia presente nel catalogo")
                    # Nel caso in cui un film della lista movies non è già presente nel catalogo
                    else:
                        self.catalog[director_name].append(movie)
            # se il regista non è presente nel catalogo creare un nuovo record, che ha come chiave il nome del regista
            # e come valore la lista movies
            else:
                self.catalog[director_name]=movies
    def remove_movie(self,director_name: str, movie_name: str )->None:
        # Check valore valido di director_name
        if not director_name:
            print("Fornire un nome valido per il regista")
        elif not movie_name :
            print("Fornire una lista di film che non sia vuota")
        else:
            if director_name in self.catalog and movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)  # Rimuovi il film dal regista
            if not self.catalog[director_name]:  # Se il regista non ha più film
                del self.catalog[director_name]  # Rimuovi il regista dal catalogo
        return self.catalog  # Restituisci il catalogo aggiornato
    
    def list_directors(self)-> list[str]:
        for keys in self.catalog.keys():
            
            return list(keys)
        # else:
        #     print("Aggiungere un nome valido per il Regista")


