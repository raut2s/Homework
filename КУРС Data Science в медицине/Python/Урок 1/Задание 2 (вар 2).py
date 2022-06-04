print('Здравствуй ученик курса GeekBrains')
second = int(input('Введите, пожалуйста, время затраченное на выполнение домашней работы в секундах:'))
hour = second // 3600
second = second % 3600
minute = second // 60
second = second % 60
print(f'{hour}:{minute}:{second}')