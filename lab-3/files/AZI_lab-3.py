from collections import defaultdict
from table import fill_table
from table import get_key
from progress_bar import printCompleatedProgressBar


def decrypt_text(path_in, path_out):
    table = fill_table()
    rezult = ''
    number = ''
    i = 1
    input_file = open(path_in, "r")
    output_file = open(path_out, "w")

    for line in input_file:
        for letter in line:
            if(i % 2 != 0):
                number += letter.strip()
                i += 1
            else:
                number += letter.strip()
                rezult += get_key(table, number)
                number = ''
                i = 1
             
    #print(rezult)
    output_file.write(rezult)
    output_file.close()
    input_file.close()


# ==============MAIN PART==============

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

print("\nDecrypting file...")

printCompleatedProgressBar()
decrypt_text(input_file, output_file)

print("Decrypting compleated! ")



