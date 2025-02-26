voto_di_laurea:int= int(input("Inserire il voto:"))
match voto_di_laurea:
    case voto_di_laurea if 106<=voto_di_laurea<=110:
        print("4.0")
    case voto_di_laurea if 101<voto_di_laurea<105:
        print("3.7")
    case voto_di_laurea if 96<voto_di_laurea<100:
        print("3.3")
    case voto_di_laurea if 91<voto_di_laurea<95:
        print("3.0")
    case voto_di_laurea if 86<voto_di_laurea<90:
        print("2.7")
    case voto_di_laurea if 81<voto_di_laurea<85:
        print("2.3")
    case voto_di_laurea if 76<voto_di_laurea<80:
        print("2.0")
    case voto_di_laurea if 70<voto_di_laurea<75:
        print("1.7")
    case voto_di_laurea if 66<voto_di_laurea<69:
        print("1.0")
    case _:
        print("Voto non valido")
    