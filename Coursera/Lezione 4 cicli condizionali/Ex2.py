try:
    in_value = int(input("Digita il totale delle ore di lavoro: "))
    tariffa_oraria = int(input("Digita la tariffa oraria: "))
except:
    raise ValueError ("Errore inserire un numero")

if in_value <= 40:
    paga = in_value * tariffa_oraria
else:
    ore_normali = 40
    ore_straordinarie = in_value - 40
    paga_normale = ore_normali * tariffa_oraria
    paga_straordinaria = ore_straordinarie * tariffa_oraria * 1.5
    paga = paga_normale + paga_straordinaria

print(f"Paga totale: {paga}")



