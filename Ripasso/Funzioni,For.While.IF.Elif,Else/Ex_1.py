from typing import Any
def comb(x:Any,y:Any,z:Any)-> bool:
    if x == True and (y or z):
        return "Azione Permessa"
    else:
        return "Azione negata"

print(comb(True, False,True))