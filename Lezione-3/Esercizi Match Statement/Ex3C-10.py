day:int = int(input("Inserire il giorno:")) 
month:int = int(input("Inserire il mese:"))

tuple_date:tuple[int] = (day, month)

match tuple_date:
    case (1,1):
        print(f"Il {day}/{month} è Capodanno")
    case (14,2):
        print(f"Il {day}/{month} è San Valentino")
    case (2, 7):
        print(f"Il {day}/{month} è la Festa della Repubblica Italiana")
    case (15, 8):
        print(f"Il {day}/{month} è Ferragosto")
    case (31, 10):
        print(f"Il {day}/{month} è Halloween")
    case (25, 12):
        print(f"Il {day}/{month} è Natale")
    case _:
        print("Nessuna festività importante in questa data.")

