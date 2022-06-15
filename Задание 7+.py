from itertools import count
from math import factorial

def fact_gen():
    for i in count(1):
        yield factorial(i)

generation = fact_gen()
x = 0
for i in generation:
    if x < 20:
        print(i)
        x += 1
    else:
        break