import random
def nums_random()-> int:
    minimo = int(input("Inserisci il numero minimo dell'intervallo: "))
    massimo = int(input("Inserisci il numero massimo dell'intervallo: "))
    genera = random.randint(minimo, massimo)
    num_tent = int(input(f"inserire numero massimo di tentativi: "))
    i = 0
    while i <num_tent:
        tentativo = int(input("indovina il numero:"))
        if tentativo == genera:
            
            print ("Hai indovinato!")
            break
        elif tentativo<genera:
            
            print ("Troppo basso")  
            
        else:
            
            print ("Troppo alto")        
        i +=1
        if i == num_tent:
            print ("Sconfitta! Non hai indovinato il numero")
    return genera

nums_random()


