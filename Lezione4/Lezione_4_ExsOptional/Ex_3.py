def product(name:str, price:float, quantity:int):
    
    print(f"Nome prodotto: {name}.\nPrezzo del prodotto: {price}. \nQuantità del prodotto: {quantity}")

def shop_cart(cart:dict[str,float],name:str, option: list = ["esci", "aggiungi", "rimuovere"]):
    print(cart)
    
    name:str = str(input("Aggiungere un prodotto:"))
    price:float = float(str(input("Aggiungere un prezzo:")))
    quantity:int = int(str(input("Aggiungere una quantita:")))
    if name and price and quantity not in cart:
        if quantity<0:
            print("Errore! La quantità inserita deve essere un numero intero positivo")
        cart[name] = price
        cart["Quantità"] = quantity 
        
        print(cart)
    
    rem_name = str(input("Rimuovere il prodotto:"))
    if rem_name in cart:
        del cart[rem_name]
        del cart["Quantità"]
        print("Prodotto rimosso", cart)
    else:
        print(cart)



def tot_cart(name:str, price: float, quantity:int,sale: int, taxes:int ):
    tot = price*quantity
    
    if sale in range(1,100):
        sconto = price*sale/100
        
    else:
        pass
    if taxes in range(1,25):
        iva = price*(1+taxes/100)

    else:
        print(tot)
    return name, tot, sconto, iva
    # print(f"Nome del prodotto: {name}. \nPrezzo del prodotto: {price}.\nQuantità del prodotto: {quantity}")
    # print(f"Prezzo totale: {tot}.\nSconto applicato: {sconto}.\nIVA:{iva} ")



def summary(cart_sum: dict[str, float|int], name: str,price:float, quantity: int ):
    totale = price*quantity
    if name and price and quantity and totale in cart_sum:
        cart_sum[name] = price
        cart_sum["Quantità"] = quantity
        cart_sum["Totale"] = totale
        print(cart_sum)
    else:
        pass
    
product("Pane", 4.89, 2)

shop_cart({"Pane": 4.89}, "nome")
print("-------------------------------")



print(tot_cart("Pane", 4.89, 2, 10, 22))





