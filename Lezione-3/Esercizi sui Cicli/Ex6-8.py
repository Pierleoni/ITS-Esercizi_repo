pet_dict1:dict[str] = {"animal_type": "cat", "name": "Fuffy"}
pet_dict2:dict[str] = {"animal_type": "dog", "name": "Shiva"}
pet_dict3: dict[str] = {"animal_type": "Iguana", "name": "Ettore"}
pet_list:list[dict] = [pet_dict1,pet_dict2,pet_dict3]
for pet in pet_list:
    print(pet)