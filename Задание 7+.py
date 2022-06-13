print('Здравствуй ученик курса GeekBrains')
word = input('Введите слово из маленьких латинских букв:')
def int_func(word):
    func1 = word.title()
    return func1
words = input(
    'Введите несколько слов из маленьких латинских букв, разделённых пробелом:')
print(int_func(words))