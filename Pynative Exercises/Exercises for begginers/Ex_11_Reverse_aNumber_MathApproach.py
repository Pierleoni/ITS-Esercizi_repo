
"""
Prendere ogni cifra da un numero mettendole in ordine inverso
"""


def reverse_num(number:int)->int:
    # Variabile per storare il numero reversato
    rev_num:int = 0
    while number>0:
        # Estrago l'ultima cifra e la salvo in una variabile 
        rem:int = number%10 
        # Aggiorno il numero inverso spostadomi a sinistra delle cifre 
        rev_num = (rev_num*10) +rem
        
        # Elmino l'ultima cifra da number
        number = number //10
        
        # print(f"rem={rem}, rev_num={rev_num}, number={number}")
    return rev_num, 

def main():
    print(reverse_num(1234))
    print(reverse_num(7536))

if __name__ == "__main__":
    main()