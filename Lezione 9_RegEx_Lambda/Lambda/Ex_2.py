from typing import Callable
somma: Callable[[int,int],int] = lambda a,b: a+b
print(somma(2,3))