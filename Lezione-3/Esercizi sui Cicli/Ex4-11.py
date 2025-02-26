pizza_list:list[str]= ["Margherita", "Alici e fiori di zucca", "Mare e monti"]
pizza_friend_list:list[str]= ["Margherita", "Alici e fiori di zucca", "Mare e monti"]
pizza_list.insert(2, "Quattro formaggi")
pizza_friend_list.append("Pizza con nutella")
print(pizza_list, pizza_friend_list)
print("My favourite pizzas are:")
for pizza in pizza_list:
    print(pizza)

print ("\nMy friend's favourite pizzas are:")
for pizzas in pizza_friend_list:
    print(pizzas)


