def molt(list:list[int], thrash = 5 ):
    prodotto_cumulato:int = 1
    for nums in list:
        if nums >= thrash:
            prodotto_cumulato *= nums
    return prodotto_cumulato

print(molt([5,6,7,8]))


def fattoriale(n:int):
    if n == 1:
        return 1
    else:
        return n*fattoriale(n-1)

print(fattoriale(7))
print(fattoriale(5))
print(fattoriale(3))