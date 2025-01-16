class NewClass:
    atr1: float
    atr2: int = 12
    def met1(self):
        pass

def introspection_info(obj):

    #Тип объекта
    obj_type = obj.__name__

    #Атрибуты объекта
    obj_atr = []
    for elem in dir(obj):
        if not callable(getattr(obj,elem)):
            obj_atr.append(elem)

    #Методы объекта
    obj_meth = []
    for elem in dir(obj):
        if callable(getattr(obj,elem)):
            obj_meth.append(elem)
            
    #Модуль, к которому объект принадлежит
    obj_module = obj.__module__
    
    #Другие интересные свойства объекта, учитывая его тип
    obj_an = NewClass.__annotations__

    return {'type':obj_type, 'attributes':obj_atr, 'methods':obj_meth,'module': obj_module, 'annotations': obj_an, }

test = NewClass
number_info = introspection_info(test)
print(number_info)
