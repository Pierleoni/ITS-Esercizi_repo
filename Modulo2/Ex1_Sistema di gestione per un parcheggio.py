posti_max:int = int(input("Inserire il numero di posti massimi:"))
posti_liberi = posti_max
opzione = None

while opzione !='esci':
    opzione = str(input("Inserire l'azione che vuole effettuare:"))
    if opzione == 'ingresso':
        if posti_liberi >0:
            posti_liberi-=1
        else:
            print("Il parcheggio è pieno")
    elif opzione == 'uscita':
        if posti_liberi<posti_max:
            posti_liberi+=1
        else:
            print("Il parcheggio è già vuoto")
    elif opzione == 'stato':
        print(posti_liberi)
        print(posti_max-posti_liberi)
    elif opzione == 'esci':
        break
    print("Errore, selezionare una scelta tra \'ingresso\', \'uscita\', \'stato\', \'esci\'")