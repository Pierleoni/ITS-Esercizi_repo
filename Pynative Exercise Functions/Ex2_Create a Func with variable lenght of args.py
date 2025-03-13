from typing import Any

def func1(*values:int) ->Any:
    for num in values:
        print(num)


func1(6,7,8,9)
func1(12,456)

