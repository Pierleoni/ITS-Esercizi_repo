# Importo il modulo math per usare il pi greco
import math

class Shape:
    # Affinche l'area di una figura ritorni il calcolo devo implementare il metodo area nelle sottoclassi usando l'overriding
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        
        """
        La formula dell'area di un cerchio è:
        A = pi*raggioDelCerchio^2 
        
        """        
        return math.pi * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        """
        La formula dell' area del quadrato è
        A = lato^2 
        """ 
        # Ritorna il lato elevato alla seconda
        return self.side**2
        # Un altro modo è:
        #! return self.side * self.side

"""
Il metodo area() della superclasse non contiene logica concreta (a differenza dell'esercizio 6),
ma funge da contratto: 
!stabilisce che ogni sottoclasse deve implementare il proprio calcolo dell'area.

!Di conseguenza, ogni sottoclasse deve riscrivere da zero il metodo area(). 
Se si provasse a chiamare super().area() all'interno della sottoclasse, 
verrebbe immediatamente sollevato un NotImplementedError, 
poiché la superclasse non fornisce alcuna logica da riutilizzare.
"""

def main():
    shapes = [Circle(5), Square(7), Circle(3)]

    for shape in shapes:
        print(shape.area())

if __name__ == "__main__":
    main()