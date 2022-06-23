my_list = []
while True:
    line = input("Введите какой-нибудь текст:")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line
        my_list.append(newline)

out_f = open("file_1.txt", "w")
out_f.writelines(my_list)
out_f.close()