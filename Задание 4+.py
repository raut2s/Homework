from itertools import count

print('Привет, ученик курса GeekBrains!')
print('У меня есть спиисок чисел и сейчас я определю элементы списка, не имеющие повторений!')
my_list = [300, 2, 55, 789, 12, 123, 44, 1,
    1, 4, 10, 7, 2, 1, 44, 78, 99, 123, 55]
new_my_list = [i for i in my_list if my_list.count(i) < 2]
print(my_list)
print(new_my_list)