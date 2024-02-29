
# Функция anything()
#
# Реализуйте функцию anything(), которая возвращает такой объект, результат сравнения с которым c помощью операторов ==, !=, >, <, >= и <= всегда равен True.
# --------------------------------------
import re
import math


class Anything:
    def __eq__(self, __o: object) -> bool:
        return True

    __ne__ = __lt__ = __gt__ = \
        __le__ = __ge__ = __eq__


def anything():
    return Anything()


# ----тест -----------

print(anything() != [])
print(anything() < 'World')
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)
# --------------------------------------

# --------------------------------------
