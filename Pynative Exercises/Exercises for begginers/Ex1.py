def multi_or_sum(number:int, number_2:int) ->int:
    prod = number*number_2
    if prod<=1000:
        return prod
    else:
        sum = number+number_2
        return sum
    

res_1:int = multi_or_sum(40,30)
print(res_1)

res_2:int = multi_or_sum(600,700)

print(res_2)