def outer_fun(a:int, b:int) ->int:
    def addition(a,b):
        return a + b
    add = addition(a,b)
    return add + 5

res = outer_fun(5,10)
print(res)



