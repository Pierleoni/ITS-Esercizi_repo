nome:str = input("inserire il nome:")
gender = input("Inserire il gender (m per Maschio ed f per Femmina): ")
match gender:
    case "m":
        print( f"Nome: {nome}\n Gender:Maschio" )

    case "f":
        print(f"Nome: {nome}\n Gender: Femmina" )
    case _:
        print(f"Mi dispiace {nome}, non e' possibile procedere con la generazione di un documento di identità!")

