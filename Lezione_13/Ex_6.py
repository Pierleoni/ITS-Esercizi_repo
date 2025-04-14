def produttoria(num:int, n:int)->int:
    # La variabile num è il numero che parte da 0 e arriva fino al valore della variabile n
    if num>n:
        return 1
    else:
        return (num + 2) * produttoria(num+1,n)

print(produttoria(0,7))
print("------------------")
print(produttoria(0,9))
print("-----------------")
print(produttoria(0,10))