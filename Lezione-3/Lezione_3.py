n = int(input("Inserire un numero:"))

if n == 1:
    print(f"{n}st!")
elif n == 2:
    print(f"{n}nd!")
elif n == 3:
    print(f"{n}rd!")
elif n == 4:
    print(f"{n}th!")
else : 
    print(f"{n}th!")


g = "f"
age = 15

match (g, age):
    case ("f", 5):
        print("Piccola!")
    case ("m", 5):
        print("Piccolo!")
    case ("f", 10):
        print("Grande!")
    case ("m", 10):
        print("Gigante!")
    case _:
        print("Kinder Sorpresa!")