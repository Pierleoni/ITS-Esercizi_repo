"""
Scrivi il contenuto di un file in un nuovo file 
saltando la riga 5
"""

from typing import TextIO
def skip_line()->TextIO:
    with open('text1.txt', 'r') as text: 
        all_lines:list[str] = text.readlines()
        # return all_lines
    with open ('test2.txt', 'w') as t:
        
        
        cont = 0
        
        for line in all_lines: 
            
            # print(line)
            if cont == 4: 
                # print(cont)
                cont+=1
                continue
            else:
                
                t.write(line)
                
            cont+=1
        # return lines





def main():
    skip_line()

if __name__ == "__main__":
    main()