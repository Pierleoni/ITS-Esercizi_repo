# somma:int = 0
# for number in range (1,11):
#     somma += number
#     print(somma)
    

# sum:int= 0
# for numbers in range (20, 38):
#     sum = sum + numbers
#     print(sum)


# summa:int = 0
# for i in range (35, 50):
#     summa+=i 
#     print(summa)
    


def sum_subtract (a:int, b:int):
        somma = a + b
        sottrazione = a-b 
    
        return somma, sottrazione
if __name__ == "__main__":
    

    somma, sottrazione= sum_subtract(10,5)
    print(f"Somma: {somma}, Sottrazione: {sottrazione}")






