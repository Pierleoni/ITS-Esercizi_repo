# numbers = (range(1, 1000001))
# start = min(numbers)
# end = max(numbers)
# print(start, end)
# sum = sum(numbers) 
# print(sum)

numbers:list[int] = []
for i in range(1, 1000001):
    numbers.append(i)
    
# print(i) 

print(min(numbers)) 
print(max(numbers))
print(sum(numbers))
