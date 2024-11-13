def custom_write(file_name, strings):
    result = {}
    red_line = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        red_line = red_line + 1
        result[red_line,file.tell()] = i
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
