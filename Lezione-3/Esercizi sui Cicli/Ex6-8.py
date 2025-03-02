pet_dict1:dict[str] = {"animal_type": "cat", "name": "Fuffy"}
pet_dict2:dict[str] = {"animal_type": "dog", "name": "Shiva"}
pet_dict3: dict[str] = {"animal_type": "Iguana", "name": "Ettore"}

for pet in pet_dict1,pet_dict2,pet_dict3:
    print(f"Tipo di animale:{pet["animal_type"]}, Nome: {pet["name"]}")