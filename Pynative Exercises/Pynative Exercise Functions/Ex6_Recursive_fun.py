def recursive_fun(num:int) ->int:
    if num>0:
        return num + recursive_fun(num - 1)
    else:
        return 0
    

res =recursive_fun(10)
print(res)

res_1 = recursive_fun(11)
print(res_1)


