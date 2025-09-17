"""
Formatta l'output di una stringa
"""

def format_str (str_1:str, str_2:str, str_3:str, str_4:str):
    print(str_1,str_2, str_3, str_4, sep='**')


def main():
    format_str("My", "Name", "Is", "James")

if __name__ == "__main__":
    main()