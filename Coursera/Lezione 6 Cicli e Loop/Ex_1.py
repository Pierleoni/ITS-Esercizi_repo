# variabile contatore
cont: int = 0

# variabile totale 
tot:int = 0 

# variabile media 
avg = None

while True:
    # dichiaro una viariabile per permettere all'utente di inseirre numeri
    line:int = input("Enter a number:")
    # Se line è uguale a 'done
    if line.lower() == 'done':
        # stampa il totale, il numero di iterazioni (cont) e la media numerica
        print(tot, cont, avg)
        # Dopodiché interrompe il ciclo 
        break 
    
    # Per evitare che l'utente inserisca altri valori che non siano numeri o che non corrisponda alla stringa 'done'
    # Gestisco tramite blocco try-excpet 
    try: 
        num = int(line) #Converte solo se non è done 
    # Se il valore non è done prendo l'eccezzione come ValueError
    except ValueError:
        # Stampo in output 'Bad Data'
        print('Bad Data')
        continue #Passo alla prossima iterazione
    
    # Sommo i valori tra tot e num 
    tot +=num 
    # Aggiorno il contatore
    cont +=1 
    # Calcolo la media numerica dividendo i valori finali di tot e cont
    avg = tot/cont 
    
    
            
        
        
    