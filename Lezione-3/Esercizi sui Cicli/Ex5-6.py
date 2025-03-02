person = input("Inserire il nome:")
age = int(input("inserire l'età: ")) 

if age < 2 : 
    print(f"{person} is a baby")
elif 2 <= age < 4: 
    print(f"{person} is a toddler")
elif 4 <= age < 13:
    print(f"{person} is a kid")
elif 13<= age < 20:
    print(f"{person} is a teenager")
elif 20<= age <65:
    print(f"{person} is an adult")
else: 
    print(f"{person} is an elder")
