import re
def is_valid_name(name:str)->str:
    if re.fullmatch(r'[A-Z][a-z]{2,}', name):
        return True
    else:
        return False

print(is_valid_name("Marco"))
print(is_valid_name("marco"))
print(is_valid_name("Ma"))
