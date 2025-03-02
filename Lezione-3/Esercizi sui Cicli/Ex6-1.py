person_dict:dict[str, int] = {
    "first_name": "Tizio", 
    "last_name": "Caio", 
    "age": 26, 
    "city": "Paperopoli"
}

# for key,values in person_dict.items():
#     print(f"Chiave:{key}", f"\nValore:{values}")

for er_popa in person_dict:
    print("Chiave:", er_popa)
    print("valore", person_dict[er_popa])


