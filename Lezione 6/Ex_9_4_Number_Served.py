
class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str, number_served:int = 0):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        # Punto 1
        self.number = number_served
    
    def describe_restaurant(self):
        # # Punto 2
        print(f"Restaurant Name: {self.restaurant}. \nType of Cuisine: {self.cuisine}, \nNumber of customers: {self.number}.")
    
    def open_restaurant(self):
        print("The Restaurant is open")
    # Punto 4
    def increment_number_served(self):
        self.number += 1
        print(self.number)

r_1:Restaurant= Restaurant("Les Sbuccion", "French Cuisine" )

r_1.describe_restaurant()

r_1.open_restaurant()
print("------------------")
# Punto 3
r_2:Restaurant = Restaurant("A' sora Sofia", "Roman Cuisine",)

r_2.describe_restaurant()
r_2.increment_number_served()

