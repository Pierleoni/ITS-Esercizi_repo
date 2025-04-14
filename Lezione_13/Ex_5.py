from fractions import Fraction
def armonic(n:int)->int:
    if n == 0 :
        raise ValueError("Errore: il numero deve essere maggiore di 0")
    elif n<1:
        raise ValueError("Errore: il numero non deve essere negativo")
    elif n==1:
        return 1
    else:
        return round(1/n* armonic(n-1),6)

print(armonic(7))