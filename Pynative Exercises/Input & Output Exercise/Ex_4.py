"""
Visualizza un numero con la virgola arrodontato di due posizioni decimali 
"""

def pos_float(n: float)->str: 
    # %.2f: arrodonta per eccesso alla seconda cifra decimale di un numero float
    print("%.2f"%n)


def main():
    pos_float(458.541315)

if __name__ == "__main__":
    main()