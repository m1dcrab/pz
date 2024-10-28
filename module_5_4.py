# метод для определения принадлежности к типам int и house переменных number_of_floors и other
def typeCheck(floors):
    if isinstance(floors, int) or isinstance(floors, House):
        return True
class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        print(f'{self.name}:')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1,new_floor+1):
                print(floor)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # операторы сравнения
    def __eq__(self, other):
        if typeCheck(self.number_of_floors) and typeCheck(other):
            return self.number_of_floors == other
    def __lt__(self,other):
        if typeCheck(self.number_of_floors) and typeCheck(other):
            return self.number_of_floors < other
    def __le__(self, other):
        if typeCheck(self.number_of_floors) and typeCheck(other):
            return self.number_of_floors <= other
    def __gt__(self, other):
        if typeCheck(self.number_of_floors) and typeCheck(other):
            return self.number_of_floors > other
    def __ge__(self, other):
        if typeCheck(self.number_of_floors) and typeCheck(other):
            return self.number_of_floors >= other
    def __ne__(self, other):
        if typeCheck(self.number_of_floors) and typeCheck(other):
            return self.number_of_floors != other

    # арифметические операторы
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self
    def __iadd__(self, value):
        self.__add__(value)
        return self
    def __radd__(self, value):
        self.__add__(value)
        return self

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

