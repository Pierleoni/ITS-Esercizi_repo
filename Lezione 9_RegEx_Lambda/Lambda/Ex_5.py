from typing import Callable
even_odd:Callable[[int], str] = lambda a: "Pari" if a%2==0 else "Dispari" 
print(even_odd(4))
print(even_odd(3))