import re

data_file = open("file_6.txt", "r")

classes = {}

for line in data_file.readlines():
    predmet = line.split()[0]
    class_time = 0

    for i in re.findall('\d+', line):
        class_time += int(i)
    predmety.update({predmet: class_time})

print(predmety)

data_file.close()
