"""
Dato un numero dall'utente, stampa il numero con 5 zeri prima di esso.
Esempio:
n = 12
Output = 00012
"""

def padding_zeros(n:int)->str:
    num_conv:str = str(n)
    pad:str = num_conv.zfill(5)
    print(pad)

number:int = int(input('Digita il numero: '))

def main():
    padding_zeros(number)

if __name__ == "__main__":
    main()