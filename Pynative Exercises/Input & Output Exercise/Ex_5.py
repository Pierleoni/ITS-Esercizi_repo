"""
Accetta una lista di 5 numeri con la virgola dati in input dall'utente
"""

def five_nums(): 
    numbers:list[float] = list()
    cont = 0
    while cont <5: 
        prompt:float = float(input("Digita il numero qui: "))
        if prompt <=0:
            print("Errore!")
        else: 
            numbers.append(prompt)
        
        cont+=1
    return numbers

def main():
    print(five_nums())

if __name__ == "__main__":
    main()


