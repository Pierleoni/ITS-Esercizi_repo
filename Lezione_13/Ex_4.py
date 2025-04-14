def recursiveDigitCounter(n:int)->int:
    if abs(n)>10:
        return 1
    if abs(n)<10:
        return 1+ recursiveDigitCounter(n//10)

print(recursiveDigitCounter(-20))