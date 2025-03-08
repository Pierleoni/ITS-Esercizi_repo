age:int = int(input("Inserire l'età:"))
if age >= 18 and age <=65:
    print("Puoi partecipare all'attività")
elif age<18:
    print("Non poui partecipare all'attvità perché non hai raggiunto l'età minima richiesta")
else:
    print("Non puoi partecipare all'attività perché hai superato l'età massima consentita")