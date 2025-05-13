def classifica_numeri(lista:int) ->dict[str:list[int]]:
    dict_nums:dict[str:list[int]] = {}
    key1 = "pari"
    key2 = "dispari"
    
    dict_nums.setdefault(key1,[]) #ritorna il valore di un item relativo a una chiave specifica
    dict_nums.setdefault(key2,[])
    
    for num in lista:
        if num %2==0:
            dict_nums["pari"].append(num)
        else:
            dict_nums["dispari"].append(num)
    return dict_nums






# a = {}
# a["abc"] = [1, 2, "bob"]

# key3 = "somekey"
# key4 = "anotherkey"
# a.setdefault(key3, [])
# a.setdefault(key4,[])
# a[key3].append(1)

# print(a)





def filtra_moltiplica(lista_numeri: list[int], fattore:int)->list[int]:
    even_nums:list[int] = [num*fattore for num in lista_numeri if num %2==0]
    
    return even_nums




def aggrega_voti(voti:list[dict])->dict[str:list[int]]:
    dizionario_aggregato = {}
    for key in voti:
        nome = key["nome"]
        voto = key["voto"]
        if nome in dizionario_aggregato:
            dizionario_aggregato[nome].append(voto)
        else:
            dizionario_aggregato[nome] = [voto]
    return dizionario_aggregato



def filtra_e_mappa(prodotti:dict[str:float]) ->dict[str:float]:
    new_dict:dict[str:float] = {}
    for key, value in prodotti.items():
        if value >20:
            prezzo_scontato = value *0.90
            new_dict[key] = prezzo_scontato
            
        else:
            continue
        
    return new_dict

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})) 

print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))


import re
# # Prima parte
# def create_contact(name:str, lastname:str, email:str=None, telefono:int = None) ->dict:
#     contact:dict[str:str,int] = {}
#     contact["nome"] = name
#     contact["cognome"] = lastname
#     email_regex = r'[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}'
#     if email is not None:
#         if re.match(email_regex, email):
#             contact["e-mail"] = email
#         else:
#             raise ValueError ("L'email fornita non è valida")
#     if telefono is not None:
#         contact["telefono"] = telefono
#     return contact


# contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)

# def update_contact(dictionary:dict, name:str, lastname:str, email:str = None, telefono:int = None) ->dict:
#     contact_key:dict = f"{name} {lastname}"
#     if contact_key is dictionary:
#         if email is not None:
#             dictionary[contact_key]["email"] = email
#         if telefono is not None:
#             dictionary[contact_key]["telefono"] = telefono
#         else:
#             raise ValueError(f"Contatto {contact_key} non trovato")
#     return dictionary


# print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))

# print(update_contact(contact, "Mario Rossi", telefono=123456789))


# def create_contact(name: str, email: str = None, telefono: int = None) -> dict:
#     contact = {}
#     email_regex = r'[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}'
#     contact["profile"] = name
#     if email is not None:
#         if email is not None:
#             if re.match(email_regex, email):
#                 contact["email"] = email
#         else:
#             raise ValueError("L'email fornita non è valida")
#     else:
#         contact["email"] = None
#     contact["telefono"] = telefono

#     return contact

# contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
# print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))

# def update_contact(dictionary: dict, name: str, email: str = None, telefono: int = None) -> dict:
#     if dictionary.get("profile") == name:
#         if email is not None:
#             dictionary["email"] = email
#         if telefono is not None:
#             dictionary["telefono"] = telefono
#     else:
#         raise ValueError(f"Contatto {name} non trovato")
#     return dictionary

# print(update_contact(contact, "Mario Rossi", telefono=123456789))

class Animal:
	def __init__(self) -> None:
		self.__name:str = "Generic Animal" # Attributo Privato

animal:Animal = Animal()
# print(animal.name) # Error: 'Animal' object has no attribute 'name'
animal.name = "It's a dog" # Crea un nuovo attributo pubblico 'name'
# print(animal.name) # Output: "It's a dog"
print(animal._Animal__name) # Forzo l'accesso all'attributo privato name

