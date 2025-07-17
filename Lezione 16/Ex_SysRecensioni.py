class Media:
    title:str
    reviews:list[int]
    def __init__(self, title: str, reviews:list[int]):
        self.setTitle(title)
        self.setReviews(reviews)
    
    def get_title(self):
        return self.title 
    
    def setTitle(self, title):
        self.title = title
    
    def get_reviews(self):
        return self.reviews
    
    def setReviews(self, reviews):
        self.reviews = reviews
    
    def aggiungiValutazione(self, voto:int):
        if voto in range (1,6):
            self.reviews.append(voto)
        else:
            raise ValueError(f"Errore! {voto} non è un valore compreso tra 1 e 5")
        self.voto = voto 
        
    def media(self)->float|int: 
        
        media =sum (self.reviews)/float(len(self.reviews))
        return media 
        
    
    def rate(self):
        media = self.media()
        if media <= 1:
            return"Terribile"
        elif media<= 2:
            return"Brutto"
        elif media<= 3:
            return"Normale"
        elif media<= 4:
            return"Bello"
        elif media<= 5:
            return"Grandioso"
        else:
            return
    
    
    def ratePercentage(self,voto: float|int)-> float:
        voti = self.reviews.count(voto)
        percentuale = (voti/len(self.reviews))*100
        return f"{percentuale}%"
        

    def recensioni(self):
        return f"Titolo del film: {self.get_title()}\n Voto Medio:{self.media():.2f}\n Giudizio: {self.rate()}\n Terribile: {self.ratePercentage(1)}\n  Brutto: {self.ratePercentage(2)}\n Normale: {self.ratePercentage(3)}\n Bello: {self.ratePercentage(4)}\n Grandioso: {self.ratePercentage(5)}"
        
        


class Film(Media):
    titolo:str
    
    def __init__(self, title, reviews):
        super().__init__(title, reviews)
        self.setTitle(title)

def main()->None:
    m:Media = Media("Boh", [1,2,3,4,5,6,7,8,9,2,2,2])
    print(f"Media voti: {m.media()}")
    m.rate()
    print(m.media())
    print(m.ratePercentage(3))
    f:Film = Film("The Shawshank Redemption", [1, 2, 3, 4, 5, 5, 5, 4, 3, 2])
    print(f.recensioni())

    




if __name__ == "__main__":
    main()