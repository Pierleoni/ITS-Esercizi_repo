"""
Prendi due numeri dati dall'utente in input e calcola il loro prodotto
"""

def two_int(): 
    n1:int = int(input("Enter the first number: "))
    n2:int = int(input("Enter the second number: "))
    return n1*n2

def main():
    print(two_int())

if __name__ == "__main__":
    main()