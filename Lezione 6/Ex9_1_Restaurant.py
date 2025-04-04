# Punto 1
class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
    # Punto 2
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant}. \nType of Cuisine: {self.cuisine}")
    # Punto 3
    def open_restaurant(self):
        print("The Restaurant is open")

r_1:Restaurant= Restaurant("Les Sbuccion", "French Cuisine" )

r_1.describe_restaurant()

r_1.open_restaurant()
