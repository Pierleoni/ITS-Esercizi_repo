from typing import Any
num_1:int = 15
num_2:int = 30 

somma: int = num_1 + num_2 


division_calc:int = somma/2

print(f"Somma: {somma} \nDivisione della somma: {division_calc}")

string_var_1:str = "Hello"
string_var_2:str = "World"

num_3:int = 20
num_4:int = 10

print(
    "Concatenazione delle stringhe:",{string_var_1 + " "+ string_var_2}, 
    f"\nSottrazione:{num_3- num_4} \nMoltiplicazione:{num_1*num_3} \nDivisione: {num_2/num_1} \nResto:{num_2%num_3}"
)

name:str = "Aldo"

food_1, food_2, food_3 = "Pizza", "Pasta", "Zucchine"

print(name, food_1,food_2, food_3)

msg:Any = "Hello" *10
print(msg)

string_1:str = "Hi"
string_2:str = "There!"
conc_string:str = string_1 + ", " + string_2
print(conc_string)

print(conc_string[0:5])

string_3:str = f"Hi my name is {name} Moro, and now I'm laying in a red Reanult 4"
print(string_3[0:])

