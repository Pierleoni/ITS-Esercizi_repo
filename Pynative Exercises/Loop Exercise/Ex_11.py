"""
Stampa tutti i numeri primi nel range tra 25 e 50
"""
import math
def prime_number(start:int, end:int)->None:
    for num in range(start, end + 1):
        if num > 1:
            # assumiamo che sia primo
            for i in range(2, num):
                if num % i == 0:
                    # non è primo, usciamo dal ciclo
                    break
            else:
                # se il ciclo non ha trovato divisori → è primo
                print(num)

def main():
    prime_number(25, 50)

if __name__ == "__main__":
    main()