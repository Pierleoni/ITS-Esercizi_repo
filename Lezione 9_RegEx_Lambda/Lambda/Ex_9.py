def moltplicatore(n:int) ->int:
    return lambda a: a*n

per_due = moltplicatore(2)
print(per_due(10))  # Output: 20

