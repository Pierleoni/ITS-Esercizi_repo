punteggio:int = 0
while punteggio <100:
    d1:int = int(input("Lanciare il primo dado:"))
    d2:int = int(input("Lanciare il secondo dado:"))
    if d1 >0 and d1 <= 6 and d2>0 and d2<=6:
        somma = d1+d2
    else:
        print("errore!")
    
    if d1 %2 == 0 and d2 %2 ==0 and somma>8:
        punteggio = 100
    elif d1 == 6 or d2==6 or somma==7:
        punteggio += 10
    else:
        punteggio = 0
        print("Sconfitta")
        break

if punteggio == 100:
    print("Vittoria!") 