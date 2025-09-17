
def first_last(n_list:list[int]):
    print(f'Data la lista: {n_list}')
    
    first_num = n_list[0]
    last_num = n_list[-1]
    if first_num == last_num:
        return True
    else:
        return False



def main():
    print( first_last([10, 20, 30, 40, 10]))
    print( first_last([75, 65, 35, 75, 30]))

if __name__ == "__main__":
    main()
