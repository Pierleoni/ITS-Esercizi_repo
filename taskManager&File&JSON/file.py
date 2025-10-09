import json

encoding:str = "utf-8"
PATH: str = "info.json"
with open(PATH, mode='r', encoding=encoding) as file:
    config:dict = json.load(file)
    
    print(config)
    



# Fa il dump : permette di salvare il dizionario sotto forma di file JSON
with open(PATH, mode="w") as file:
    json.dump(config, file, indent=4)



