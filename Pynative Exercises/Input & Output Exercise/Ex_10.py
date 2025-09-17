"""
Leggi solo la riga N.4 da un file
"""
def read_one():
    with open ('newFile.txt', 'r') as file:
        contenuto = file.readlines()
        print(f'La quarta riga: {contenuto[4]}')

def main():
    read_one()

if __name__ == "__main__":
    main()