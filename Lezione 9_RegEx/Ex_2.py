import re
def extract_email(text:str):
    # text = "Contattaci a info@azienda.com oppure support@help.org"
    return re.findall(r'[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}', text)

print(extract_email(text = "Contattaci a info@azienda.com oppure support@help.org"))