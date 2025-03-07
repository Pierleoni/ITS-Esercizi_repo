def check_each(*args)->int:
    for number in args:
        if number>5:
            print(f"{number}:Bigger")
        elif number<5:
            print(f"{number}:Smaller")
        else:
            print(f"{number}:Equal")

check_each(5,4,7)