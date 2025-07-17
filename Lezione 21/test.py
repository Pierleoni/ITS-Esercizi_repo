from Ex_TestiDigitali import Documento, Email, File

def main():
    # Blocco per l'oggetto Email
    e:Email = Email("Marco", "Andrea", "Importante!!!", "Ghesboro, vez!")
    print(e.getText())
    
    
    # Blocco per testare un oggetto File
    f:File = File ("C:/Users/Project Lead/Desktop/Esercizi Programazzione ITS/Progetti_Py/Lezione 21/document.txt")
    print(f.getText())
    print("--------------------------------------------------------")
    e2:Email = Email ("Marco", "Vittorio", "Daje", "Possiamo incontrarci?")
    
    e2.writeToFile()
    print(f"Contenuto:\n {e2.getText()}")
    
    print(e2.isInText("incontrarci"))
    
    print(e2.isInText("percorso"))



if __name__ == "__main__":
    main()