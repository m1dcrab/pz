import queue
import time
import random
import threading


class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randrange(3,10))


class Cafe:
    def __init__(self,*tables):
        self.queue = queue.Queue()
        self.tables = tables

    def get_empty_table(self):
        for t in range(0, len(self.tables)):
            if self.tables[t].guest is None:
                return t
        return None

    def guest_arrival(self,*guests):
        for g in guests:
            empty_table = self.get_empty_table()
            if empty_table is not None:
                self.tables[empty_table].guest = g
                g.start()
                print(f"{g.name} сел(-а) за стол номер {self.tables[empty_table].number}")
            else:
                self.queue.put(g)
                print(f"{g.name} в очереди")
    def is_empty(self):
        if not self.queue.empty():
            return False
        for t in self.tables:
            if t.guest is not None:
                return False
        return True
    def discuss_guests(self):
        while not self.is_empty():
            for t in range(0,len(self.tables)):
                if (self.tables[t].guest is not None) and (not self.tables[t].guest.is_alive()):
                    print(f"{self.tables[t].guest.name} покушал(-а) и ушёл(ушла)")
                    self.tables[t].guest = None
                    print(f"Стол номер {self.tables[t].number} свободен")
            empty_table_index = self.get_empty_table()
            if not (self.queue.empty()) and (empty_table_index is not None):
                self.tables[empty_table_index].guest = self.queue.get()
                self.tables[empty_table_index].guest.start()
                print(f"{self.tables[empty_table_index].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[empty_table_index].number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
