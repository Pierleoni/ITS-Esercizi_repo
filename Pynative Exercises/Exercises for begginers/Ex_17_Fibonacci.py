"""
Generare una serie di Fibonacci che sale per 15 termini
"""

def fibonacci(n:int)->int:
    if n<=0:
        return 0 
    elif n == 1:
        return 1
    else: 
        return int(fibonacci(n-1)+ fibonacci(n-2))
    


def fibo(num_1:int, num_2:int)->int:
    # Per ogni numero nel range di 15 
    for i in range(15):
        # Aggiorno il vlaore di num_1 con il valore di num_2
        num_1 = num_2
        # Aggiungo gli ultimi due numeri per avere i numeri successivi
        
        res = num_1 + num_2
        # Aggiorno il valore di num_2 con il valore del risultato
        num_2 = res
        
        # Stampo
        print(num_1, end=" ")
    

def main():
    print('Primo Approccio:')
    print(fibonacci(15))
    print('\nSecondo approccio:')
    fibo(0,1)

if __name__ == "__main__":
    main()