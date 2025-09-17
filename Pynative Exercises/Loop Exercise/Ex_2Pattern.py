"""
Stampa il seguente pattern: 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

def patttern(rows:int):
    
    for i in range(1,rows+1,1): 
        for j in range(1, i+1): 
            print(j, end=' ')
        print(' ')


def main():
    patttern(5)

if __name__ == "__main__":
    main()