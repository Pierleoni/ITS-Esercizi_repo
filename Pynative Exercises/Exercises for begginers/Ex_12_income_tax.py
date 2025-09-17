"""
Calcolare l'imposta sul reditto → IRPEF

Prima dei 10,000 si applica lo 0% di aliquota 
Dopo i 10,000 si applica il 10% di aliquota 
Per tutto quello che supera i 20,000$ vine tassato al 20%.

!N.B.: la tassa viene applicata SOLO sull'intero reddito e non sull'eccedente
"""

def income_tax(income:int= 45000)->int:
    
    tax:int = 0
    # Se il reddito è minore o uguale a 10000 
    if income <= 10000:
        # La tassa da applicare è 0%
        tax = 0
        return f"Non ci sono tasse da applicare su questo reddito: {income}"
    # Se il reddito è minore o uguale a 20000 
    elif income <= 20000:
        # Per i primi diecimila non ci sono tasse da applicare
        sott:int = income - 10000
        # Per i successivi invece si applica l'aliquota del 10%
        tax = sott*10/100
        return f"Al reddito di {income} viene applicato il 10% di tasse, quindi il rimanente è: {tax}"
    else:
        # Per i primi 10000 no tasse
        tax = 0
        
        # Oltre i diecimila si applica il 10% di tasse
        tax = 10000 * 10 / 100
        
        
        tax = (income- 20000)*20/100
        return f"Al reddito di {income} viene applicato il 20% di tasse,\
\nquindi il totale delle tasse da pagare è: {tax}"
        
    

def main():
    print(income_tax())
    
    print(income_tax(47000))
    
    
    
    
    
    
    
    
    
    
    
    
    
    # income = 45000
    # tax_payable = 0
    # print("Given income", income)

    # if income <= 10000:
    #     tax_payable = 0
    # elif income <= 20000:
    #     # no tax on first 10,000
    #     x = income - 10000
    #     # 10% tax
    #     tax_payable = x * 10 / 100
    # else:
    #     # first 10,000
    #     tax_payable = 0

    #     # next 10,000 10% tax
    #     tax_payable = 10000 * 10 / 100

    #     # remaining 20%tax
    #     tax_payable += (income - 20000) * 20 / 100

    # print("Total tax to pay is", tax_payable)

if __name__ == "__main__":
    main()