data_list = ['Иванов 18635.19', 'Петров 29469.82', 'Сидоров 11444.44', 'Кошкин 19999.99', 'Собакин 19200.68',
    'Уткин 22367.88', 'Гусев 45968.15', 'Щуркин 46999.75', 'Смирнов 53687.25', 'Рыбкин 17777.77']
file_open = open('file_3.txt', 'w')
data = [file_open.write(str(data_list[i]) + "\n") for i in range(len(data_list))]
file_open.close()

summa = 0
count = 0
persons = []

with open('file_3.txt', 'r') as file_open:
    for i in file_open:
        i = i.split(' ', 1)
        if float(i[1]) < 20000.00:
            persons.append(i[0])
        summa += float(i[1])
        count += 1
result_salary = summa / count
print(persons)
print(result_salary)


