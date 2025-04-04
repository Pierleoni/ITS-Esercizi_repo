def recursivePower(a:int, b:int) ->int:
    if a == 0:
        return 0
    elif a==1:
        return 1
    elif b ==0:
        return 1
    else:
        return pow(a,b)

p_1:int = print(recursivePower(3,4))

print("--------")

p_2:int = print(recursivePower(0,4))
print("--------")

p_3:int = print(recursivePower(3,0))