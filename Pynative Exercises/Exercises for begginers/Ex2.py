previous_num:int = 0
for i in range(1, 11):
    
    somma = previous_num+i
    previous_num = i

print(f"Current number: {i}, Previous number: {previous_num}, Somma: {somma}")