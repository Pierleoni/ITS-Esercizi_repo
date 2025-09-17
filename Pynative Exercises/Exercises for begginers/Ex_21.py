"""
Controlla se una stringa inserita dall'utente contiene
una qualsiasi cifra numerica
"""

def check_str(stringa: str): 
    for chars in stringa:
        if '0' <= chars <= '9':
            return True
    return False



def main():
    user_str:str = input("Enter a string:")
    
    
    if check_str(user_str):
        print('La stringa contiene almeno una cifra numerica')
    else: 
        print("La stringa non contiene nessuna cifra numerica")

if __name__ == "__main__":
    main()