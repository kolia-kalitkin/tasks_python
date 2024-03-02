from typing import Any


class FieldTracker:
    def __init__(self) -> None:
        self.dict_attr = {name_attr: [value_attr] for name_attr, value_attr in self.__dict__.items()}     
        

    def __setattr__(self, name_attr: str, value_attr: Any) -> None:        
        if 'dict_attr' in self.__dict__:            
            self.dict_attr[name_attr].append(value_attr)     # добавляем измененное значение     
        self.__dict__[name_attr] = value_attr

                
    def base(self, name_attr: str) -> int:
        """метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута, либо исходное (указанное при определении) значение этого атрибута, если оно было изменено"""
        if len(self.dict_attr[name_attr]) > 1:
            return self.dict_attr[name_attr][0]     # исходное (указанное при определении)
        return getattr(self, name_attr, None)       # текущее значение атрибута

    
    def has_changed(self, name_attr: str) -> bool:
        """метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого атрибута было изменено хотя бы раз, или False в противном случае"""       
        return len(self.dict_attr[name_attr]) > 1

    
    def changed(self) -> dict:
        """метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои значения, а значениями — их исходные значени"""
        dict_attr_changed = {}
        for name_attr, value_attr in self.dict_attr.items():
            if len(value_attr) > 1:
                dict_attr_changed.setdefault(name_attr, value_attr[0])

        return dict_attr_changed

    
    def save(self) -> None:
        """метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли свои значения, а их текущие значения считаются исходными"""
        for value_attr in self.dict_attr.values():
            old_value = value_attr[0]  # сохраняем начальное значение атрибута 
            value_attr.clear()
            value_attr.append(old_value)


# --------тест -----------
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())