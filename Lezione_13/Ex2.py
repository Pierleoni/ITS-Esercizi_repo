def compoundInterest(m:float,t:int)->float:
    if m < 0.00:
        return 0.00
    elif m == 0.00:
        return 0.00
    else:
        if t<=0:
            # approsimo m a 2 cifre decimali
            return round(m,2)
        else:
            return round(1.005* compoundInterest(m,t-1),2)


a_1:int = print(1.005*compoundInterest(1000,24))