print('Привет, ученик курса GeekBrains!')
print('Я создаю картотеку учеников и мне нужна информация о тебе!!!!!')
arg_1 = input('Введи своё имя:')
arg_2 = input('Введи свою фамилию:')
arg_3 = float(input('Введи год своего рождения:'))
arg_4 = input('Введи название города в котором ты живешь:')
arg_5 = input('Введи свой email:')
# тут решил использовать input(), потому что пользователь может ввести телефон с дефисами и тогда int не поймет его....
arg_6 = input('Введи номер своего телефона:')
def database(arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
    return(f"Имя - {arg_1}; Фамилия - {arg_2}; Год рождения - {int(arg_3)}; Город проживания - {arg_4}; Email - {arg_5}; Номер телефона - {arg_6}")
print('Итак, подведем итог:', database(arg_1, arg_2, arg_3, arg_4, arg_5, arg_6))
