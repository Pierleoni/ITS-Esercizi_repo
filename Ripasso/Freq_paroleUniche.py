import string

def freq_word(txt:str, )-> dict[str,int]:
    
    # Dizionario vuoto che deve contenere le parole come chiave e il numero dei tokens come valori
    dict_count_word:dict[str,int] = {}
    # Per splittare il testo in tokens
    tokens= txt.split()   
    n_tokens = 1

    # Itera sulle parole del messaggio
    for word in tokens:
        # Converte le parole in minuscolo
        word = word.lower()
        
        word = word.strip(string.punctuation) #il .punctuation è un attributo del moudlo string che contiene tutti i caratteri di punteggiatura 
        # Se word equivale a una stringa vuota salta l'iterazione
        if word == "":
            continue
        
        # Se la prarola non si trova dentro il dizionario e gli assegna il valore di defualt di n_tokens 
        if word not in dict_count_word:
            dict_count_word[word] = n_tokens
        
        # Se la parola si trova dentro il dizionario somma il valore di di n_tokens per quante volte quella parola continua a comparirre
        else:
            dict_count_word[word] =n_tokens + n_tokens
    
    return dict_count_word

print(freq_word(" Hello, world! Hello... PYTHON? world."))

