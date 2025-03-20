

def merged (list_1:list[int], list_2:list[int]) -> list:
    res_list:list[int] = []
    for nums in range(1,10):
        if nums%2!=0:
            res_list.append(nums)
    for nums in list_2:
        if nums%2==0:
            res_list.append(nums)
    print(res_list)
    


merged(10,20,45,60)