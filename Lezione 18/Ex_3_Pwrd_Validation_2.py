from Ex_2_Pwrd_Validation import validate_password

class InvalidPasswordError(Exception):
    "La password fa cagare"

if validate_password(password="abcroptmpqABC!#%?hjn"):
    print("La password è ok")
else:
    raise ValueError (f"La password è {InvalidPasswordError}")

print(validate_password("abcroptmpqABC!#%?hjl"))

print("------------------------------")

print(validate_password("abcroptmpqABC!"))