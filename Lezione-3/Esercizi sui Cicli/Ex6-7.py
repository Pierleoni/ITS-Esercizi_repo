people:list[dict, str,int]= [ 
{"first_name": "Tizio", "last_name": "Caio", "age" : 26, "city": "Paperopoli"},
{"first_name": "Caligola", "last_name": "Sempronio", "age": 33, "city": "Topolinia"},
{"first_name": "Giulio", "last_name": "Cesare Augusto", "age": 13, "city": "Sin City"}
] 

for key_elm in people:
    print(f"Nome:{key_elm['first_name']}, Cognome: {key_elm['last_name']}, Age: {key_elm['age']}, City: {key_elm["city"]}")