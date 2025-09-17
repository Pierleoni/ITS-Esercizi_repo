"""
Conta il totale delle cifre in un numero 
"""

# Definisco una funzione con un solo parametro in input
def total_digit(number:int)->int:
    
    # Inizializzo una variabile contatore a 0 
    cont:int = 0
    
    # Fin tanto che il numero è diverso da 0 
    while number !=0: 
        
        # Elimino l'ultima cifra a destra del numero
        number = number //10
        
        # Aggiorno il contatore
        cont+=1
        
    # Il numero di iterazioni sarà uguale al totale di cifre del numero, percio stampo il contatore 
    print(cont)



def main():
    total_digit(75869)

if __name__ == "__main__":
    main()