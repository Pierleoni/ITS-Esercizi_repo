def recursiveFactorial(n:int)->int:
    if n <0 or n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*recursiveFactorial(n-1)

print(recursiveFactorial(5))
print(recursiveFactorial(6))
print(recursiveFactorial(4))

