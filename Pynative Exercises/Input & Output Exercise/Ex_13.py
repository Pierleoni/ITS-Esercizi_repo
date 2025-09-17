"""
Visaulizza l'output allineata a destra
"""

def right_aligned(s:str, n:int)->str:
    print(f"{s:>20}{n}")


stringa:str = input('Enter a string: ')
number:int = int(input('Enter a number: '))

def main():
    right_aligned(stringa, number)

if __name__ == "__main__":
    main()