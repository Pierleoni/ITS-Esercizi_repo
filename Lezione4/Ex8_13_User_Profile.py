from typing import Any
def build_profile(name, last_name,age, height, description) -> Any:
    greets = f"Hi my name is {name} {last_name}, I'm {age} years old and I'm {height} m tall. \n{description}"
    return greets

myself_descr:Any = build_profile(
    name= "Pietro", 
    last_name="Pacciani", 
    age= 67, 
    height= 1.70, 
    description='''Se ni\' mondo esistesse un po\' di bene,
e ognun si honsiderasse suo fratello,
ci sarebbe meno pensieri e meno pene,
e il mondo ne sarebbe assai più bello''')

print(myself_descr)