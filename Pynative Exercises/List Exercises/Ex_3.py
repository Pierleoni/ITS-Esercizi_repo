"""
Calcolare la somma e la media di tutti i numeri in una lista
"""
def somma_media(my_list: list[int])->None:
    somma:int = sum(my_list)
    media:int = sum(my_list)/len(my_list)
    print(f"Somma:{somma}\nMedia: {media}")


def main()->None:
    somma_media([10, 20, 30, 40, 50])

if __name__ == "__main__":
    main()