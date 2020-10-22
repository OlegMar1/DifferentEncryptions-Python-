from collections import defaultdict
from table import fill_table
from progress_bar import printCompleatedProgressBar
import random


def encrypt_text(path_in, path_out):
    table = fill_table()
    rezult = ''
    input_file = open(path_in, "r", encoding='utf-8')
    output_file = open(path_out, "w", encoding='utf-8')

    for line in input_file:
        for letter in line:
            l = letter.strip()
            if(l == ""):
                l = " "
            i = random.randint(0,len(table[l])-1)
            #print(len(table[letter.strip()]))
            rezult += table[l][i]
            #print(rezult)
             
    #print(rezult)
    output_file.write(rezult)
    output_file.close()
    input_file.close()


# ==============MAIN PART==============

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

print("\nEncrypting file...")

printCompleatedProgressBar()
encrypt_text(input_file, output_file)

print("Encrypting compleated! ")