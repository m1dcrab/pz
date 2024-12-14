import threading
import time
from random import randrange


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(0,100):
            random_value = randrange(50,500)
            self.balance += random_value
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {random_value}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(0, 100):
            random_value = randrange(50,500)
            print(f"запрос на {random_value}.")
            if random_value <= self.balance:
                self.balance -= random_value
                print(f"Снятие: {random_value}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')