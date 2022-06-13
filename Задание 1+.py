print('Привет, ученик курса GeekBrains!')
print('Мне нужно от тебя 2 целых числа')
arg_1 = int(input('Введи первое число:'))
arg_2 = int(input('Введи второе число:'))
while arg_2 == 0:
    print('На 0 делить нельзя!!!!!')
    arg_2 = int(input('Введи второе число ещё раз:'))
    continue
def quotient(arg_1, arg_2):
    num = arg_1 / arg_2
    return num

print('У меня получилось число -', quotient(arg_1, arg_2))