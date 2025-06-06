def fun(num_list:list[int|float])->dict[str,list[int|float]]:
    dict_pos:dict[list[int|float]] = {"positivo":[], "negativo": []}
    for nums in num_list:
        if nums >=0:
            dict_pos["positivo"].append(nums)
        else:
            dict_pos["negativo"].append(nums)
    return dict_pos

print(fun([-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,3.14]))