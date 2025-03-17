def panino(*toppings:list)->list[str]:
    
    return list (toppings) #in questo modo sto convertendo una tupla in una lista 

if __name__=="__main__":
    menù_1= panino("Pomodori", "Salsiccia", "Insalata", "Scarola")
    print(f"Il menù ordinato è:{menù_1}")

    menu_2 = panino("Tofu", "Avocado", "Pomodori", "Insalata", "Falafel")
    print(f"Il menù ordinato è : {menu_2}")

    menu_3 = panino("French Fries", "Ketchup", "Stracetti di soia", "Polpette di seitan")
    print(f"Il menù ordinato è : {menu_3}")