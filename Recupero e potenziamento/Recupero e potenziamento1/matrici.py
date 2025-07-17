import random
def genera(dim: int)-> list[list[int]]:
    matrix:list[list[int]] = []
    for r in range (dim):
        row : list[int] = []
        for c in range(dim):
            # num_matrix:int = random.sample(range(0,13),dim)
            while True:
                n:int = random.randint(0,13)
                if c ==0:
                    row.append(n)
                    break
                if n!= row[0]:
                    row.append(n)
                    break
        
        matrix.append(row)
    return matrix





    # for i in matrix:
    #     print(i)


def printMAT(mat:list[list[int]])->list[list[int]]:
    for r in range (len(mat)):
        for c in range(len(mat[r])):
            print(f"{mat[r][c]:<5}", end="")
        print("\n")


def calcolaCarico(matrice: list[list[int]],index_r:int, index_c: int)->int:
    somma_righe = 0
    somma_colonna = 0
    for i in matrice[index_r]:
        somma_righe +=i
        for j in matrice:
            somma_colonna += len(matrice[j][index_c])
        carico = somma_righe - somma_colonna
    return carico
        


def caricoNullo(mat:list[list[int]])-> list[tuple]:
    pass



def main()->None:
    genera_mat = genera(5)
    printMAT(genera_mat)
    


if __name__=="__main__":
    main()