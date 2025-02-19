list_person:list=["Bruce Dickinson", "Lemmy Kilmister", "Filthy Animal Taylor", "Wendy O' Williams"]
list_person[3]="Jo Bench"
list_person.insert(0, "Riley Gale")
list_person.insert(2, "Doro Pesch")
list_person.append("Cronos")
print(f"Unfortunately {list_person[0]} the table won't arrive in time for the dinner ")
print(f"Unfortunately {list_person[1]} the table won't arrive in time for the dinner")
print(f"Unfortunately {list_person[2]} the table won't arrive in time for the dinner")
print(f"Unfortunately {list_person[3]} the table won't arrive in time for the dinner")
print(f"Unfortunately {list_person[4]} the table won't arrive in time for the dinner")
print(f"Unfortunately {list_person[5]} the table won't arrive in time for the dinner")
print(f"Unfortunately {list_person[6]} the table won't arrive in time for the dinner")
print(f"Unfortunately {list_person.pop(6)} are not more invited")
print(f"Unfortunately {list_person.pop(2)} are not more invited")
print(f"Unfortunately {list_person.pop(0)} are not more invited")
print(f"Unfortunately {list_person.pop(3)} are not more invited")
print(f"Unfortunately {list_person.pop(2)} are not more invited")
# print(list_person) 
# print(f"I'd like to informed Mr.{list_person[0]} that you are still on the list of the guests for the dinner")
# print(f"I'd like to informed Mr.{list_person[1]} that you are still on the list of the guests for the dinner")
# del list_person[1]
# del list_person[0]
# print(list_person)


# if len(list_person) ==7:
#     print(f"Unfortunately {list_person[0]} the table won't arrive in time for the dinner ")
#     print(f"Unfortunately {list_person[1]} the table won't arrive in time for the dinner")
#     print(f"Unfortunately {list_person[2]} the table won't arrive in time for the dinner")
#     print(f"Unfortunately {list_person[3]} the table won't arrive in time for the dinner")
#     print(f"Unfortunately {list_person[4]} the table won't arrive in time for the dinner")
#     print(f"Unfortunately {list_person[5]} the table won't arrive in time for the dinner")
#     print(f"Unfortunately {list_person[6]} the table won't arrive in time for the dinner")
# elif len(list_person) ==2:
#     print(f"I'd like to informed Mr.{list_person[0]} that you are still on the list of the guests for the dinner")
#     print(f"I'd like to informed {list_person[1]} that you are still on the list of the guests for the dinner")
    


# if len(list_person) == 2:
#     for person in list_person:
#         print(f"I'd like to inform {person} that you are still on the list of the guests for the dinner.")


cont = 0
len= len(list_person)
while cont<len:
    print(f"I'd like to informed Mr.{list_person[cont]} that you are still on the list of the guests for the dinner")
    
    cont+=1