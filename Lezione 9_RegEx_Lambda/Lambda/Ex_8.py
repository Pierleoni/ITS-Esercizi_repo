
studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

ordered_stud:list[dict[str,int]] = sorted(studenti, key=lambda index:index[1] ) 

print(ordered_stud)