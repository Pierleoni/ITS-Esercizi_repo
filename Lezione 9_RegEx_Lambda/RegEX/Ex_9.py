import re
def find_fc(text:str) ->list[str]:
    return re.findall(r'[A-Z0-9]{16}', text)


testo:str = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
codici:list[str] = find_fc(testo)

print(codici)