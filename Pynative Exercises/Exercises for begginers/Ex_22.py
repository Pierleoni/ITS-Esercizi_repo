"""
Rendi maiuscoli tutti i primi caratteri delle lettere nella stringa
"""

def cap_str(text:str): 
    words = text.split()
    list_words:list[str] = [word.capitalize() for word in words] 
    return " ".join(list_words)
    

def main():
    print(cap_str("pynative.com is for python lovers"))

if __name__ == "__main__":
    main()