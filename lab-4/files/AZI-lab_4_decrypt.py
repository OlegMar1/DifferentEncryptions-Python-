from table import fill_table
from table import get_key
from progress_bar import printCompleatedProgressBar
#from collections import defaultdict

#alphabet = ' абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

def encrypt_file(key_word, path_in, path_out):
    table = fill_table()
    i = 0
    rezult = ''
    N = len(table)

    input_file = open(path_in, "r")
    output_file = open(path_out, "w")

    for line in input_file:
        

        if (len(key_word) >= len(line.strip())):        # робимо так, щоб текст і гамма були одинакової довжини
            key_word = key_word[0:len(line.strip())]
            #print(key_word)
        else:
            while(len(key_word) < len(line.strip())):
                key_word += key_word
            key_word = key_word[0:len(line.strip())]
            
        #print(line.strip())
        #print(key_word)

        for letter in line:
            l = letter.strip()
            if(letter == '\n'):
                continue
        
            if(l == ""):
                l = " "
            a = int(table[l]) # цифра букви вхідного тексту
            b = int(table[key_word[i]]) # цифра відповідної букви ключа 
            i += 1

            number = (a - b) % N    # цифра букви після кодування 
            #print(number, " ", get_key(table, str(number)))
            rezult += get_key(table, str(number))
            #print(rezult)

    #print(rezult)
    output_file.write(rezult)
    output_file.close()
    input_file.close()


# ==============MAIN PART==============

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")
key_word = input("Please, enter key word: ")


print("\nEncrypting file...")

printCompleatedProgressBar()
encrypt_file(key_word, input_file, output_file)

print("Encrypting compleated!\n")
