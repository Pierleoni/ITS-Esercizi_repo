def car_specifics(manifacturer: str, modelname: str, **optional):
    mycar: dict = {"Manifacturer": manifacturer, "modelname": modelname, **optional}
    return mycar

cars= car_specifics('subaru', 'outback', color= 'blue', tow_package= True)

print(cars)