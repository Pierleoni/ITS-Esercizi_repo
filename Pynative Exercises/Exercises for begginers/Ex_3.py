"""
Stampare i caratteri di una stringa con indici pari
"""

def even_chars():
    s = input('La stringa originaria è:')
    print(s)
    size = len(s)
    for chars in range(0, size-1, 2):
        print("index [",chars, "]",s[chars])




def main():
    even_chars()

if __name__ == "__main__":
    main()