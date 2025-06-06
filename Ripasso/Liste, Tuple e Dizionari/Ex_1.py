from typing import Any
def convert(list_tuple:list)-> dict:
    dict_1:dict[Any, Any] = {}
    for key,value in list_tuple:
        if key in dict_1:
            dict_1[key] += value 
        else:
            dict_1[key] = value
    return dict_1
    
    # for k in dict(list_tuple).keys():
    #     if k in dict(list_tuple):
            
    # return dict(list_tuple)

print(convert([("Valore", 1),("Valore", 1)]))