string = "Hello"
# string = "World"
if string == "Hello":
    print(True)
elif string != "Hello":
    print(False)

numTest = 5
numTest2 = 10
numTest3 = 12
numTest4 = 10 
numTest5 = 12
numTest6 = 3 
numTest7 =  7 
numTest8 = 14 
numTest9 = 22 
if numTest > numTest2:
    print(False)
elif numTest < numTest2:
    print(True)

if numTest2 == numTest4 and numTest3 == numTest5:
    print(f"{numTest2} e {numTest4}, {numTest3} e {numTest5} sono uguali, perciò:", True)

if numTest6 >= numTest7 or numTest7 <= numTest8:
    print(False)
elif numTest6 <= numTest7 and numTest7 >= numTest8:
    print(False)
elif numTest > numTest6:
    print(True)
elif numTest7 < numTest8:
    print(True)
elif numTest9 > numTest8 and numTest9> numTest2 and numTest9 > numTest3:
    print(True)


test_list:list[int, str] = [1,2,3,4,5,6, "Hello", "AO", "World"]
if "Hello" in test_list:
    print(True)
elif 4 not in test_list:
    print(False)



