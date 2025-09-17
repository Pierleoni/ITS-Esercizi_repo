"""
Prendere un integer ed elevarlo per il suo esponente
"""

def exponent(base:int, exp:int)->int:
    
    # La variabile num punta al valore di exp per una maggiore reusibilità
    num = exp
    # Inzializzo variabile result con valore 1 per moltiplicazioni ripetute
    result = 1
    
    # Fintanto che l'esponente è maggiore di 0
    while num > 0:
        
        # result viene moltiplicato per la base
        result = result * base
        # e num decrementa di 1
        num = num - 1
    
    
    return f"{base} elevato alla potenza di {exp}: {result}"


def main():
    print('Caso 1:')
    print(exponent(2,5))
    print('Caso 2:')
    print(exponent(5,4))
    

    print(exponent('H', -2))
if __name__ == "__main__":
    main()