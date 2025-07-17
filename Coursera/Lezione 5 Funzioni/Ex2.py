# try:
#     in_value = int(input("Digita il totale delle ore di lavoro: "))
#     tariffa_oraria = int(input("Digita la tariffa oraria: "))
# except:
#     raise ValueError ("Errore inserire un numero")


def computepay(hours: int, rate: int):
    if hours <= 40:
        paga = hours * rate
    else:
        ore_normali = 40
        ore_straordinarie = hours - 40
        paga_normale = ore_normali * rate
        paga_straordinaria = ore_straordinarie * rate * 1.5
        paga = paga_normale + paga_straordinaria
        return f"Paga totale: {paga}"

print(computepay(45, 10))

