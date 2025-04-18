import re
def is_integer(s:str) -> bool:
    if re.fullmatch(r'^-?\d+$', s):
        return True
    else:
        return False

s_1:bool = print(is_integer("12.3"))
s_2:bool = print(is_integer("123"))
s_3:bool = print(is_integer("-456"))
