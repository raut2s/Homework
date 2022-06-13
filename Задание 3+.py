print('Привет, ученик курса GeekBrains!')
def first_func(var_1, var_2, var_3):
    if (var_1 >= var_3 and var_2 > var_3) or (var_1 >= var_3 and var_2 > var_3) or (var_1 >= var_3 and var_2 >= var_3):
        sum_max = var_1 + var_2
    elif (var_1 >= var_2 and var_3 > var_2) or (var_1 > var_2 and var_3 >= var_2) or (var_1 >= var_2 and var_3 >= var_2):
        sum_max = var_1 + var_3
    elif (var_2 >= var_1 and var_3 > var_1) or (var_2 > var_1 and var_3 >= var_1) or (var_2 >= var_1 and var_3 >= var_1):
        sum_max = var_2 + var_3
    return sum_max

print(first_func(12, 18, 18))
