number_tutor:int = 10
attesa = 0

while number_tutor == 0 and attesa < 50:
    studente:str= str(input("Inserire nome studente:"))
    if number_tutor > 0:
        number_tutor -= 1
        print(f"Tutor assegnato con successo a {studente}. Tutor rimanenti: {number_tutor}")
    else:
        attesa+=1
        print("Studente in attesa")
    if number_tutor==0 and attesa>50:
        print("Limite raggiunto: tutor terminati e lista d'attesa piena.")
        break