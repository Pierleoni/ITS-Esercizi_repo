"""
Stampa i primi 10 numeri naturali usando il while loop
"""

def natural_numbers(n:int= 10): 
    cont = 1
    while cont<=n: 
        print(cont)
        cont+=1


def main():
    natural_numbers()

if __name__ == "__main__":
    main()