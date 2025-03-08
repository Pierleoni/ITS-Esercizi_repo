day:int = int(input("Inserire il giorno:")) 
month:int = int(input("Inserire il mese:"))

tuple_date:tuple[int] = (day, month)
#Creo la lista dove inserisico i giorni totali di ogni mese 
giorni_per_mese:list[int] = [31, 29, 31, 30,31,30, 31, 31, 30,31,30,31]

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
    #Questo case mi è utile per controllare se la data inserita sia valida. Questa cosa si chiama Short circuit evaluation
    
    #creo il case per valutere i valori del giorno e del mese e se il valore del mese è maggiore di 12 o se day è maggiore della lista giorni_per mese, meno i valori di month -1 allora mi printa il messaggio
    
    case (day,month) if month>12 or day >giorni_per_mese[month-1]:
        print(f"Il {day}/{month}  non esiste")
    case _:
        print("Nessuna festività importante in questa data.")

