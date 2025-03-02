glossary_dict:dict[str] = {
    "indentation": "The use of spaces or tabs to define the structure of code.",
    "comments": "Annotations in the code that are ignored by the interpreter, used for documentation.",
    "statements": "Instructions that a Python interpreter can execute.",
    "lists": "Ordered collections of items that can be changed.",
    "sets": "Unordered collections of unique elements.",
    "dictionaries": "Collections of key-value pairs, where each key is unique."
}

# for key in glossary_dict:
#     print(f"word:{key} \nmeanings: {glossary_dict[key]}")


for key, meaning in glossary_dict.items():
    print(f"Word: {key}\nMeaning: {meaning}\n")