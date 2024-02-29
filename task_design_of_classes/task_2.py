# Класс Vector
#
# Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector должен создаваться на основе собственных координат:

# a = Vector(1, 2, 3)
# b = Vector(3, 4, 5)
# c = Vector(5, 6, 7, 8)

# В качестве неформального строкового представления вектор должен иметь собственные координаты, заключенные в круглые скобки:

# print(a)                       # (1, 2, 3)
# print(b)                       # (3, 4, 5)
# print(c)                       # (5, 6, 7, 8)

# Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:

# print(a + b)                   # (4, 6, 8)
# print(a - b)                   # (-2, -2, -2)
# print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
# print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292

# а также операции сравнения на равенство и неравенство:

# print(a == Vector(1, 2, 3))    # True
# print(a == Vector(4, 5, 6))    # False

# При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено исключение ValueError с текстом:
# Векторы должны иметь равную длину


from math import sqrt


class Vector:
    """
    класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector должен создаваться на основе собственных координат
    """

    def __init__(self, *args: "Vector") -> None:
        self.args = args

    @staticmethod
    def if_different_len(obj1: "Vector", obj2: "Vector"):
        if len(obj1) != len(obj2):
            raise ValueError('Векторы должны иметь равную длину')

    def __len__(self) -> int:
        return len(self.args)

    def __str__(self):
        return ', '.join(str(i) for i in self.args)

    def __add__(self, other) -> "Vector":
        self.if_different_len(self, other)
        if isinstance(other, type(self)):    # type(self) или __class__
            return type(self)(tuple(self.args[i] + other.args[i] for i in range(len(self))))
        return NotImplemented

    def __sub__(self, other) -> "Vector":
        self.if_different_len(self, other)
        if isinstance(other, __class__):
            return type(self)(tuple(self.args[i] - other.args[i] for i in range(len(self))))
        return NotImplemented

    def __mul__(self, other) -> "Vector":
        self.if_different_len(self, other)
        if isinstance(other, __class__):    # type(self) или __class__
            return type(self)(sum(self.args[i] * other.args[i] for i in range(len(self))))
        return NotImplemented

    def norm(self) -> float:
        return sqrt(sum(i**2 for i in self.args))

    def __eq__(self, other) -> bool:
        self.if_different_len(self, other)
        if isinstance(other, type(self)):    # type(self) или __class__
            return self.args == other.args
        return NotImplemented


# ---------тесты --------------
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

vector3 = vector1 + vector2
vector4 = vector1 - vector2

print(type(vector3))
print(type(vector4))

# ----------
vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)
# ----------
vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 == Vector(1, 2, 3))
print(vector1 == Vector(4, 5, 6))
print(vector1 != vector2)
