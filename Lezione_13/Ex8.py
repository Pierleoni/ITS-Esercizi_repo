def vowelsCounter(word:str)->str:
    if not word:
        return 0
    if word[0].lower() in ["a","e", "i","o","u"] :
        return 1 + vowelsCounter(word[1:])
    else:
        return 0 + vowelsCounter(word[1:])

print(vowelsCounter("Ciao"))

