from __future__ import annotations
from film import *
from movie_genres import *
from noleggio import *


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
    
    print ("Quale film vuoi nolleggiare?")
    n1.rentAMovie(a1, 2)
    n1.rentAMovie(c4, 2)
    n1.rentAMovie(c4, 3)
    n1.rentAMovie(d7, 2)
    n1.giveBack(c4, 2, 3)
    print()
    print("Lista di film presenti in negozio:")
    n1.printMovies()
    
    

if __name__ == "__main__":
    main()