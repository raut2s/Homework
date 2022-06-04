print('Здравствуй ученик курса GeekBrains')
n = 0
number = int(input('Введите, пожалуйста, целое положительное число:'))
while number != 0:
    last_digit = number % 10
    if last_digit > n:
        n = last_digit
    number = number // 10
print(n)
