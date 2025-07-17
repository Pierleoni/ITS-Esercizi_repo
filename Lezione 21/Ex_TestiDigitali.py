import re
class Documento:
    text:str
    
    def __init__(self,testo:str ):
        
        self.setText(testo)
    
    def getText(self):
        return self.text
    
    def setText(self, testo):
        self.text = testo
        
    
    def isInText(self, key_word)-> bool:
        if key_word in self.text:
            return True
        else:
            return False
    
    
    def __str__(self):
        return f"{self.getText()}"
        


class Email(Documento):
    mittente:str
    destinatario:str
    titolo_messaggio:str
    
    def __init__(self, mittente:str, destinatario:str, titolo_messaggio:str,testo):
        super().__init__(testo)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo_messaggio)
        
        
    
    # get per il mittente
    def mitt(self):
        return self.mittente
    
    # Setter per il mittente
    def setMittente(self, mittente):
        re.fullmatch(r' [^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+ ', mittente)
        self.mittente = mittente
    
    
    # Getter per il destinatario
    def dest(self): 
        return self.destinatario
    
    # Setter per il destinatario
    def setDestinatario(self, destinatario):
        self.destinatario = destinatario
        
    
    # gettter per il titolo del messaggio
    def titolo(self):
        return self.titolo_messaggio
    
    
    # setter per il titolo del messaggio
    def setTitolo(self, titolo):
        self.titolo_messaggio = titolo
    
    def getText(self):
        
        return f"Da:{self.mitt()}\n Titolo: {self.titolo()}\n a: {self.dest()} \nMessaggio: {super().getText()}.\n "
    
    def writeToFile(self):
        with open("C:/Users/Project Lead/Desktop/Esercizi Programazzione ITS/Progetti_Py/Lezione 21/email1.txt", "w",encoding="utf-8") as file:
            return file.write(self.getText())


class File(Documento):
    nome_percorso: str
    def __init__(self, nome_percorso: str):
        self.nome_percorso = nome_percorso

        super().__init__(self.leggiTestoDalFile())

    
    def percorso(self):
        return self.nome_percorso 
    
    def setPercorso(self, nome_percorso):
        self.nome_percorso = nome_percorso
    
    def leggiTestoDalFile(self):
        percorso_file = self.percorso()
        with open(percorso_file, "r", encoding="utf-8") as file:
            return file.read()
            
    def getText(self):
        return f"Percorso: {self.percorso()}\nContenuto: {super().getText()}"






'''
Per aprire un file in Python devo scrivere 'with open('inserire il path del file', modalità d'accesso(w→write, a→append[appende il contenuto quindi non sovrascrive], r->read)) as file'
file.modalitaD'acceso()
se scrivo file.write(specificare l'oggetto da scrivere)
file.read()-> non serve scrivere nulla come argomento perché sta leggendo il file
file.readfile() -> legge riga per riga il file e lo restiruisce tutto su una stringa
file.readfiles()-> legge tutte le righe di tutto il file, utile da utilizzare in ciclo for
'''