numbers_list:list[int] = [10,30,40,50,10]
numbers_list_2:list[int] = [10,30,40,50,10]
print("Given List:", numbers_list)

if numbers_list[0] == numbers_list_2[-1]:
    print(True)
else:
    print(False)