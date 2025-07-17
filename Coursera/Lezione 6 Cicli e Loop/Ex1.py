# Contatore 
cont = 0

# Accumulatore
tot = 0

while True:
    prompt = input("Choose an options:")
    
    if prompt == "go":
        try:
            n = int(input("Enter an integer:"))
        except ValueError:
            print("Invalid Input")
            continue
        
        tot = tot+n 
        cont+=1
        
    elif prompt == 'done':
        print (f"Total: {tot}.\nCount: {cont}.\nMedia: {tot/cont}")
        break
    # cont +=1



# while True:
#     line = input(">")
#     if line[0]=='#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print(line)


# smallest_so_far = None
# print('Before', smallest_so_far)
# for nums in [9,41,12,3,74,15]:
#     if smallest_so_far is None:
#         smallest_so_far = nums
#     elif nums<smallest_so_far:
#         smallest_so_far = nums
#     print(smallest_so_far, nums)

# print(f'After, {smallest_so_far}')

# found = False
# int_list:list[int] = [9,41,12,3,74,15]
# print(f'Before: {found}')
# for value in int_list:
#     if value == 3:
#         found = True
        
#     else:
#         found = False
#     print(found, value)
# print(f'After: {value}')
