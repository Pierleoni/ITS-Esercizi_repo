
def make_shirt(size:str = "L", text_message:str = "I love Python")->None:
    print(f"The size of the t-shirt is {size}, and the phrase is: {text_message}")


sizes:list[str] = ["XS", "S", "M", "L", "XXL"]

for size in sizes:
    if size == "L" and "XXL":
        make_shirt(size)
    else:
        make_shirt(size, "Biggus Dickus")


# make_shirt()
# make_shirt("XXL")
# make_shirt(size="XS", text_message= "Biggus Dickus")
# make_shirt(size = "S", text_message= "Monti Python")





# size_list:list[str] = ["XS", "S", "M", "L", "XXL", "XXXL"]
# for elem in size_list:
#     print(elem)