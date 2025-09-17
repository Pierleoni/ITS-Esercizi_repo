"""
Calcola il cubo di tutti i numeri dal 1 fino al numero dato
"""

def cube_num(n:int):
    for i in range(1,n+1): 
        res = i**3
        print(f"Current number: {i} and the cube is {res}")


def main():
    cube_num(6)

if __name__ == "__main__":
    main()