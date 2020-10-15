import time
def fill_table():   # заповнення таблиці з заданого файла
    table = []
    arr = []
    file_name = "table.txt"
    #flag = 1
    myfile = open(file_name, "r")

    for line in myfile:
        for letter in line:
            l = letter.strip()
            if(letter == '\n'):
                continue
            if(l == ""):
                l = " "
            arr.append(l)

        table.append(arr)
        arr = []

    #print(table)

    return table

#fill_table()

