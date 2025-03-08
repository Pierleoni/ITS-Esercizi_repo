cont = 0
sum = 0
scelta:str = (input("Inserire l'opzione:"))
while scelta != "NO":
    
    if scelta == "si":
        voto:int = int(input("Inserire il voto:"))
        if voto>0:
            cont+=1
            sum= sum +voto
        else:
            print("Errore:inserire numero positivo")
        scelta:str = (input("Inserire l'opzione:"))
    elif scelta=="no":
        break
media = sum/cont
print(media)

    
