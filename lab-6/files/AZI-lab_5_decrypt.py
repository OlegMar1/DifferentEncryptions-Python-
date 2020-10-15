from table import fill_table
from progress_bar import printCompleatedProgressBar


def decrypt_file(path_in, path_out):

    table = fill_table()

    counter = 1 # потрібно для зчитування 2 букв з файла і запис в pair
    rezult = '' 
    pair = '' # пара з 2 букв
    coordinates = [] # двовимірний масив, в 1 підмасиві координати 1 букви з поточної пари, в 2 підмасиві координати 2 букви з поточної пари
    flag = 0 # це перевірка, чи знайшла функція вже 2 букви, щоб приступити до їх шифрування
    k = 1 # потрібна для того, щоб функція спочатку знайшла 2 букви, а вже потім почала їх щифрувати

    input_file = open(path_in, "r")
    output_file = open(path_out, "w")

    for line in input_file:
        
        for letter in line:     #проходження по файлі
            #pair = ''
            l = letter.strip()

            if(letter == '\n'):
                continue      
            if(l == ""):
                l = " "

            if((counter % 2) != 0):     #зчитуємо по 2 букви в pair перед тим як піти до самого шифрування
                pair += l
                counter += 1
                continue

            pair += l

            #i = 0
            #j = 0            
            for i in range(len(table)):
                letter_i = table[i]
                for j in range(len(letter_i)): # проходження по таблиці
                    letter_j = letter_i[j]
                    for letter_pair in pair: # проходження по pair
                        #k = 0
                        if letter_pair == letter_j: # зчитування координат кожної з букв в pair
                            arr = []
                            arr.append(i)
                            arr.append(j)
                            coordinates.append(arr)
                            arr = []
                            #print('coord: ', coordinates)
                            if ((k % 2) == 0):                               
                                flag = 1
                                k = 0
                            k += 1

                        if(flag):
                            #k = 1
                            flag = 0

                            #Якщо букви утворюють прямокутник:
                            if((coordinates[0][0] != coordinates[1][0]) & (coordinates[0][1] != coordinates[1][1])):
                                new_pair = ''
                                new_pair += table[coordinates[1][0]][coordinates[0][1]]
                                new_pair += table[coordinates[0][0]][coordinates[1][1]]
                                rezult += new_pair
                                coordinates = []
                                #print(rezult)

                            #Якщо букви одинакові:
                            elif((coordinates[0][0] == coordinates[1][0]) & (coordinates[0][1] == coordinates[1][1])):
                                new_pair = ''
                                new_pair += table[coordinates[0][0]][(coordinates[0][1] - 1) % len(table[coordinates[0][0]])]
                                new_pair += table[coordinates[1][0]][(coordinates[1][1] - 1) % len(table[coordinates[1][0]])]
                                rezult += new_pair
                                coordinates = []

                            #Якщо букви стоять в одному рядку моєї таблиці:
                            elif((coordinates[0][0] == coordinates[1][0]) & (coordinates[0][1] != coordinates[1][1])):
                                new_pair = ''
                                new_pair += table[coordinates[0][0]][(coordinates[0][1] - 1) % len(table[coordinates[0][0]])]
                                new_pair += table[coordinates[1][0]][(coordinates[1][1] - 1) % len(table[coordinates[1][0]])]
                                rezult += new_pair
                                coordinates = []

                            #Якщо букви стоять в одному стовпці моєї таблиці:
                            elif((coordinates[0][0] != coordinates[1][0]) & (coordinates[0][1] == coordinates[1][1])):
                                new_pair = ''
                                new_pair += table[(coordinates[0][0] - 1) % len(table)][coordinates[0][1]]
                                new_pair += table[(coordinates[1][0] - 1) % len(table)][coordinates[1][1]]
                                rezult += new_pair
                                coordinates = []

            pair = ''

    #print(rezult)
    output_file.write(rezult)
    output_file.close()
    input_file.close()

#table = fill_table()


#===========================MAIN============================

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")


print("\nDecrypting file...")

printCompleatedProgressBar()

decrypt_file(input_file, output_file)

print("Decrypting compleated!\n")

