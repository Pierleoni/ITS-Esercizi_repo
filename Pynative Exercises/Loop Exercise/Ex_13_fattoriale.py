"""
Trova il fattoriale di un numero
"""
def fattoriale(n:int)->int:
    # caso base
    if n==0 or n<1:
        raise ValueError('Il numero deve essere maggiore di 0')
    elif n== 1:
        return 1
    # Passo ricorsivo:
    # moltiplica n per il risultato del fattoriale di (n-1).
    # La ricorsione continua finché n non diventa 1.
    else:
        return n* fattoriale(n-1)

print(fattoriale(5))

def main():
    fattoriale(5)

if __name__ == "__main__":
    main()