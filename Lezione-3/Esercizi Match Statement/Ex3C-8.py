word:str = str(input("Inserire una frase:"))

match word:
    case word if word[-1]=="?" and len(word)%2==0:
        print("Si")
    case word if word[-1]=="?" and len(word)%2!=0:
        print("No")
    case word if word[-1] =="!":
        print("Wow!")
    case _: 
        print(f"Tu dici \"{word}\" ")


