"""
Visualizza i numeri decimali 
"""

def octal(n:int)->str: 
    
    # tramite la f-literal posso formattare l'output del numeri in input senza il prefisso 0o
    """
    - : → introduce le opzioni di formattazione
    - o → specifica che il numero deve essere convertito in ottale
    
    
    Quind f"{n:0}" significa: 
        inserisci dentro la stringa il valore di n, 
        formattato in base ottale (senza prefisso 0o)
    """    
    print(f"{n:o}")
    


def main():
    octal(8)

if __name__ == "__main__":
    main()