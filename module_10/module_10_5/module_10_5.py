import multiprocessing
import time


def read_info(name):
    all_data =[]
    file = open(name,'r',encoding='utf-8')
    while file.readline() != '':
        all_data.append(file.readline())
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейный вызов
    time_start = time.time()
    for f in filenames:
        read_info(f)
    time_end = time.time()
    print(time_end - time_start)
    # Многопроцессный
    time_start = time.time()
    with multiprocessing.Pool(len(filenames)) as p:
        p.map(read_info,filenames)
    time_end = time.time()
    print(time_end-time_start)