favourite_places:dict[str] = {
    "Ronnie": "Tokyo", 
    "Giovanni": "Roma Termini", 
    "Lorenzo": "Stazione Tiburtina"
}

print("\nWhat's your favourite place?")
for key,place in favourite_places.items():
    print(f"Nome: {key}; Posto: {place}")
