from __future__ import annotations
import math
class Frazione:
    __numeratore:int
    __denominatore:int
    def __init__(self, numeratore, denominatore):
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)
    
    def get_numeratore(self):
        return self.__numeratore
    
    def set_numeratore(self, numeratore):
        if isinstance(numeratore, int):
            self.__numeratore = numeratore
        else:
            self.__numeratore = 13
    
    def get_denominatore(self):
        return self.__denominatore
    
    def set_denominatore(self, denominatore):
        if isinstance(denominatore,int) and denominatore !=0:
            
            self.__denominatore = denominatore
        else:
            self.__denominatore = 5
    def value(self):
        result = self.__numeratore/self.__denominatore
        return round(result, 3)
    def __repr__(self):
        return f" {self.get_numeratore()}/{self.get_denominatore()}."
    def __str__(self):
        return f"{self.get_numeratore()}/{self.get_denominatore()}"
    
    # esercizio 8.B
    def mdc(self,x: int, y: int)-> int:
        if math.gcd(x,y)>0:
            return math.gcd(x,y)
        else:
            return 1
        
    # esercizio 8.C
    def semplifica(self, l: list[Frazione])->list[Frazione]:
        l_irrud:list[Frazione] = []
        for f in l:
            num = f.get_numeratore()
            den = f.get_denominatore()
            mdc = math.gcd(num, den)
            if mdc ==1:
                l_irrud.append(f)
            else: 
                nuova_frazione = Frazione(num//mdc, den//mdc)
                l_irrud.append(nuova_frazione)
        return l_irrud
        
    # 8.D
    def fractionCompare(self, l: list[Frazione],l_irrud:list[Frazione]):
        for orig, sempl in zip(l, l_irrud):
            print(f"Valore frazione originale: {orig.value()} --- Valore frazione ridotta: {sempl.value()}")
        
    
    # 8.E
    

if __name__ == "__main__":
    
    
    f:Frazione = Frazione(15,5)
    print(f)
    print(f.value())
    print(f.mdc(13,7))
    print(f.mdc(20,10))
    lista:list = [Frazione(3,4), Frazione(6,9), Frazione(4,4)]
    irriducibili = f.semplifica(lista)
    for frazioni in irriducibili:
        print(frazioni)
    
    f.fractionCompare(lista, irriducibili)
    # print(f.fractionCompare([[Frazione(3,4), Frazione(6,9), Frazione(4,4)]],[Frazione(3,4), Frazione(6,9), Frazione(4,4)]))
    # print(f.semplifica([Frazione(1,2,3)]))
    
    
    