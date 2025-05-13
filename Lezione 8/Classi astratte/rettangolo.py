'''
creo questo file rettangolo.py per definire la classe rettangolo che eredità dalla classe FormaGenerica
'''
from formaGenerica import FormaGenerica
class Rettangolo(FormaGenerica):
    '''
    quello che mi apsetto dalla classe rettangolo è che fornisca un implemtazione del metodo draw()
    '''
    def __init__(self):
        super().__init__()
        self.setShape("rettangolo")
        
    def draw(self)->None:
        print(f"\n{self.getShape()}:\n")
        '''
        vediamo come fare i disegni in python:
        vogliamo disegnare un rettngolo che ha la base lunga 10 asterischi e l'altezza lunga 5 asterischi, ho bisgono di due cili for annidati:
        il primo for gestisce la prima variabile i che socrre gli asterischi in verticalmente
        e un altro for che gestisce la variabile j che scorre gli asterischi orrizontalemte.
        Quindi per disegnare le forme devo capiure le i e le j come sono in relzione tra loro:
        inziamo dal lato A : quando voglio definire questo lato il valore di i è sempre uguale a 0 mentre j e compreso tra 0 e 9
        lato b: questo lato si estende sulla colonna dove j è sempre uguale a 0 e i varia tra 0 e 4 quindi la formula sara i <=5 and j==0
        lato c: si comporta in maniera analoga i<5 and j==10-1 scrivo così perchè in questo caso bisgona generealizzare il più possibile.
        lato d: simile al caso del lato a i=5-1 and j<10
        '''
        # Istruzioni per disegnare un rettangolo 5*10
        
        # outer for
        for i in range(5):
            # inner for
            for j in range(5*2):
                # lato a e lato b del rettangolo 
                if i == 0 or i == 5-1:
                    print("*", end="")#questo end significa che andare accappo continuamo sulla stessa linea, perchè di defualt Python dopo aver eseguito un print va accapo
                # Lato b e lato c del rettangolo
                elif j ==0 or j==(5*2)-1:
                    print("*", end="")
                # se queste due condizioni non sono verificate stampare uno spazio biano
                else:
                    print("", end="")
            print("\n", end="")