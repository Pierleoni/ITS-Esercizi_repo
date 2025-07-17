prompt:float = float(input("Inserire uno score:"))

if  prompt >=0.9:
    print("A")
elif prompt >= 0.8:
    print("B")
elif prompt >=0.7:
    print("C")
elif prompt >= 0.6:
    print("D")
else:
    print("F")
