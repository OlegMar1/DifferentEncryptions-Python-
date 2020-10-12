from collections import defaultdict
from table import fill_table
from table import get_key
from progress_bar import printCompleatedProgressBar
from collections import Counter


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



def standart_file_statistics(path_in, path_out):
    input_file = open(path_in, "r")
    output_file = open(path_out, "w")
    statistic = []

    for line in input_file:
        for letter in line:
            l = letter.strip()
            if (l == ""):
                l = " "

            statistic += l

    output_file.write("Value\tCount\n")
    a = sorted(Counter(statistic).items())
    for k, v in a:

        rez = str(k) + "\t" + str(v) + "\n"
        output_file.write(rez)

    output_file.close()
    input_file.close()



def encrypted_file_statistics(path_in, path_out):
    input_file = open(path_in, "r")
    output_file = open(path_out, "w")
    statistic = []
    number = ''
    i = 1

    for line in input_file:
        for letter in line:
            #l = letter.strip()
            if(i % 2 != 0):
                number += letter.strip()
                i += 1
            else:
                number += letter.strip()
                statistic.append(number)
                #rezult += get_key(table, number)
                number = ''
                i = 1

    output_file.write("Value\tCount\n")
    a = sorted(Counter(statistic).items())
    for k, v in a:

        rez = str(k) + "\t" + str(v) + "\n"
        output_file.write(rez)

    output_file.close()
    input_file.close()

# ==============MAIN PART==============

print("Decrypting file...")

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

printCompleatedProgressBar()
decrypt_text(input_file, output_file)


print("Decrypting compleated! ")

print("\n===================================================\n")

#==================GET STATISTICS FROM STANDART FILE================

print("Collecting statistics from standart text:")

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

standart_file_statistics(input_file, output_file)

print("\n===================================================\n")


#==================GET STATISTICS FROM ENCRYPTED FILE================

print("Collecting statistics from encrypted text:")

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

encrypted_file_statistics(input_file, output_file)

