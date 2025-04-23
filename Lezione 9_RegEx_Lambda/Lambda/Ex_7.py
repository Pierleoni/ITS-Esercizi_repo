import re
from typing import Callable
parole:list[str] = ["cane", "gatto", "elefante", "ratto", "orso"] 

words:Callable[[list[str]], str] = list(filter(lambda x: re.fullmatch(r'\w{5,8}',x), parole))
print(words)