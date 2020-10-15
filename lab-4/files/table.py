#from collections import defaultdict
import time
alphabet = ' абвгдеєжзиіїйклмнопрстуфхцчшщьюя'


def get_key(d, value):  # в мене значення ключа це список, тож тут дызнаюсь ключ по заданому значенню
    for k, v in d.items():
        if v == value:
            return k


def fill_table():   # заповнення словника з заданого файла
    table = dict()
    #table = defaultdict(list)
    str = ''
    file_name = "table.txt"
    flag = 1
    myfile = open(file_name, "r")

    for line in myfile:
        for letter in line:
            if(letter == '\n'):
                continue
            #if(alphabet.find(letter.strip()) != -1):
            if letter.strip() in alphabet:
                if((letter.strip() == "") & flag):
                    key_letter = " "
                    flag = 0
                else:
                    key_letter = letter.strip()
                    
            else:
                str += letter.strip()
        table[key_letter] = str
        #table[key_letter].append(str)
        str = ''
    #print(table)
    #print(len(table))

    return table

#fill_table()



