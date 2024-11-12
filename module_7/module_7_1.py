class Product:
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = float(weight)
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    __file_name = 'products.txt'
    file = open(__file_name, 'a')
    file.close()

    def get_products(self):
        file = open(self.__file_name,'r')
        return file.read()

    def add(self, *products):
        for i in products:
            file = open(self.__file_name, 'r')
            if str(i) in self.get_products():
                print(f'Продукт "{i}" уже есть в магазине')
                file.close()
            else:
                file = open(self.__file_name, 'a')
                file.write(str(i)+'\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


