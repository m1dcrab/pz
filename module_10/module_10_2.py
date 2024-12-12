import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.warriors = 100
    def run(self):
        print(f"{self.name}, на нас напали!")
        day_counter = 0
        while self.warriors - self.power >= 0:
            day_counter = day_counter + 1
            warriors_left = self.warriors = self.warriors - self.power
            print(f"{self.name} сражается {days(day_counter)}, осталось {warriors_left} воинов.")
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days(day_counter)}!')

def days(day):
    if day == 1:
        return f'{day} день'
    if day in(2,3,4):
        return f'{day} дня'
    else:
        return f'{day} дней'

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()