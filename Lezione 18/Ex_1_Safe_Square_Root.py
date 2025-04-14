import math
def safe_sqrt(number:int)->int:
    if number <0:
        try:
            math.sqrt(number)
        except ValueError as error:
            print(error)
    else:
        print(math.sqrt(number))

safe_sqrt(5)
safe_sqrt(-1)