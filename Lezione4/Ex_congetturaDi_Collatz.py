
# import matplotlib.pyplot as plt 

def Col(n: int)-> int: 
    cont = 0
    while n !=1:
        if n %2!=0:
            n= n*3+1
        else:
            n= n/2
        cont+=1
    return n

print(Col(100))

