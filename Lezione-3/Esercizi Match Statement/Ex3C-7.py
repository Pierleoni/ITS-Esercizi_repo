
cont:int = 1
testa:int = 0
croce:int = 0
while cont<=8:
    lancio:str = (input("Inserire testa o croce:"))
    match lancio:
        case "t":
            testa += 1 
        case "c":
            croce +=1
        case _:
            print("Lancio non valido")
    cont+=1


testa_perc = (testa/8)*100
croce_perc = 100 - testa_perc

print(f"Totale testa: {testa}. \nPercentuale testa: {testa_perc}")
print(f"Totale testa: {croce}. \nPercentuale croce: {croce_perc}")

