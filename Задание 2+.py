my_list = ['Привет, ученик курса GeekBrains!\n',
'С каждым разом задания на дом всё изощрённее!\n',
'И каждый раз есть дедлайн выполнения этого задания!\n',
'А дел появляется всё больше и больше!\n',
'И на домашнюю работу всё меньше времени!\n',
'Но вариантов нет!!!!!\n',
'Начал учиться, значит надо довести до конца!\n']
with open("file_2.txt", 'w') as file_obj:
    file_obj.writelines(my_list)
with open("file_2.txt") as file_obj:
    lines = 0
    for line in file_obj:
        words = 0
        lines += line.count("\n")
        words += line.count(" ")
        print(f"{words+1} слов в строке")
    print(f"В файле насчитывается {lines} строк")