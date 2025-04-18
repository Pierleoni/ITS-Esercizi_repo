import re
def is_valid_cap(cap:str) -> bool:
    if re.fullmatch(r'\d+', cap):
        return True
    else:
        return False

print(is_valid_cap("70124"))
print(is_valid_cap("A0123"))
