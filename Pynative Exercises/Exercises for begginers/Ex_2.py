
"""
Stampare la somma del numero corrente e del numero precedente
"""

# Dichiaro funzione con un parametro passato con valore di defualt a 0
def current_previous(n:int = 0):
    
    previous_num = 0
    # Loop da n a 10
    for nums in range(n, 11):
        # faccio la somma tra il numero precedente con il numero corrente
        somma = previous_num + nums
        
        # Stampo il numero corrente, il numero precedente e la somma tra i due
        print(f"Current number: {nums}, Previous number: {previous_num}  Somma: {somma}")
        
        # Aggiorno la variabile previous_num con il numero corrente in modo che
        # Ad ogni iterazione previous_num si aggiorni fino a 10
        previous_num = nums



def main():
    current_previous(1)

if __name__ == "__main__":
    main()