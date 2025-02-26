list_three:list[int] = []
for number in range (3, 31, 3):
    list_three.append(number)
    if number % 3 == 0:
        print(number)



