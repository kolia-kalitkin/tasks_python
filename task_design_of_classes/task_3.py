
# # Классы ArithmeticProgression и GeometricProgression
#
# Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:
# progression = ArithmeticProgression(0, 1)
# for elem in progression:
#     if elem > 10:
#         break
#     print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
# Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.
# Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:
# progression = GeometricProgression(1, 2)
# for elem in progression:
#     if elem > 10:
#         break
#     print(elem, end=' ')    # 1 2 4 8
# Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Progression(ABC):
    first_member: int
    step: int
    flag: bool = field(default=None, init=False)

    def __iter__(self): return self

    @abstractmethod
    def __next__(self):
        pass


class ArithmeticProgression(Progression):
    """
    класс для генерации членов арифметической прогрессии. 
    """

    def __next__(self):
        result = self.first_member
        self.first_member += self.step
        return result


class GeometricProgression(Progression):
    """
    класс для генерации членов геометрической прогрессии
    """

    def __next__(self):
        result = self.first_member
        self.first_member *= self.step
        return result


# --------тесты ------------
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

print()
# ---------

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

print()
# ---------

progression = ArithmeticProgression(100, -10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

print()
