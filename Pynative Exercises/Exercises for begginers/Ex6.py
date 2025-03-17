number_list:list[int] = [10, 20,33, 45, 79, 80, 66, 50]

for num in number_list:
    if num%5==0:
        print(num)
    else:
        print(f"{num} non è divisibile per 5")