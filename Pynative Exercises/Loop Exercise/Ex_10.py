"""
Visualizza il messaggio 'Done!' dopo l'esecuzione del for loop
"""

def display_msg(n:int): 
    for i in range(n): 
        print(i)
    print('Done!')


def main():
    display_msg(5)

if __name__ == "__main__":
    main()