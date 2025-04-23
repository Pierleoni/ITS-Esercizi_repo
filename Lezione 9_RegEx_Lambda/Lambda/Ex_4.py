from typing import Callable

studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]
order_stud: Callable[[tuple[list]], list] = sorted(studenti, key=lambda index:index[1] )
print(order_stud)