from __future__ import annotations
from film import Film
from movie_genres import *

class Noleggio: 
    list_film:list[Film]
    rented_film:dict[int, list[Film]]
    
    def __init__(self, film_list: list[Film]):
        self.list_film = film_list
        self.rented_film = dict()
    
    
    # Metodo per controllare se il film scelto dall'utente è disponibile in negozio
    def isAvaible(self, another_film:Film)->str:
        
        # Itero sugli ID dei film nella lista dei film
        for film in self.list_film:
            
            # Check: richiamo il metodo .isEqual della classe Film:
                # Se .isEqual() == True 
            if film.isEqual(another_film) == True:
                # Inzializzo una variabile a cui assegno valore True
                avaible = True
                
                # Stampo in output il messaggio che il film è disponibile
                
                # Interrompo il ciclo
                break
            elif film.isEqual(another_film)==False:
                
                # Altrimenti se l'ID del film non è presente nella lista 
                # La variabile avaible = False
                avaible = False
                # Stampo in output il messaggio
                
        if avaible == True:
            print(f"Il film scelto è disponibile: {another_film.Title()}, {avaible} ")
            
        else:
            print(f"Il film scelto non è disponibile: {another_film.Title()} ")
        # Restituisco il valore della variabile avaible
        return avaible
    
    
    # Metodo per gestire il noleggio di un film
    def rentAMovie(self,other_film: Film, clientID:int)->str:
        # Check: se il film è disponibile
        if self.isAvaible(other_film):
            # Lo rimuove dalla lista in base al suo valore
            self.list_film.remove(other_film)
            
            # Check se l'id del cliente è presente nel dizionario rented_movie
            if clientID in self.rented_film:
                
                # Appende il film noleggiato alla lista di film noleggiati da quel cliente
                # In base all'id del cliente (la chiave del dizionario)
                self.rented_film[clientID].append(other_film)
            else: 
                # Altrimenti se l'id del cliente non è presente nel dizionario
                # Crea la chiave e associa come valore di quella chiave il film appena noleggiato
                self.rented_film[clientID] = [other_film]
            # Stampo in output l'id del cliente è il titolo del film
            print(f"Il cliente {clientID} ha noleggiato {other_film.Title()}")
        else:
            
            print(f"Non è possibile nolegiare il film {other_film.Title()}")
    
    # Metodo per gestire la restituzione dei film in negozio
    def giveBack(self,A_film:Film, clientID:int, days:int)->str:
        self.rented_film[clientID].remove(A_film)
        self.list_film.append(A_film)
        print(f"Cliente: {clientID}! La penale da pagare per il film {A_film.Title()} è di {A_film.calcolaPenaleRitardo(days)} euro!")
    
    def printMovies(self):
        for films in self.list_film:
            print(f"{films.Title()}- {films.getGenere()}")
    
    
    # Questo metodo stampa l'id del cliente e la lista di film noleggiati
    def printRentMovies(self, ClientID:int):
        # List comprehension:
            # itero sui film nell dizionario rented_film in base alla chiave(l'id del cliente)
            # e mi resitiruisce il titolo dei film perché richiamo il metodo get dei titoli nel file film.py della classe Film
        print(f"ID Cliente: {ClientID}. Lista di film noleggiati: {[f.Title() for f in self.rented_film[ClientID]] }")
    



def main()->None:
    
    
    a1:Action = Action(8, 'Mission: Impossible', 'Azione', 3.00)
    a2:Action = Action(9, 'John Wick', 'Azione', 3.00)
    a3:Action = Action(10, 'The Matrix', 'Azione', 3.00)
    a4:Action = Action(11, 'Mad Max: Fury Road', 'Azione', 3.00)
    a5:Action = Action(12, 'The Dark Knight', 'Azione', 3.00)
    a6:Action = Action(13, 'Gladiator', 'Azione', 3.00)
    a7:Action = Action(14, 'Avengers: Endgame', 'Azione', 3.00)
    
    c1:Comedy = Comedy(15, 'Una notte al museo', 'Commedia', 2.50)
    c2:Comedy = Comedy(16, 'Non ci resta che piangere', 'Commedia', 2.50)
    c3:Comedy = Comedy(17, 'The Hangover', 'Commedia', 2.50)
    c4:Comedy = Comedy(18, 'Benvenuti al Sud', 'Commedia', 2.50)
    c5:Comedy = Comedy(19, 'Superbad', 'Commedia', 2.50)
    c6:Comedy = Comedy(20, 'Scary Movie', 'Commedia', 2.50)
    
    d1:Drama = Drama(21, 'Forrest Gump', 'Drammatico', 2.00)
    d2:Drama = Drama(22, 'La vita è bella', 'Drammatico', 2.00)
    d3:Drama = Drama(23, 'The Shawshank Redemption', 'Drammatico', 2.00)
    d4:Drama = Drama(24, 'Schindler''s List', 'Drammatico', 2.00)
    d5:Drama = Drama(25, 'The Godfather', 'Drammatico', 2.00)
    d6:Drama = Drama(26, 'Titanic', 'Drammatico', 2.00)

    d7:Drama = Drama(27, 'La parola ai giurati', 'Drammatico', 2.00)
    
    n1:Noleggio= Noleggio([
        a1,a2,a3,a4,a5,a6,a7,
        c1, c2,c3,c4,c5,c6,
        d1,d2,d3,d4,d5,d6,d7])
    n1.isAvaible(a1)
    n1.rentAMovie(a3, 12)
    n1.rentAMovie(d4, 12)
    n1.rentAMovie(c6, 12)
    n1.rentAMovie(d7, 12)
    n1.rentAMovie(c2, 12)
    n1.rentAMovie(c2, 12)
    
    n1.giveBack(a3, 12, 4)
    n1.printMovies()
    n1.printRentMovies(12)

if __name__ == "__main__":
    main()