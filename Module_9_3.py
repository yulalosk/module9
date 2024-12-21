import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
res = list(map(lambda x,y: x in y, first, second))
print(res)

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for str_ in data_set:
                file.write(str(str_) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это странный код', ['Несколько заданий в одном модуле.] [ХМ]'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
       return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

