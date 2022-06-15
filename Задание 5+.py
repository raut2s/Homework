print('Привет, ученик курса GeekBrains!')
list1 = [i for i in range(100, 1001) if i % 2 == 0]
print(list1)
from functools import reduce
def my_func(i1, i2):
    return i1 * i2
print(reduce(my_func, list1))
