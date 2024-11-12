def custom_write(file_name, strings):
    result = {}
    red_string = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        red_string = red_string + 1
        result[red_string,file.tell()] = i
        file.write(i+'\n')
    file.close()
    return result

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)