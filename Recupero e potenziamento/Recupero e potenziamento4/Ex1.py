import math
def calculateCharges(ore:int|float)-> float:
    tariffa = 0 
    if ore <=3:
        tariffa =2
        return tariffa
    elif ore<24:
        ore = math.ceil(ore)
        return 2.00 + (ore -3)*0.50
    else:
        tariffa = 10
        return tariffa

print(calculateCharges(5))