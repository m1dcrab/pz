import threading
import time

thread_list = []

def start_thread(*args):
    thread = threading.Thread(target=write_words, args=args)
    thread.start()
    thread_list.append(thread)

def join_all_threads():
    for i in thread_list:
        i.join()

def write_words(word_count, file_name):
    file = open(file_name,'w',encoding='utf-8')
    for i in range(0,word_count+1):
        file.write(f"Какое-то слово №{i}\n")
        time.sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")

time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
print(time_end-time_start)
time_start = time.time()

start_thread(10, 'example5.txt')
start_thread(30, 'example6.txt')
start_thread(200, 'example7.txt')
start_thread(100, 'example8.txt')
join_all_threads()

time_end = time.time()
print(time_end-time_start)


