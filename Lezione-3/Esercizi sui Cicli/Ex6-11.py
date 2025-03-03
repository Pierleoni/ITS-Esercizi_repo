from typing import Any
cities_dict:dict[str, dict] = {
    "Rome":
        {"Nation": "Italy", "Population":2.748165, "Fact": "It has 1,500 fountains"},  
    "Bogota":
        {"Nation": "Colombia", "Population": 11.658200, "Fact": "It has the biggest bike lane in the World"},  
    "Tokyo":
        {"Nation": "Japan", "Population": 37.000000, "Fact":  "It has the highest number of Michelin-starred restaurants in the world "},
    "Vienna":
        {"Nation": "Austria", "Population": 2.005760, "Fact": "It's the most famous city for its pubblic transport efficienty" }
}

for key, value in cities_dict.items():
    print(f"{key}: {value}")


