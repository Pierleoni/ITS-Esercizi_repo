def sum_primary_diagonal(matrix: list[list[int]])->int:
    
    somma = 0
    somma_2 = 0
    for n in range(len(matrix)):
        somma += matrix[n][n] 
        somma_2 +=matrix[n][len(matrix)-1-n]
    return somma, somma_2


print(sum_primary_diagonal([[1,2,3], [4,5,6], [7,8,9]]))
