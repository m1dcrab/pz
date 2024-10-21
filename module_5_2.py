from random import random, randrange
class House:
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
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('Рандом', randrange(1,12))
'''
h1.go_to(5)
h2.go_to(10)
h3.go_to(randrange(-2,12))
'''
# __str__
print(h1)
print(h2)
print(h3)

# __len__
print(len(h1))
print(len(h2))
print(len(h3))
