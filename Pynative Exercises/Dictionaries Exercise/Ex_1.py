""" 
Operazioni basi sui dizionari
"""

def basic_ops_dict(my_dict: dict[str, int|str])->str:
    print(f'Dizionario originale: {my_dict}')
    """ 
    1. Aggiungere coppie di chiave valore al dizionario
    """
    
    print()
    
    # 1 metodo
    def key_val_squareBrackets(d: dict[str, str|int])->str:
        """ 
        #Salvo in una variabile l'aggiunta della chiave 'profession' e del suo valore associato
        val = d['profession'] = 'Doctor'
        #Ma mi restiuisce solo il valore della chiave poichè 'val' contiene solo il valore e non la chiave
        Se volessi vedere anche la chiave dovrei fare
        d['profession'] = 'doctor'
        key, val = 'profession', d['profession']
        
        In questo modo la variabile key contiene la chiave 
        e la variabile val contiene il valore della chiave
        """
        # Al dizionario aggiungo la coppia chiave-valore
        d['profession'] = 'Doctor'
        # Stampo in output il risultato
        print(f"\nCon il metodo delle parentesi quadre []: {d} ")
    
    # 2 metodo
    def key_val_updateMethod(d: dict[str, str|int])->str: 
        # Salvo in una variabile il risultato del dizionario aggiornato
        # Uso il metodo .update(): 
            # Questo metodo permette di aggiungere più coppie di chiave-valore a un dizionario
            # o di modificare uno gia esistente
        """
        In particolare come arogmento del metodo si passa un altro dizonario 
        o un iterabile formato da coppie chiave-valore 
        per aggiungere queste coppie a un dizionario già esistente
        """
        d.update({'profession':'Doctor'})
        
        # Salvo l'update in una variabile che contiene il dizionario in input + l'aggiunta della coppia chiave-valore
        update: dict[str, str] = d
        print(f"\nCon il metodo built-in .update(): {update}")
    
    # Terzo metodo
    # Uso il dictionary unpacking
    def key_val_dictUnpacking(d: dict[str, str|int])-> str:
        
        # Salvo in una variabile l'unpacking del dizionario e l'aggiunta di una coppia chiave-valore
        unpacking: dict[str, str] = {**d, 'profession': 'Doctor'}
        
        # Stampo in output il risultato
        print(f"\nUsando l'operatore \'**\' per l'unpacking: {unpacking} ")
    
    # QUarto metodo
    # Uso il costruttore dict() per aggiungere la coppia chiave-valore
    def key_val_dictConstructor(d: dict[str, str|int])->str:
        # Salvo in una variabile l'aggiunta della coppia
        # Tramite dict() passo come arogmento il dizionario in input e la coppia chiave-valore
        #! Questo metodo è utile quando si vuole creare un nuovo dizionario che include sia l'originale che le modifiche degli elementi
        dict_constructor = dict(d, profession = 'Doctor')

        print(f"\nCon il dict constructor (dict()): {dict_constructor}")
    
    
    """ 
    2. Modificare il valore della chiave 'age'
    """
    # 1 metodo: 
        # Uso le square brackets '[]'
    def modify_valKey_brackets(d: dict[str, str|int])->str:
        
        # Accedo alla chiave 'age' del dizionario 'd' e cambio il valore della chiave da 35 a 40
        d['age'] = 40
        
        # Salvo il dizionario aggiornato nella variabile 'modifica'
        modifica = d
        
        # Stampo in output il risultato
        print(f"\nModifico il valore della chiave \'age\' usando le square brackets \'[]\': {modifica}")
    
    
    # 2 metodo : uso il metodo built-in .update()
    def modify_valKey_update(d: dict[str,str|int])->str:
        
        # Tramite il metodo .update() acceddo alla chiave 'age' (passandola come argomento del metodo)
        # Del dizionario 'd' e aggiorno il valore a 40
        d.update({'age': 40})
        
        # Salvo il dizionario aggiornato nella variabile 'mod'
        mod = d
        
        # Stampo in output il risultato
        print(f"\nCon il metodo .update(): {mod}")
    
    
    # 3 metodo: usare l'unpacking dei dizionari
    def modify_valKey_unpacking(d: dict[str,str|int])-> str:
        
        # Creo un nuovo dizionario chiamato unpack in cui salvo e spacchetto tutte le coppie chiave-valore del dizionari 'd'
        # Accedo alla chiave 'age' e aggiorno il valore a 40
        unpack:dict[str, str|int] = {**d, 'age': 40 }
        
        
        
        
        # Stampo in output il risultato
        print(f"\nUsando l'unpacking dei dizionari: {unpack}")
        
        
    
    
    """ 
    3. Accedere al valore della chiave 'city'
    """
    # 1 metodo: uso le square brackets
    def accessKey_Val_squareBrackets(d: dict[str, str|int])->str:
        
        # Creo una variabile in cui salvo il valore della chiave 'city' nel dizionario d
        accessSquare_brackets:str = d['city']
        
        # Stampo il risultato
        print(f"\nCon le square brackets \'[]\': {accessSquare_brackets}")
    
    
    # 2 metodo: uso il metodo .get()
    def access_keyVal_getMethod(d: dict[str, int|str])->str:
        
        # Salvo il valore della chiave 'city' in 'd' in una variabile 
        access_via_get: str = d.get('city')
        
        # Stampo in output il valore della chiave
        print(f"\nUsando il metodo .get(): {access_via_get}")
    
    
    # 3 metodo: uso un for loop con l'operatore in
    def access_keyVal_inOps(d: dict[str, int|str])->str:
        
        # Itero sulle chiavi del dizionario in input
        for key in d: 
            # Check: se la chiave equivale alla stringa 'city'
            if key == 'city': 
                
                # Stampo in output il suo valore 
                print(f"Usando un for loop con l\'operatore \'in\': {d[key]}")
                
            #! Ridondante: il ciclo continua di defualt
            # else: 
            #     continue
            
            
    
    
    
    
    print('Metodi per aggiungere coppie di chiave valore al dizionario:')
    key_val_squareBrackets(my_dict.copy())
    key_val_updateMethod(my_dict.copy())
    key_val_dictUnpacking(my_dict.copy())
    key_val_dictConstructor(my_dict.copy())
    print('----------------------------------------------')
    print('Metodi per modificare il valore della chiave:')
    print(f"\nDizionario originale : {my_dict}")
    modify_valKey_brackets(my_dict.copy())
    modify_valKey_update(my_dict.copy())
    modify_valKey_unpacking(my_dict.copy())
    
    print('--------------------------------------------------------')
    print("Metodi per accedere al valore della chiave \'city\': ")
    print(f"Dizionario Originale: {my_dict}")
    accessKey_Val_squareBrackets(my_dict)
    access_keyVal_getMethod(my_dict)
    access_keyVal_inOps(my_dict)
    
    


def main()->None:
    basic_ops_dict({'name': 'Alice', 'age': 35, 'city': 'New York'})

if __name__ == "__main__":
    main()