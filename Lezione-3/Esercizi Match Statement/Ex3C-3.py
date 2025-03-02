oggetti = []
for n in range(3):
    oggetti.append(input("Inserire elemento:"))
    


match oggetti:
    case oggetti if "penna" and "matita" and "quaderno" in oggetti:
        print(oggetti)
        print("\nMateriale didattico")
    case oggetti if "pane" and "latte" and "uova" in oggetti:
        print(oggetti)
        print("\nProdotti alimentari")
    case oggetti if "sedia" and "tavolo" and "armadio" in oggetti:
        print(oggetti)
        print("\nMobili")
    case _:
        print(oggetti)
        print("\nCategoria sconosciuta")
        