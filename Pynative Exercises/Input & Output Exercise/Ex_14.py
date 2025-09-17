"""
Date due liste crea una tabella in output con a sinistra gli elementi della prima lista
a destra gli elementi della seconda lista
"""
#  Definisco una funzione che riceve due liste (nomi e punteggi) e stampa una tabella
def tabular(names:list[str], scores:list[int]):
    # Stampo l'intestazione delle colonne
    # Name :<8  → colonna larga 8 caratteri, allineata a sinistra
    # Score:<5  → colonna larga 5 caratteri, allineata a sinistra   
    print(f" {'Name':<8} {'Score':<5}")
    
    # Riga di separazione
    print('-'*15)
    
    # Itero sugli elementi di entrambe le liste contemporaneamente
    for  words, numbers in zip(names, scores):
        # words:<8   → i nomi occupano 8 spazi
        # numbers:<5 → i punteggi occupano 5 spazi       
        print(f'{words:<8} {numbers:<5}')


def main():
    tabular(["Alice", "Bob", "Charlie"],[85, 92, 78])

if __name__ == "__main__":
    main()



