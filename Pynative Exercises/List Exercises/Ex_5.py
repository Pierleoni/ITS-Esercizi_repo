"""
Trasforma tutti gli elementi di una lista nei loro quadrati
"""

def square_elements(numbers_list: list[int])->None:
    square_list:list[int] = list()
    for nums in numbers_list:
        nums*= nums
        square_list.append(nums)
    print(square_list)


def main()->None:
    square_elements([1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    main()