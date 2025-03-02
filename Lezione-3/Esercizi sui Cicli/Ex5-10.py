current_users_list: list[str] = [
    "Lo stagista schiavo", 
    "Rene", 
    "BIASCICA", 
    "ITALA", 
    "Mariano", 
    "Sergio", 
    "Stanis"
    ]

new_user_list:list[str] = [
    "Duccio",
    "Glauco", 
    "Arianna",
    "Sandra Gusberti",
    "Alessandro", 
    "Corinna",
    "Biascica",
    "Itala"
]

for user in current_users_list:
    
    if user.lower().title() in new_user_list:
        print(f"{user.lower().title()}, il nome è già esistente nel programma ") 
