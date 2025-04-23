from functools import reduce
from typing import Callable
numeri = [2, 3, 4]
prodotto:Callable[[int,int],int] = reduce(lambda a,b:a*b, numeri)
print("Lista originale:", numeri)
print("-------------------------")
print(f"Prodotto degli elementi della lista: {prodotto}")
