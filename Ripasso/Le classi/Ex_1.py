class ContactManager():
    def __init__(self, contacts:dict[str,list[str]] = {}):
        self.contacts = contacts
    def set_contacts(self,contacts):
        self.contacts = contacts
        """
        Questa funzione aggiunge un nuovo contatto al dizionario 
        e ritorna un nuovo dizionario con il nome e il numero di telefono
        """    
    def create_contacts(self, name: str,phone_number:list[str])-> dict[str, list[str]]:
        if name  in self.contacts:
            raise ValueError("Errore: il contatto non è nella rubrica")
        else: 
            self.contacts[name] = phone_number
            return {name:phone_number}
        # Questa funzione aggiunge un numero di telefono alla lista di n. di tel associati al nome del contatto
    def add_phone_number(self, contact_name:str, phone_number:str )->dict[str, list[str]]:
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste!")
        if phone_number  in self.contacts[contact_name] :
            raise ValueError ("Il numero è già associato al contatto!")
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}
    # QUesta funzione rimuove un numero di telefono
    def remove_phone(self, contact_name:str, phone_number: str):
        if contact_name  not in self.contacts:
            raise ValueError("Errore: il contatto non esiste")
        if phone_number in self.contacts[contact_name]:
            self.contacts[contact_name].pop()
        else:
            raise ValueError("Errore: il numero di telefono non è presente. ")
        return {contact_name: self.contacts[contact_name]}
    # Questa funzione aggiunge un nuovo numero di telefono rimpiazzando il numero vecchio
    def update_phone_number(self, contact_name: str, old_phone_number: str,new_phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Il numero non è presente")
        index:int =self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number
        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self)->list[str]:
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name:str)-> str:
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste")
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str)-> list[str]:
        contact_list:list[str] = []
        for contact, list_contacts in self.contacts.items():
            if phone_number in list_contacts:
                contact_list.append(contact)
        if not contact_list:
            raise Exception("Nessun contatto trovato con questo numero di telefono!")
        return contact_list
        
    

ctm:ContactManager= ContactManager({"marco": ["3489056080"]})
print(ctm.create_contacts("Alessio",["349823456"]))
print("----------------------------------------")
print(ctm.add_phone_number("Alessio","349823457"))
print("----------------------------------------")
print(ctm.remove_phone("Alessio","349823457"))
print("----------------------------------------")
print(ctm.update_phone_number("Alessio", "349823456", "347323457" ))
print("----------------------------------------")
print(ctm.list_contacts())



