from typing import Any
def show_employee(name_emp:str, salary_emp:int = 9000) ->Any :
    return f"Name:{name_emp}, salary: {salary_emp}"

print(show_employee("Carlo"))
print(show_employee("Jessica", 12000))

