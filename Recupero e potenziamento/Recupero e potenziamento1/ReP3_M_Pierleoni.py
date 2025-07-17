# from __future__ import annotations
import random

class Creatura:
    def __init__(self, nome: str):
        self.setNome(nome)

    def get_nome(self):
        return self.nome

    def setNome(self, nome: str):
        # il metodo strip leva tutti i caratteri bianchi a inizio e fine stringa
        if isinstance(nome, str) and nome.strip():
            self.nome = nome
        else:
            self.nome = "Creatura Generica"

    def __str__(self):
        return f"Creatura: {self.nome}"


class Alieno(Creatura):
    def __init__(self, nome: str):
        self._setMatricola()  
        
        if not isinstance(nome, str):
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            nome = f"Robot-{self.matricola}"
        super().__init__(nome)  
        self._setMunizioni()

    def _setMatricola(self):
        self.matricola = random.randint(10000, 90000)

    def _setMunizioni(self):
        self.munizioni = [i**2 for i in range(0,15)]

    def getMatricola(self):
        return self.matricola

    def getMunizioni(self):
        return self.munizioni

    def __str__(self):
        return f"Alieno: {self.nome}"




class Mostro(Creatura):
    assalto:list[int]
    def __init__(self, nome, urlo_vittoria:str, gemito_sconfitta:str):
        self._setVittoria(urlo_vittoria)
        self._setSconfitta(gemito_sconfitta)
        self._setAssalto()
        super().__init__(nome)
        
    
    def getUrlo(self):
        return self.urlo_vittoria
    
    def getGemito(self):
        return self.gemito_sconfitta
    
        
    def _setAssalto(self)->list[int]:
        self.assalto = random.sample(range(1,101), 15)
    
    def get_assalto(self):
        return self.assalto
    
    def _setVittoria(self, vittoria:str):
        if isinstance(vittoria, int|float) or isinstance(vittoria, bool ):
            self.urlo_vittoria = "GRAAAHHH"
        else:
            self.urlo_vittoria = vittoria
            
    def _setSconfitta(self, sconfitta: str):
        if not isinstance(sconfitta, str) or not sconfitta.strip():
            self.gemito_sconfitta = "Uuurghhh"
        else:
            self.gemito_sconfitta = sconfitta
    
    def __str__(self):
        # per restutire l'alternarsi dei caratteri in maiuscoli e minuscoli del nome uso un ciclo for
        res = ""
        for idx in range(len(self.nome)): #itera sulla stringa usando i suoi indici
            if idx%2 ==0:
                res +=self.nome[idx].lower()
            else:
                res += self.nome[idx].upper()
        return f"Mostro: {res}"
        


def pariUguali(a:list[int], b:list[int])->list[int]:
    c:list[int] = []
    for x, y in zip(a,b):
        if x %2 and y%2==0:
            c.append(1)
        
        else:
            c.append(0)
        return c
    
    

def combattimento(a:Alieno, m: Mostro):
    if not isinstance(a, Alieno) and isinstance(m, Mostro):
        print(f"{a} non è un Alieno, {m} non è un Mostro")
        return None
    elif isinstance(a,Alieno) and isinstance(m, Mostro):
        result = pariUguali(a.getMunizioni(), m.get_assalto())
        # Il metodo .count conta quante volte un determinato elemento compare nella lista result.
        # In questo caso conta quanti 1 ci sono nella lista, e se sono più di 4 stampa l'urlo di vittoria *3
        if result.count(1)>4:
            print(m.getUrlo()*3)
            return m
        else:
            print(m.getGemito())
            return m 

def proclamaVincitore(c:Creatura):
    if not isinstance(c, Alieno) and not isinstance (c,Mostro):
        raise ValueError(f"Errore! {c} non è un istanza ne di Alieno ne di Mostro")
    larghezza = len(c.__str__())+10
    altezza = 5
    
    for i in range(altezza):
        for j in range(larghezza):
                
                if i == 0 or i == (altezza - 1) or j == 0 or j == (larghezza - 1):
                    print('*', end='')
                elif i == 2 and j == 5:
                    print(c, end='')
                    
                    print('     *', end="")
                    break
                else:
                    print(' ', end='')
        
        print()





if __name__ == "__main__":
    a1 = Alieno("Robot-12345")
    print(a1)

    a2 = Alieno("AlienoStrano")
    print(a2)

    a3 = Alieno(" ")
    print(a3)

    m = Mostro("Godzilla", "AAAAAAA", "uuuuuu")
    print(m)
    
    vincitore = combattimento(a1, m)
    print(f"Vincitore: {vincitore}")
    
    a3:Alieno = Alieno("Robot-41119")
    
    
    m1:Mostro = Mostro("gOrThOr", "GRAAAAAAAHHHH", "iiiiiiiiuuuu")
    
    vincitore2 = combattimento(a3, m1)
    print(f"Il vincitore è {vincitore2}")
    print("---------------------")
    proclamaVincitore(m1)
    



