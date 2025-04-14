def pi_3(num:int, n:int) ->int: 
    if num>n:
        return 1
    else:
        return (num**3) * pi_3(num+1,n)

print(pi_3(1,5))