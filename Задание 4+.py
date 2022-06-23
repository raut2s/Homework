slovar = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

file_4_input = open("file_4.txt")
file_4_output = open("file_4_new.txt", "a", encoding="utf8")

for line in file_4_input.readlines():
    for slovo in slovar:
        if slovo == line.split()[0]:
            line = line.replace(line.split()[0], slovar.get(slovo))
            file_4_output.write(f"{line}")
            print(line)

file_4_input.close()
file_4_output.close()