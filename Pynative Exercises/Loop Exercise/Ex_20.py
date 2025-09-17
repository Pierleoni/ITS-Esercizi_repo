"""
Stampa il pattern di numeri alternati
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15
"""
def alt_pattern(rows:int)->None:
    for i in range(1,rows+1): 
        if i%2==0:
            for j in range(1,i+1):
                print(j, end=' ')
        else: 
            for k in range(1,i+1):
                print(k, end=' ')
        print()

def main():
    alt_pattern(5)

if __name__ == "__main__":
    main()