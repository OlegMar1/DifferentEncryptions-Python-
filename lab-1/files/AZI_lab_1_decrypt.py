from progress_bar import printCompleatedProgressBar

alpha = ' абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
beta = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

def decrypt_file(key, path_in, path_out):

    input_file = open(path_in,"r", encoding='utf-8')   
    output_file = open(path_out, "w", encoding='utf-8')
    rezult = ''
    temp = ''

    for line in input_file:
        for letter in line:
            l = letter.strip()
            if l in alpha:
                temp = alpha[(alpha.index(l) - key) % len(alpha)]

            elif l in beta:
                temp = beta[(beta.index(l) - key) % len(beta)]

            #else:
            #    print("You have made a mistake in text!")
            rezult += temp;

    #print('Result: "' + rezult + '"')

    output_file.write(rezult)
    output_file.close()
    input_file.close()


input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")
key = int(input("Enter a key value: "))


print("\nDecrypting file...")

printCompleatedProgressBar()
decrypt_file(key, input_file, output_file)

print("Decrypting compleated!\n")



