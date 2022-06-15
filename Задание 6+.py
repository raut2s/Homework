from itertools import count
from itertools import cycle

print('Привет, ученик курса GeekBrains!')
print('Давай я попробую сделать домашнюю работу, а ты мне в этом поможешь!')
numbers_start = int(input(
    'Введи, пожалуйста число, начиная с которого мы начнем генерировать целые числа:'))
numbers_stop = int(input('Введи, пожалуйста число, при достижении которого мы закончим генерировать новые целые числа:'))

def my_count(numbers_start, numbers_stop):
    for i in count(numbers_start):
        if i > numbers_stop:
            break
        else:
            print(i)
generation1 = my_count(numbers_start, numbers_stop)

print('Этот print я вывел для того, чтобы разделить ответы на задания!!!')

my_list = [123, 'python', True, False, 1, 2]

x = 0
for i in cycle(my_list):
    if x >= 15:
        break
    else:
        print(i)
        x += 1

