from forma import *

class Quadrato(Forma):
    lato:int|float
    lunghezza_lato:int
    
    def __init__(self, lato_quadrato:int|float):
        super().__init__()
        self.nome = 'Quadrato'
        self.setLato(lato_quadrato)
    
    
    def setLato(self, lato:int|float)->None:
        if lato: 
            self.lato = lato
        else:
            raise ValueError('Errore! Il lato non può essere una stringa vuota')
    
    def getLato(self)->int|float:
        return self.lato
    
    def getArea(self):
        super().getArea()
        area:int|float = self.getLato()**2
        return area
    
    def render(self):
        super().render()
        pass


# class FormaGenerica(ABC):
#     @abstractmethod
#     def draw(self) -> None:
#         pass  # Metodo astratto: nessun contenuto qui

#     def setShape(self, shape: str) -> None:
#         if shape:
#             self.shape = shape
#         else:
#             print("Shape non può essere una stringa vuota")

#     def getShape(self) -> str:
#         return self.shape