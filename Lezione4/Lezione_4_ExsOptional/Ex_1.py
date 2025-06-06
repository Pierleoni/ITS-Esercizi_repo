def grade(name: str, marks: list[int]):
    media = sum(marks)/len(marks)
    if media >=60:
        return f"{name} ha superato l'esame con la media di {media}"
    else: 
        return f"{name} non ha superato l'esame"



print(grade("Luca", [70,80,90, 100]))

studs:list[tuple] = [("Luca",[70,80,90, 100]),
("Maria", [40,50,55])
]
for nome, voti in studs:
    print(grade(nome, voti))


