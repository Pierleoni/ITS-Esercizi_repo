# x = 5
# y = 10
# z = 15

# if x<5 and y>x:
#     print(True)
# else:
#     print(False)

# if x<5 or y>x:
#     print(False)
# else:
#     print(True)


# def transform(x:int)->int:
#     if x %2==0:
#         return  x//2
#     else:
#         return x*3-1


# def print_seq():
#     print("Sequenza a):")
#     for num in range(1, 8):
#         print(num)

#     print("\nSequenza b):")
#     for i in range(3, 24, 5):
#         print(i)

#     print("\nSequenza c):")
#     for j in range(20, -11, -6):
#         print(j)

#     print("\nSequenza d):")
#     for nums in range(19, 52, 8):
#         print(nums)
#     return 

# print_seq()

# def integerPower(base:int, esponente:int)->int:
#     result = 1
#     for i in range(esponente):
#         result*=base

#     return result

# print(integerPower(2,3))

# import math
# def hypotenuse(l_1:float, l_2:float)->float:
#     esponente = 2
#     result = math.sqrt((l_1**esponente)+(l_2**esponente))
#     return result

# print(hypotenuse(3,4))

# numbers: list[int] = [1, 2, 3, 4, 5]

# for i in numbers:
#     print('Number:', i) 


# def seconds_since_noon(ore:int,min:int, sec:int) ->int:
#     ore = ore*3600
#     min = min*60
#     tot_sec = ore+min+sec
#     return tot_sec




# def time_difference(ore1: int, minuti1: int, secondi1: int, ore2: int, minuti2: int, secondi2: int) -> int:
#     if seconds_since_noon(ore1, minuti1, secondi1) > seconds_since_noon(ore2, minuti2, secondi2):
#         return seconds_since_noon(ore1, minuti1, secondi1) - seconds_since_noon(ore2, minuti2, secondi2)
    
#     elif seconds_since_noon(ore2, minuti2, secondi2) > seconds_since_noon(ore1, minuti1, secondi1):
#         return  seconds_since_noon(ore2, minuti2, secondi2) - seconds_since_noon(ore1, minuti1, secondi1)
    
#     else:
#         return 0


# def rimbalzo():
#     # Valori iniziali
#     altezza = 0.0
#     velocita = 100.0
#     tempo = 0
#     rimbalzi = 0
    
#     print(f"Tempo: {tempo} Altezza: {altezza}")
    
#     # Continua fino al quinto rimbalzo
#     while rimbalzi < 5:
#         tempo += 1
        
#         # Aggiorna altezza e velocità
#         altezza = altezza + velocita
#         velocita = velocita - 96.0
        
#         # Controlla se c'è un rimbalzo
#         if altezza < 0:
#             # Simula il rimbalzo
#             velocita = velocita * -0.5
#             altezza = altezza * -0.5
#             rimbalzi += 1
#             print(f"Tempo: {tempo} Rimbalzo!")
#         else:
#             print(f"Tempo: {tempo} Altezza: {altezza}")

# def rimbalzo():
#     tempo = 0  
#     altezza = 0.0  
#     velocita = 100
#     rimbalzi = 0  

#     while rimbalzi < 5: 
#         if altezza < 0: 
#             print(f"Tempo: {tempo} Rimbalzo!")
#             rimbalzi += 1
#             altezza *= -0.5
#             velocita *= -0.5
#         else:
#             print(f"Tempo: {tempo} Altezza: {altezza}")
#             altezza +=velocita
#             velocita-=96
#         tempo +=1


# rimbalzo()


import math

def memorizza_file(files:list[int]):
    blocchi_disponibili = 1000  
    
    for dimensione in files:
        dimensione_compressa = dimensione * 0.8
        
        
        blocchi_necessari = round(dimensione_compressa / 512)
        
        if blocchi_necessari <= blocchi_disponibili:
            
            blocchi_disponibili -= blocchi_necessari
            print(f"File di {dimensione} byte compresso in {dimensione_compressa:.1f} byte e memorizzato. Blocchi usati: {blocchi_necessari}. Blocchi rimanenti: {blocchi_disponibili}.")
        else:
            
            print(f"Non è possibile memorizzare il file di {dimensione} byte. Spazio insufficiente.")
            break


memorizza_file([1100, 20000, 1048576, 512, 5000])
