"""
Conta le occorenze della parola football nella lista
"""
def cont_occur(str_list: list[str])->None:
    
    # 1 metodo: uso il metodo built-in count()
    print(f"Lista originaria: {str_list}")
    def count_method(str_list:list[str])->None:
        occorenza:int = str_list.count('Football')
        print(f"Con il metodo count():{occorenza}")
    
    
    # 2 metodo: itero sugli elementi della lista
    # Definisco una sotto-funzione che prende in input una lista di stringhe
    def cont_occur2(str_list:list[str])->None:
        
        # Inzializzo variabile contatore a 0
        # Serve per contare il numero di occorenze
        cont:int = 0
        
        # Per gli elementi nella lista in input
        for ele in str_list:
            # Check: se l'elemento è uguale alla stringa 'Football' 
            if ele == 'Football':
                
                # Aggiorno il contatore di una unità 
                cont+=1
                
        
        # Stampo il numero di occorenze 
        print(f"Numero di occorenze della parola \'Football\': {cont}")
    
    count_method(str_list)
    cont_occur2(str_list)


def main()->None:
    cont_occur(['Cricket', 'Football', 'Hockey', 'Football', 'Tennis'])

if __name__ == "__main__":
    main()