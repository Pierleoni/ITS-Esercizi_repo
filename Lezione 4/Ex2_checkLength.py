def check_length(word:str)->str:
    if len(word)>10:
        print(f"{word} è maggiore di 10 caratteri")
    elif len(word)<10:
        print(f"{word} è minore di 10 caratteri")
    else:
        print(f"{word} è uguale a 10 caratteri")

result = check_length("Salvini infame")
