# Класс SequenceZip
# 
# Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является последовательностью. Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи. Объединение должно происходить аналогично тому, как это делает функция zip().
# При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.
# Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
# Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.

# Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
# Примечание 2. Экземпляр класса SequenceZip не должен зависеть от последовательностей, на основе которых он был создан. Другими словами, если исходные последовательности изменятся, то экземпляр класса SequenceZip измениться  не должен.
# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.

from typing import Iterable, Iterator, Any
import copy

class SequenceZip:    
    def __init__(self, *args: Iterable) -> None:
        args = copy.deepcopy(args)        
        self.iterator_sequence = zip(*args)
        
    def __iter__(self) -> Iterator:
        return copy.deepcopy(self.iterator_sequence)
    
    def __len__(self) -> int:
        return sum(1 for _ in copy.deepcopy(self.iterator_sequence))
    
    def __getitem__(self, item: int) -> Any:       
        for index, element_sequence in enumerate(copy.deepcopy(self.iterator_sequence)):           
            if item == index:
                return element_sequence    
    
    def __next__(self) -> Any:           
        return next(self.iterator_sequence)


# --------------тесты -------------
print("----1----")
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))

print("----2----")
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])


print("----3----")
print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

print("----5----")
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])