# метод для определения принадлежности к типам int и house переменных number_of_floors и other
def typeCheck(floors):
    if isinstance(floors, int) or isinstance(floors, house):
        return True

class house:
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
        elif isinstance(value, house):
            self.number_of_floors += value.number_of_floors
        return self
    def __iadd__(self, value):
        self.__add__(value)
        return self
    def __radd__(self, value):
        self.__add__(value)
        return self

h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

#print(h1 != '12')
