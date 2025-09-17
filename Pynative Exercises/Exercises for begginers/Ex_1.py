"""
Calcolare la moltiplicazione e la somma di due numeri
"""


# Definisco una funzione
def sum_or_multi(n1:int, n2:int):
    # Salvo il prodotto dei due numeri in una variabile 
    multi= n1*n2
    
    # Check se il prodotto è minore o uguale a 1000
    if multi <=1000:
        # ritorno il prodotto
        return multi
    else:
        # Altrimenti salvo l'addizione tra i due numeri in una variabile 'res'
        res = n1+n2
        # Ritorno il valore della variabile 'res'
        return res
    
    


def main():
    print(sum_or_multi(40, 30))
    print(sum_or_multi(20,30))

if __name__ == "__main__":
    main()