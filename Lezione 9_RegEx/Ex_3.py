import re
def mask_number(text:str) -> str:
    return re.sub(r'\d', "#", text)

print(mask_number(text="Il codice è 12345 e la data è 2025."))