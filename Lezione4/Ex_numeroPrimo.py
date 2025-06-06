def num_primo(n:int)-> bool:
    
    if n <=1:
        return False
    cont = 2
    while cont*cont <n:
        if n %cont== 0:
            return False
    cont+=1
    return True

print(num_primo(2))


# print(num_primo(6))
print(num_primo(7))

