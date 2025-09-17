"""
Reverse di ogni singola parola di una stringa
"""

def reverse (sentence:str):
    # Splitto la stringa in una lista sugli spazi bianchi
    words:list[str] = sentence.split(" ")
    # Itero per ciascun elemento sulla lista e li reverso usando ::-1
    new_word_list:list[str] = [word[::-1] for word in words]
    
    # Unisco gli elementi della nuova lista in una sola stringa usando il metodo '.join()'
    res_words:str = " ".join(new_word_list)
    return res_words

print(reverse('Hello, World'))



