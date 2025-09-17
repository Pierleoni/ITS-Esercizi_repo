def display(number_list:list[int]):
    for nums in number_list:
        
        if nums%5==0:
            print(nums)
        

def main():
    display([10, 20, 33, 46, 55])

if __name__ == "__main__":
    main()