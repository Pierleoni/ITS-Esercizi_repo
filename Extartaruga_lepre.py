import random 

# lista_percorso:list[str] = ["_"]*70

# lepre: str = "H"
# tart:str = "T"
# lista_percorso[0] = lepre, tart

# print(lista_percorso)

# n= random.randint(1,10)
# print(n)
lista_percorso:list[str] = ["_"]*70
tart_pos:int = 1
lepre_pos:int = 1

lista:list[int] = [1,2,3,45,66,7,6,89,70,10,22,33,3]*10

print(lista[+3])


def mossa_tart(i:float) ->float:
    i = random.randint(1,10)
    if i>=1 and i<=5:
        tart_pos += 3
    elif i>=8 and i<=10:
        tart_pos+=1
    else:
        tart_pos-=6
        if tart_pos <=0:
            tart_pos = 1
    





def posizioni_gara( lepre: str = "H",tart:str = "T" ):
    

    
    return lista_percorso
    



