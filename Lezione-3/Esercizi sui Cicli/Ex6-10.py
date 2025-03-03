people_dict:tuple[str, int] = {
    "Giacomo": (23, 66), 
    "Carlo": (33, 87), 
    "Federico": (12, 24), 
    "Erica": (99, 22), 
    "Giancarlo": (45,75), 
    "Enrica":(13, 23)
}

for key, number in people_dict.items():
    print(f"nome: {key} \nnumero:{number}\n")