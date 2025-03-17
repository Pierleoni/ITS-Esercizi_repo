def describe_city(city_name:str, country:str = "Mexico")->None:
    print(f"{city_name} is in {country}")

if __name__=="__main__":
    describe_city("Rome")
    describe_city("Ciudad de Mexico")
    describe_city("Springfield")