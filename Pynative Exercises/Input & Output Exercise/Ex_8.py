"""
Formatta le variabili usando il metodo format()
"""

def str_format(quantity = 3, totalMoney = 1000, price = 450 )->str: 
    msg:str= "I have {1} so I can buy {0} football for {2:.2f} dollars"
    print(msg.format(quantity, totalMoney, price))
    


def main():
    str_format( )

if __name__ == "__main__":
    main()