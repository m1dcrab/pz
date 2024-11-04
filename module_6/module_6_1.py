class Animal:
    alive = True
    fed = False
    name = None
    def __init__(self,name):
        self.name = name
    def eat(self, food):
        if food.edible is True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не съел {food.name}")
            self.alive = False
class Mammal(Animal):
    pass
class Predator(Animal):
    pass

class Plant:
    def __init__(self,name):
        self.name = name
    edible = False
    name = None

class Flower(Plant):
    def __init__(self,name):
        super().__init__(name)
        self.edible = False
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)