import Ex5_addOne
Ex5_addOne.add_one(4)

from Ex8_2_Favorite_Book import favorite_book
favorite_book("Moby Dick")

from Ex8_12_Sandwiches import panino as fn
print(fn("Hamburger", "Peanut Butter", "Trofie al pesto",)) 
#In questo caso ho dovuto mettere il print prima della chiamata della funzione perche nel corpo della funzione c'è un return: quindi mi viene restituito il valore ma non viene stampato in output

import Ex8_5_Cities as mn
mn.describe_city("Barcellona", country="Spain")

from Ex8_15_Printing_Models import*
