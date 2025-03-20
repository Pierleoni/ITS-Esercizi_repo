from typing import Any
# # 1.Create a list of names and print the second item.
# name_list:list[str] = ["Bob", "Sarah", "Emily", "Deacon", "John"]
# print(name_list[2])

# # 2.Create a list of sports and then replace the second item with another sport.
# sport_list:list[str] = ["Football", "Rugby", "Beachvolley", "Racing", "Swim"]
# sport_list[2]= "Volleyball"
# print(sport_list)

# # 3.Create a list containing numbers and delete the fifth number from the array. 

# list_num:list[int,float] = [5,6,7,8,9.20,10,25 ]
# del list_num[5]
# print(list_num)



# # 4.Create two lists of numbers and merge them. 
# list_num_1:list[int] = [1,22,33,45,6,7,8]
# list_num_2:list[int] = [2,79,90,10,56,23]

# merge_list:list[int] = list_num_1 + list_num_2

# print(merge_list)


# # 5. Create a list of numbers and find the length, minimum, and maximum. 

# list_n:list[int] = [1,2,3,45,6,78,9,10,12,15,23]
# print("Length of the list:", len(list_n))
# print(f"The max number in the list: {max(list_n)}")
# print(f"The min number in the list: {min(list_n)}")


# # 6. Create a dictionary of students and scores and print out a student’s score.
# studs_score:dict[int] = {"Emma": 26, "Tyron": 23, "Jason": 25, "Kelly": 20}
# print(f"The Score of Emma is: {studs_score['Emma']}.\nThe score of Tyron is: {studs_score['Tyron']}.\nThe score of Jason is: {studs_score['Jason']}.\nThe score of Kelly is: {studs_score['Kelly']}")


# # 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair. 
# person_dict:dict[int] = {"Aldo": 26, "Giovanni": 33, "Giacomo": 46, "Fabio": 12, "Giangiangi": 4}
# del person_dict["Giacomo"]
# print(person_dict)


# # 8. Create a dictionary of names and ages and then print out all the keys and values
# names_ages:dict[int] = {"Gianluca": 24, "Erica": 23, "Jacob": 45}
# print(names_ages)

# # 9. Create a tuple of your favorite movies

# films_favourite:tuple[str] = ("Good Fellas", "Gangs of New York", "Inglorious Bastards", "Pulp Fiction", "Ted")


# # 10. Create a tuple and print all the items from the first to third index.

# tup_items:tuple[Any] = ("Hi", 20, 40, True, False, "Hurry up", 3,4,5,6,7,8,9)
# print(tup_items[0:2])


# def calculate_factorial(number) ->int:
#     fact =1
#     for elem in range(1, number+1):
#         fact*=elem
#     return fact

# print(calculate_factorial(5))

def check_access(username: str, password:str, is_active: bool) -> str:
    password_string = str(password)
    username.lower()
    if username == "admin" and password_string == "12345" and is_active == True:
        return "Accesso consentito"
        
    return "Accesso negato"

print(check_access("admin", "12345", True))
print(check_access("admin", "12345", False))
print(check_access("user", "12345", True))
print(check_access("admin", "54321", True))
print(check_access("admin", "54321", False))



# def remove_duplicates(*list_item:Any) -> list:
#     list_item = []
#     for elem in list_item:
#         list_item.append(elem)
#         list_item = list(set(list_item))
#     return list_item




# def remove_duplicates(list_item:list[Any]) -> list:
#     may_tup:tuple = set()
#     list_items:list = []
#     for elem in list_item:
#         if elem not in may_tup:
#             may_tup.add(elem)
#             list_items.append(elem)
        
        
#     return list_items

# print(remove_duplicates([1,2,2,3,3]))

def countdown(n:int) -> int:
    cont = 0
    for elem in range (n,-1,-1):
        
        
        print(elem)

print(countdown(5))


def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return len(numbers) / (sum(numbers) -1)
        
    else:
        return sum(numbers) / len(numbers)
        

average = calculate_average([1,2,3,4])
print(average)

# n = 123
# s = str(n)
# print(type(s))