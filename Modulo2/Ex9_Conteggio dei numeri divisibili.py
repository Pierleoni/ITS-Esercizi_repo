number:int = int(input("Inserire la soglia:"))
if number<=0:
    print("Il numero deve essere positivo")
elif number%1==0:
    cont = 0
    i = 0
else:
    print("Il numero deve essere positivo")

while i != 10:
    number_2:int = int(input("Inserire numero:"))
    if number_2%number == 0:
        cont +=1
    i +=1
print(cont)
