"""
Stampa i numeri da -10 a -1 usando un loop
"""

def negative_counter(neg_number:int= -10)->None:
    for n in range(neg_number,0):
        print(n)

def main():
    negative_counter()

if __name__ == "__main__":
    main()
