"""
Controlla se un anno è bisestile
"""

def leap_year(year:int)->bool:
    if year %4 ==0 :
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def main():
    print(leap_year(2020))
    print(leap_year(2025))
    print(leap_year(2000))
    

if __name__ == "__main__":
    main()