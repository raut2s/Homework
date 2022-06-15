print('Привет, ученик курса GeekBrains!')
print('Давай сыграем ещё в одну игру!')
print('Ты напишешь список чисел, а я выведу те элементы списка, значения которых больше предыдущего элемента!')
list1 = []
numbers = input('Придумал числа? Вводи их:').split()
for i in range(1, len(numbers)):
    if int(numbers[i]) > int(numbers[i - 1]):
        list1.append(int(numbers[i]))
print('Список таких чисел будет -', list1)