"""
Combina due liste in una sola e stampala

"""


def combine_lists(original_list1: list[int], original_list2: list[int])->None:
    print(f"Liste originarie: {original_list1}, {original_list2}")
    # 1 metodo: con l'operatore '+'
    def operator_plus(lst3:list[int], lst4:list[int])->None:
        combine_list:list[int] = lst3 + lst4
        print(f"La lista risultante è: {combine_list}")
        
    
    #2 metodo: con il metodo .extend()
    
    def extend_method(another_list: list[int], another_list2: list[int])->None:
        new_combine:list[int] = list()
        new_combine.extend(another_list)
        new_combine.extend(another_list2)
        print(f"La lista risultante con il metodo \'.extend()\': {new_combine}")
    
    operator_plus(original_list1, original_list2)
    extend_method(original_list1, original_list2)




def main()->None:
    combine_lists([1, 2], [3, 4])

if __name__ == "__main__":
    main()