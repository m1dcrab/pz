from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda f, s: True if f == s else False, first, second)))

#Замыкание:
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        for i in data_set:
            file.write(str(i)+'\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
class MysticBall:
    words = None
    def __init__(self,*words):
        self.words = words
    def __call__(self,*words):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())