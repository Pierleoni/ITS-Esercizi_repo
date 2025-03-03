
x:tuple[int] = int(input("Inserire numero asse X:"))
y:tuple[int] = int(input("Inserire numero asse y:"))

coordinate:tuple[int,int] = (x,y)
match coordinate:
    case coordinate if y ==0:
        print(f"Il punto {coordinate} si trova sull'asse X")
    case coordinate if x == 0:
        print(f"Il punto {coordinate} si trova sull'asse Y")
    case coordinate if x>0 and y>0:
        print(f"il punto {coordinate} si trova nel primo quadrante")
    case coordinate if x<0 and y>0:
        print(f"Il punto {coordinate} si trova nel secondo quadrante.")
    case coordinate if x<0 and y<0:
        print(f"Il punto {coordinate} si trova nel terzo quadrante.")
    case coordinate if x >0 and y<0:
        print(f"Il punto {coordinate} si trova nel quarto quadrante.")
    case _:
        print(f"Il punto {coordinate} si trova nell'origine.")
