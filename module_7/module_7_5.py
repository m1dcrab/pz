import os
import time
directory = '.'

for root, dirs, files in os.walk(directory):

    for file in files:
        filepath = os.path.join(root,file)

        filetime = os.stat(filepath).st_mtime

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        filesize = os.stat(filepath).st_size

        parent_dir = os.path.dirname(filepath)

        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')