# Функция roundrobin()
# 
# Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.
# Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых объектов: сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее; после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.
# Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

from typing import Iterable, Iterator, Any
from itertools import chain, zip_longest


class roundrobin:
    
    def __init__(self, *args: Iterable) -> None:
        self.iter_seq = chain(*zip_longest(*args, fillvalue='`j2PgAL#EH70'))
        
    def __iter__(self):
        return self
    
    def __next__(self) -> Any:       
        while True:            
            value = next(self.iter_seq)
            
            if value == '`j2PgAL#EH70':
                continue              
            else:
                return value


# ----------тесты-----------
print('-----1-----')
print(*roundrobin('abc', 'd', 'ef'))



print('-----2-----')
numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))



print('-----3-----')
print(list(roundrobin()))



print('-----4-----')
numbers = roundrobin(map(abs, range(-10, 10)))

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))



print('-----5-----')
numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))
    



