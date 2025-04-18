import re
def check_product_code(code:str)->bool:
    if re.fullmatch(r'PROD-\d{4}-[A-Z]{2}', code):
        return True
    else:
        return False

print(check_product_code("PROD-9876-ZX"))
print(check_product_code("PROD-98-ZX"))
print(check_product_code("ACED-9845-AC"))
print(check_product_code("PROD-9845-ZX"))
