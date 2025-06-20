import re
def is_valid_ipv4(address: str)-> bool:
    # Divide il contenuto di address in una lista dove ogni otteto è un elemento
    chars = address.split(".")
    # Controllo per verificare che ogni elmento della lista sia un otteto dell'indirizzo IP
    if len(chars) !=4:
        return False
    
    for char in chars:
        if not char.isdigit():
            return False
        char_num = int(char)
        if char_num <0 or char_num> 255:
            return False
        
    return True
    # if re.fullmatch(pattern, address):
    #     return True
    # else:
    #     return False



print(is_valid_ipv4("255.255.255.255"))
print(is_valid_ipv4("192.168.0.1"))
print(is_valid_ipv4("256.100.10.1"))
print(is_valid_ipv4("192.168.1"))
print(is_valid_ipv4("192.168.1.a"))