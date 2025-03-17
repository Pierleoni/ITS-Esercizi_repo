from typing import Any
def remove_chars(word:str,n:int) ->Any:
    print("Stringa Originale", word)
    remove = word[n:]
    return remove

print(remove_chars("Pynative", 4))
print(remove_chars("Pynative", 2))