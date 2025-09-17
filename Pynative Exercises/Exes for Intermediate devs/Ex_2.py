"""
Leggi un file di testo in una variabile rimpiazzando 
tutte le newlines con gli spazi
"""

with open('sample.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    print(data)
