fruits_list:list[str] = ["Apple", "Peach", "Melon", "Pear"]
if "Watermelon" in fruits_list:
    print("You really like Watermelon")
elif "Grape" in fruits_list:
    print("You really like grape")
elif "Melone" in fruits_list: 
    print("You really like Melone")
elif "Peach"  not in fruits_list: 
    print("You really like", fruits_list[3])
else:
    print("you really like", fruits_list)
    
