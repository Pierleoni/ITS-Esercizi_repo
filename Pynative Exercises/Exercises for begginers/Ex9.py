def reverse_num(num_1:int) ->int:
    print("Original Number:", num_1)
    original_number:int =num_1
    reversed_num:int = 0
    while num_1>0:
        reminder = num_1%10
        reversed_num = (reversed_num*10) + reminder
        num_1 = num_1//10
    if original_number == reversed_num:
        print("Given number Palindrome")
    else:
        print("Given number is not palindrome")

reverse_num(121)
reverse_num(125)





