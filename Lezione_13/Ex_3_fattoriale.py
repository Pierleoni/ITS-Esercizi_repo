def fattoriale(n:int)->int:
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*fattoriale(n-1)
    

num_1:int = print(fattoriale(5))
print("----------------------")
num_2:int = print(fattoriale(7))