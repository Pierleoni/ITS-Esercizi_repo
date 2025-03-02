list_user:list[str] = [
    "Jade", 
    "Ciro", 
    "Louis", 
    "Giorgio", 
    "Claudia", 
    "Benny", 
    "Topolindo", 
    "Heroin Bob", 
    "admin"
]

if "admin"in list_user:
    print(f"Hello admin, would you like to see a status report? ")
else:
    print(f"Hello {list_user}, thank you for logging in again")
