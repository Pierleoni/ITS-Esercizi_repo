from typing import Any
# Variabile per trovare il valore numerico più grnade nella lista di interi
largest_num:Any = None

# Variabile per trovare il valore numerico più piccolo nella lista di interi 
smallest_num: Any = None

tot:int = 0

lista:list[int] = [6,7,8,9,10,2,3]

for nums in lista: 
    tot+=nums
    
    if largest_num is None and smallest_num is None:
        largest_num = nums
        smallest_num = nums 
    elif nums > largest_num: 
        largest_num = nums 
    elif nums<smallest_num:
        smallest_num = nums
    
    # print(f"Numero più grande:{largest_num, nums}")
    # print(f"Numero più piccolo{smallest_num, nums}")
    

print(f"Totale della somma degli elementi:{tot}\nNumero più grande:{largest_num}\nNumero più piccolo: {smallest_num}")

