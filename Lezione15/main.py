with open("example.txt", mode="w", encoding="utf-8") as file:
    message:str = "Hello, World!\n"
    # Sovrascrive il contenuto del corpo su example.txt, se non avessi avuto questo file me lo creava
    written_char:int = file.write(message)
    """
    quindi in questa maniero ho aperto un file e ci ho sovrascritto sopra, usando with non devo specificare che devo chiudure un file me lo chiude da solo quando esco dal programma.
    
    
    """    
    print(f"Message is: {message} \nWritten characters: {written_char}")

"""
La parola chiave with viene usata per i gestire i contesti:
creiamo una nuova classe chiamata StopWatch
"""

import time
class StopWatch:
    """
    il debbuger fa vedere i vlaori delle variabili in tempo reale: in questo caso sul questo self mi farà vedere in tempo reale l'indirizzo di memoria del self
    """    
    def __init__(self):
        """
        questo due variabili definisco l'inizio o la fine 
        """        
        self.start_time = None
        self.end_time = None
    
        """
        la funzione speciale enter:
        non si usa di solito ma solo con with
        """    
    def __enter__(self):
        """
        In questo caso memeorizza il tempo corrente, e come dire al proprio computer che ore sono e memorizza il tempo corrente nella variabile
        self.start_time.
        
        """        
        self.start_time = time.time()
        return self
    """
    serve una funzione chiamata exit () per uscire, cioè stampare il tempo 
    
    """    
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.8f} seconds")
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"An erro occured: {exc_value}")
            print(f"Traceback: {traceback}")
        # Se mettiamo False l'eccezione, se ce stata, ritorna al chiamaente, se mettiamo True l'eccezione, se ce stata, rimane confinata all'intenro della funzione di exit
        return False
        








pass
# Cliccando sul pallino rosso a sinistra del numero della riga ho inserito un breakpoint: vuol dire che quando il debbuger viene runnato si fermarà alla linea dove è stato insertito il breakpoint.
# Quando si ferma alla linea del breakpoint questa viene evidenziata per dire che è la seconda parte che verra controllata dal debbuger 
with StopWatch():
    print("Hello, World")
    time.sleep(2)
    print("Goodbye, World")