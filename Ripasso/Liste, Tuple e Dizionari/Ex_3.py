
def fun_2(dict_prod: dict[str,int|float]) -> dict[str,int|float]:
    dict_p_2:dict = {}
    for keys,values in dict_prod.items():
        if values < 50 :
            new_value = round(values*1.10,2)
            dict_p_2[keys] = new_value
        else:
            continue
    return dict_p_2

print(fun_2({"pane": 2.20, "carne": 55, "pasta": 3.40}))


