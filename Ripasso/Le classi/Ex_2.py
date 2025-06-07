class Movie:
    def __init__(self, movie_id: str, title:str, director:str, is_rented: bool = False):
        self.movie = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
    
    # Questa funzione contrassegna il film per vedere se è noleggiato o meno
    def rent(self):
        if self.is_rented:
            # Questo flag cambia dinamicamente lo stato dell'attributo is_rented da False a True
            self.is_rented = True
            return f"{self.title}è gia noleggiato "
        else: 
            return f"{self.title} è disponibile"
        
    
    # Questa funzione contrassergna il film come restituito
    def return_movie(self):
        if self.is_rented:
        # Questo flag resetta lo stato di is_rented da True a False 
            self.is_rented = False
            return f"{self.title} è gia noleggiato"
        else: 
            return f"{self.title} non è stato noleggiato da questo cliente"
    
    # Questo metodo permette di leggere gli oggetti movie in modo leggibile per gli user
    def __str__(self):
        return f"{self.title} "
    
    # Questo metodo permette far visualizzare gli elementi della lista rented_movies in modo leggibile per il debug
    def __repr__(self):
        return self.__str__()

class Customer:
    def __init__(self, customer_id:str, name:str, rented_movies:list[Movie] = None):
        if rented_movies is None:
            rented_movies = []
        self.customer = customer_id
        self.name = name
        self.rented = rented_movies
    
    # def __str__(self):
    #     return f"{self.customer} {self.name} {self.rented}"
    
    # def __repr__(self):
    #     return self.__str__()
    # Questa funzione  aggiunge oggetti movie e torna una lista di oggetti movie 
    def rent_movie(self, movie:Movie) ->list[Movie]:
        # Se l'attributo di movie is_rented è false appende l'oggetto movie alla lista
        if movie.is_rented == False:
            self.rented.append(movie)
            return self.rented
        else:
            return f"Il film '{movie.title}' è già noleggiato."
    
    def return_movie(self,movie: Movie):
        if movie in self.rented:
            self.rented.remove(movie)
            return self.rented
        else:
            return f"Il film '{movie.title}' non è stato noleggiato da questo cliente."



class VideoRentalStore:
    def __init__(self, movies:dict[str,Movie], customers:dict[str, Customer]):
        self.movies = movies
        self.customers = customers
    
    def __str__(self):
        return f"{self.movies}, {self.customers}"
    
    def __repr__(self):
        return self.__str__()
    
    # Questo metodo aggiunge un nuovo film 
    def add_movie(self,movie_id:str, title:str, director:str):
        
        # Cerca l'id del film (ovvero la chiave) nel dizionario movies
        if movie_id in self.movies:
            return f"Il film con ID {movie_id} esiste già"
        else:
            # Se la chiave non è presente nel dizionario, si crea un nuovo oggetto Movie e lo si aggiunge come valore della chiave
            new_movie = Movie(movie_id, title, director )
            self.movies[movie_id] = new_movie
            return self.movies
        
    # Aggiunge un nuovo cliente al dizionario customers
    def register_customer(self,customer_id:str, name:str):
        # Cerca se la chiave (cioè l'id del cliente) è gia presente nel dizionario
        if customer_id in self.customers :
            return f"Il cliente con ID '{customer_id}' è gia registrato"
        else:
            # Se l'id non è presente crea un nuovo oggetto Customer e lo assegna come valore alla chiave customer_id
            new_customer:Customer = Customer (customer_id, name)
            self.customers[customer_id] = new_customer 
            return self.customers
    
    
    # Questo metodo permette al cliente di noleggiare un film se sia il cliente che il film sono presenti nel videonoleggio
    def rent_movie(self, customer_id:str, movie_id:str):
        # Se la chiave customer_id o la chiave movie_id non sono dentro i rispettivi dizionari solleva l'errore
        if customer_id not in self.customers or movie_id not in self.movies:
            return "Cliente o film non è stato trovato"
        # Prende l'oggetto Customer
        customer = self.customers[customer_id]
        # Prende l'oggetto Movie
        movie = self.movies[movie_id]
        if not movie.is_rented:
            movie.rent() #Richiamando il metodo rent() lo stato viene cambiato a noleggiato
            customer.rent_movie(movie) #Aggiunge il film alla lista del cliente dei film noleggiati
            return f"{customer.name} ha noleggiato il film {movie.title}"
        else:
            return f"Il film {movie.title} è già noleggiato"
    
    # Questo metodo permette di restituire un film se il cliente o il film sono presenti nel videonoleggio
    def return_movie(self,customer_id:str, movie_id:str):
        if customer_id not in self.customers or movie_id not in self.movies:
            return "Il Cliente o il Film non sono stati trovati"

        customer = self.customers[customer_id]
        movie = self.movies[movie_id]
        if movie.is_rented == True:
            movie.return_movie()
            customer.return_movie(movie)
            return f"{customer.name} ha restituito il film {movie.title} "
        else:
            return f"Il film {movie.title} è già noleggiato"
        
    # Questo metodo restituisce la lista di film noleggiati dal cliente
    def get_rented_movies(self, customer_id:str)->list[Movie]:
        # Se la chiave customer_id è nel disizionario customer, restituisce il dizionario con la chiave customer_id è il suo valore associato ovvero la lista rented_movies
        if customer_id in self.customers:
            return self.customers[customer_id].rented
        else:
            return f"Cliente non tovato: {[]}", 



m:Movie = Movie ("34tr", "La compagnia dell'anello", "Peter Jackson")
print(m.rent())
m_2: Movie = Movie("35tr", "Le due torri", "Peter Jackson")
print(m_2.return_movie())
m3:Movie = Movie("003", "Batman", "Nolan") 
m4:Movie = Movie("004", "Pulp Fiction", "Tarantino") 



m1 = Movie("001", "Matrix", "Wachowski", False)
m2 = Movie("002", "Inception", "Nolan", False)

print("------------------------------------------------")

c1 = Customer("C123", "Luca", [m3, m4])
print(c1.rent_movie(m1))

print(c1.rent_movie(m2))  
print(c1.return_movie(m1))
print("-----------------------------")
v1:VideoRentalStore = VideoRentalStore({"001": m1}, {"002": c1})


print(v1.add_movie("389TRS", "Il grande Lebowski", "Joel ed Ethan Coen"))
print(v1.add_movie("547TRS", "The Prestige", "Nolan"))

v1.register_customer("C123", "Luca")

v1.rent_movie("C123", "001")
v1.rent_movie("C123", "002")

print("Film noleggiati da Luca:")
print(v1.get_rented_movies("C123"))

v1.return_movie("C123", "001")

print("Film noleggiati da Luca dopo restituzione:")
print(v1.get_rented_movies("C123"))
