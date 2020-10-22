from collections import defaultdict
import time

alphabet = ' абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
#table = defaultdict(list)


def get_key(d, value):  # в мене значення ключа це список, тож тут дызнаюсь ключ по заданому значенню
    for k, v in d.items():
        for i in v:
            if i == value:
                return k


def fill_table():   # заповнення словника з заданого файла
    table = defaultdict(list)
    i = 1
    str = ''
    file_name = "table.txt"
    flag = 1
    myfile = open(file_name, "r", encoding='utf-8')

    for line in myfile:
        for letter in line:
            if(alphabet.find(letter.strip()) != -1):
            #if letter.strip() in alphabet:
                if((letter.strip() == "") & flag):
                    key_letter = " "
                    flag = 0
                else:
                    key_letter = letter.strip()
            else:
                if(i % 2 != 0):
                    str += letter.strip()
                    i += 1
                else:
                    str += letter.strip()
                    i = 1
                    table[key_letter].append(str)
                    str = ''

    return table



#fill_table()
#print(fill_table())

