from typing import Any
list = []
def printListBackward(list, val:int =-1)-> list[Any]:
    if len(list) + val ==0:
        print("Done")
    else:
        return printListBackward(list + val)
    


print(printListBackward([]))