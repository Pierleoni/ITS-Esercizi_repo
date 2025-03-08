number:int = int(input("Inserire il numero:"))
if number%1==0 and number>0:
    sum = 0
    i = 1
    while i<=number:
        sum=sum+i**2
        i+=1
    print(sum)
else:
    print(f"Errore, {number} non è positivo")