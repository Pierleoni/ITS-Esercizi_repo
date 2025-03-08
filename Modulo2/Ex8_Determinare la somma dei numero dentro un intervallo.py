num_a:int= int(input("Inserire il numero:"))
num_b:int = int(input("Inserire il numero:"))
if num_a >= num_b:
    print(f"Errore: {num_a} deve essere minore di {num_b}")
elif num_a <= 0 or num_b <= 0:
    print("Errore: I numeri devono essere positivi")
else:
    
    somma = 0
    i = num_a 

    # Ciclo while per sommare tutti i numeri da A a B (inclusi)
    while i <= num_b:
        somma += i  # Aggiunge il valore corrente di i alla somma
        i += 1  # Incrementa i per passare al numero successivo

    # Stampa il risultato
    print(f"La somma dei numeri tra {num_a} e {num_b} è: {somma}")




