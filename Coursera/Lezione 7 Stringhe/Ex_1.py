

stringa:str = 'X-DSPAM-Confidence: 0.8475'
# Cerco la prima posizione di ':'
extract_1:int = stringa.find(':')
# Cerco la prima posizione del ultima virgoletta a fine stringa a partire da extraxct_1

ext_2:int = stringa.find(' \' ', extract_1)

# Estra la sottostringa compresa tra lap osizione subito dopo di ':' e la posizione dell'ultima virgoletta della stringa originaria
num_str:str = stringa[extract_1+1:ext_2]

# Converte la stringa estratta in un float
num= float(num_str)
print(num)