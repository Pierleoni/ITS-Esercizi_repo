animal_list:list[str] = ["Cougar", "Lion", "Tiger", "Leopard"]

animal_list.insert(0, "Jaguar")
animal_list.insert(2, "Elephant")
animal_list.append("Koala")
additional_animal_list:list[str] = ["Emu", "Capybara","Axolotl", "Duck-bill", "Sheep", "Deer", "Wolf", "Bear", "Horse", "Wolverine", "Raccon",  "Mule","Cow","Cat","Dog"]
animal_list.extend(additional_animal_list)
# print(animal_list)
animal_list.pop(0)
animal_list.pop(6)
animal_list.remove("Tiger")
# print(animal_list)
animal_list.sort()
print(animal_list)

# for animal in animal_list:
#     if animal=="Axolotl" in animal_list:
#         print(f"{animal} is a Wonder of nature")
#     elif animal == "Bear" in animal_list:
#         print(f"{animal}, rather not")
#     else:
#         print(f"{animal} is animal")


for animal in range(len(animal_list)):
    print(animal)
    
more_animal: list = ["Tiger", "Jaguar", "Emu", "Jaguar"]
animal_list.extend(more_animal)
print(animal_list)
type_animal_dict:dict[list,str] = {"Predators":f"{animal_list[1]}", "Herbiveros": f"{animal_list[4]}", "Those who defeated a nation": f"{animal_list[21]}", "Pet": {animal_list[3]}}

