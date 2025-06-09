from string import ascii_lowercase


def ceasar_cipher( message:str, key:int)->str:
    # Converte il valore di message in minuscolo 
    message = message.lower()
    # Questa variabile serve per contenere il messaggio criptato
    encrypted_message = ""
    # itera su ogni lettera del messaggio
    for letter in message:
    
        # Controlla se la lettera si trova dentro la lista alphabet
        if letter in ascii_lowercase:
            # Trova l'indice della lettera scorrendo dal primo indice  fino all'ultimo della lista alphabet
            new_letter = ascii_lowercase.index(letter)
            # somma l'indice trovato con il valore di key 
            result = (new_letter + key) % len(ascii_lowercase)
            # punta al valore di result
            encrypted_letter = ascii_lowercase[result]
            # Aggiunge la lettera cripttata all messaggio criptato
            encrypted_message +=encrypted_letter
        else:
            encrypted_message += letter
            
    return encrypted_message


print(ceasar_cipher("ciao", -3))
print(ceasar_cipher("ciao", 3))
print(ceasar_cipher("hello world!", 3))
print(ceasar_cipher("BUONGIORNO", 3))


