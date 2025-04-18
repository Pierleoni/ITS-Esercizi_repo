import re
def find_dates(text:str) -> list[str]:
    return re.findall(r'\d+/?\d+/?\d+', text)

print(find_dates(text="Le date importanti sono 09/04/2025 e 15/08/2023."))