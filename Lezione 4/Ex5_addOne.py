def add_one(num_1:int)->int:
    num_1+=1 
    return num_1

print(add_one(1))


def add_one_list(my_list:list)->list[int]:
    new_list:list=[]
    for numbers in my_list:
        new_list.append(add_one(numbers))
    print(new_list)

popa = add_one_list([1,2,3]) 




