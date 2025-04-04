


class Food:
    def __init__(self, name:str, price:float, description:str):
        self.name = name 
        self.price = price
        self.description = description
    

class Menù:
    def __init__(self, foods:list[Food] = []):
        self.foods = foods
    def addFood(self, food:Food):
        self.foods.append(food)
    def getFoods(self):
        return self.foods
    def removeFood(self, index:int):
        if len(self.foods) > 0:
            self.foods.pop(index)
        #if remove_name in self.foods:
        #    self.foods.remove(remove_name)
        #else:
        #    print(f"{remove_name}")
    def printPrices(self):
        for food in self.foods:
            print(f"{food.name}: {food.price}")
    def getAveragePrice(self):
        food_prices = [f.price for f in self.foods]
        return sum(food_prices) / len(food_prices)


f1:Food = Food ("Lasagna", 10.50, "Lasagna is a traditional Italian dish made of layered pasta sheets, meat or vegetable filling, tomato sauce, béchamel, and cheese, typically baked until golden and bubbly" )
f2:Food = Food ("Ramen", 12.00, "Ramen is a Japanese noodle soup consisting of wheat noodles served in a flavorful broth, typically made with soy sauce or miso, and topped with ingredients like sliced pork, green onions, seaweed, and eggs")
f3:Food = Food ("Spaghetti con la bottarga di muggine", 13.50, "Spaghetti with mullet bottarga is an Italian pasta dish featuring dried, salted, and cured fish roe grated over spaghetti, often enhanced with garlic, olive oil, and lemon zest for a rich and savory flavor")
menu = Menù([Food("pizza", 5.50, "o sole mio"), Food("pasta", 12.00, "Ciao"), Food("salad", 4.50, "Ciao")])
f4:Food = Food ("Burger", 12.40, "A burger is a popular sandwich consisting of a cooked ground meat patty, usually beef, placed inside a sliced bun and often topped with ingredients like lettuce, tomato, cheese, onions, and sauces.")
f5:Food = Food ("Caeser Salad", 7.50, "Caesar salad is a classic dish made with romaine lettuce, croutons, parmesan cheese, and a creamy dressing typically made from egg, lemon juice, anchovies, garlic, and olive oil. It is often served with grilled chicken or shrimp." )
f6:Food = Food ("Onion Rings", 3.30, "Onion rings are a popular snack or side dish made of onion slices dipped in batter or breadcrumbs and deep-fried until crispy and golden brown.")

menu.addFood(f1)
menu.addFood(f2)
menu.addFood(f3)
menu.addFood(f4)
menu.addFood(f5)
menu.addFood(f6)

menu.removeFood(0)
menu.removeFood(1)
menu.removeFood(2)

menu.printPrices()
print(menu.getAveragePrice())
# menu.getAveragePrice()



