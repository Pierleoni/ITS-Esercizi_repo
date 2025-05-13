'''
creaimo creare una classe Forma generica, ed deve essere una classe base per tutte le altre classi,
deve contenre un metodo draw()
'''

from abc import ABC, abstractmethod
'''
il modulo abc devo imporate la classe ABC(Abstract base class)

'''

class FormaGenerica(ABC): #sto dicendo che forma generica deriva dalla classe ABC del modulo abc
    
    '''
    Dobbiamo indicare a Python che il metodo draw() è un metodo astratto per farlo:
    '''
    @abstractmethod
    # Per definire un metodo astratto uso un decorator e indico con l'abstract method a Python che questo metodo è astratto, 
    # quindi non ci apsettiamo un corpo di questo metodo in questa classe ma saranno le classi figlie ad implementare questo metodo.
    
    
    
    def draw(self)->None:
        
        '''
        come definiamo questo metodo? Dobbiamo definire un metodo che in output ci restituisca in forma generica, ma come disegno una forma generica e quale può essere una forma genreica?
        Io posso disengare un trinagolo, rettangolo, etc. ma non posso sapere qual'è la forma genrica geometrica di una forma generica geometrica, questo perché essendo una forma generica non so definire la forma a priori.
        posso inventarmi un metodo draw() per questa classe e tramite il polimormismo o overriding vado a definire le classi Trinagolo, quadrato o posso usarel e classi astratte:
        un metodo astratto significa che ha solo la sua deinizione ma non ha contentuto, ovverro dentro la classe forma fenerica c'è un metodo draw() ma non ha corpo o conetutno e quindi dovrò pubblicare le sottoclassi per fonrire un implemetazione del metodo draw.
        Quindi se di una classe dichiaro il metodo astratto posticipo il suo contentuo senza definire cosa fa il metodo in questione.
        Quello che si fa di solito e definire un metodo astratto all'intenro di una classe base e abbiamo definito un metodo draw()
        Voglio che siano le sotto classi di forma generica dare un implemtazione di questo metodo
        Una classe astratta è una classe che contiene almeno un metodo astratto
        '''
        '''
        definiamo il metodo concreto setShape()
        '''
        def setShape(self, shape:str)->None:
            if shape:
                self.shape = shape
            else:
                print("Shape non può essere una stringa vuota")
        def getShape(self)->str:
            return self.shape
        