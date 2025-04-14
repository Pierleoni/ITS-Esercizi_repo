def validate_password(password:str) -> str:
    alfa_count = 0
    upper_count = 0
    for char in password:
        if char.isupper():
            upper_count +=1
        
        if not char.isalpha():
            alfa_count +=1
    if len(password) == 20 and upper_count >= 3 and alfa_count >= 4:
        return "The password is valid"
    else:
        raise ValueError("The password is invalid")


try:
    result = validate_password("ABC_@[]abc123tyr3wqtpn")
    print(result)
except ValueError as e:
    print(e)

res_1 = validate_password("abcroptmpqABC!#%?hjn")

print(res_1) 
