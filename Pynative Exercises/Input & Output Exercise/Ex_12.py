"""
Crea un menu interrativo basato su 3 opzioni: 
1. Say hello
2. Calculate Square
3. exit 
"""
from typing import Any

def menu(option:str)->Any: 
    cont= 0
    while True: 
        
        if option == 'say hello': 
            print('Hello There!')
            
            
            
        elif option == 'calculate square': 
            try: 
                lato_1:int = int(input('Inserisci il lato del quadrato: '))
            
                print("Calcolo del perimetro e dell'area:")
                perimetro:int = lato_1*4 
                area:float = lato_1**2
                print(f"Il perimetro è: {perimetro}.\n\
L'area del quadrato è: {area:.2f} ")
            except ValueError: 
                print('Input non valido. Inserire un numero intero')
            
        elif option == 'exit':
            print('Done!')
            break
        else: 
            print('Input non valido riprova')
        # cont+=1


try: 
    prompt:str = input('Inserisci un opzione: ')
except ValueError: 
    print('Input non valido!')

def main():
    menu(prompt)

if __name__ == "__main__":
    main()