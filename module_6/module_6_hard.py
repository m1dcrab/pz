import math

class Figure:
    sides_count = 0
    def __init__(self,color,sides):
        self.__sides = []
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            for i in range(0,self.sides_count):
                self.__sides.append(1)

        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = (0,0,0)
        self.filled = False

# методы для цвета
    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if 255 >= (r or g or b) >= 0:
            return True

    def set_color(self,r,g,b):
        if self.__is_valid_color(r, g, b):
            self.__color = r,g,b


# методы для сторон
    def __is_valid_sides(self,new_sides_check):
        for i in new_sides_check:
            if i > 0 and len(new_sides_check) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides

# метод для вычисления периметра фигуры
    def __len__(self):
        return sum(self.__sides)


# круг
class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __init__(self, color, *circle_side):
        super().__init__(color, list(circle_side))
        self.__radius = self.get_sides()[0] / 2 * math.pi

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / 2 * math.pi

    def get_square(self):
        return math.pi * (self.__radius ** 2)

# треугольник
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *triangle_sides):
        super().__init__(color, list(triangle_sides))
        
    def get_square(self):
        p = self.__len__()/2
        return math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))

# куб
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *cube_side):
        sides_list = []
        if len(cube_side) == 1:
            for i in range(0, self.sides_count):
                sides_list.append(*cube_side)
        else:
            for i in range(0, self.sides_count):
                sides_list.append(1)
        super().__init__(color, sides_list)

    def set_sides(self, *side):
        if len(side) == 1:
            sides_list = []
            for i in range(0, self.sides_count):
                sides_list.append(*side)
            super().set_sides(*sides_list)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
triangle1 = Triangle((212,122,122),5,1,6)
cube1 = Cube((222, 35, 130), 5)

circle2 = Circle((300, 200, 100), 10,2)
triangle2 = Triangle((212,122,122),5,6,1,2)
cube2 = Cube((222, 35, 130), 6,2)
print('проверка правильно созданных объектов:')
print(circle1.get_sides())
print(triangle1.get_sides())
print(cube1.get_sides())
print(circle1.get_color())
print('проверка неправильно созданных объектов:')
print(circle2.get_sides())
print(triangle2.get_sides())
print(cube2.get_sides())
print(circle2.get_color())

print('Проверка на изменение цветов:')
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

print('Проверка на изменение сторон: \nне изменится:')
circle1.set_sides(13,13)
print(circle1.get_sides())
triangle1.set_sides(14)
print(triangle1.get_sides())
cube1.set_sides(5, 3, 12, 4, 5, 12, 4, 5, 12, 4, 5, 12)
print(cube1.get_sides())

print('изменится:')
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
triangle1.set_sides(14,12,21)
print(triangle1.get_sides())
cube1.set_sides(6)
print(cube1.get_sides())

print('Проверка периметра:')
print(len(circle1))
print(len(cube1))

print('Проверка площади круга:')
print(circle1.get_square())

print('Проверка площади треугольника:')
print(triangle1.get_square())

print('Проверка объёма куба:')
print(cube1.get_volume())
