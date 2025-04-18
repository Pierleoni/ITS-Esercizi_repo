import re
def find_codes(text:str)->list[str]:
    return re.findall(r'[A-Z0-9]{8}', text)

print(find_codes("I codici sono AB12CD34 e 12345678 e XYZZYZZZ"))