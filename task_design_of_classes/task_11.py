# Класс Selfie 🌶️
# 
# Реализуйте класс Selfie, экземпляры которого запоминают свои предыдущие состояния и умеют восстанавливаться до тех состояний, в которых они были раньше. Под состоянием объекта понимается определенный набор атрибутов и соответствующих значений. Во время жизни экземпляр класса Selfie может различными способами изменять свое состояние, например, получать новые атрибуты или изменять значения имеющихся:

# obj = Selfie()

# obj.x = 1
# obj.y = 2

# Для фиксации текущего состояния экземпляра класса Selfie должен использоваться метод save_state(): 

# obj.save_state()              # фиксируем состояние: x=1, y=2
# obj.x = 0                     # изменяем состояние
# obj.y = 0                     # изменяем состояние

# Зафиксированные состояния экземпляра класса Selfie должны индексироваться: первое зафиксированное состояние должно иметь индекс 0, второе — 1, третье — 2, и так далее. По этим же индексам должна быть возможность возвращаться к необходимым состояниям:

# print(obj.x)                  # 0
# print(obj.y)                  # 0
# obj = obj.recover_state(0)    # возвращаемся к первому состоянию
# print(obj.x)                  # 1
# print(obj.y)                  # 2

# Обратите внимание, что при возвращении к одному из предыдущих состояний с помощью метода recover_state() должен возвращаться новый экземпляр класса Selfie, имеющий необходимое состояние. Если в метод recover_state() передан индекс, по которому экземпляр класса Selfie не имеет состояния, должен быть возвращен текущий экземпляр:

# obj = obj.recover_state(7)
# print(obj.x)                  # 1
# print(obj.y)                  # 2

# Каждый экземпляр класса Selfie должен знать, сколько состояний он зафиксировал:

# obj = Selfie()

# print(obj.n_states())         # 0
# obj.x = 0
# obj.save_state()
# obj.x = 1
# obj.save_state()
# obj.x = 2
# obj.save_state()
# print(obj.n_states())         # 3
# ------------------------------------------
import copy
from typing import TypeVar



Self = TypeVar("Self", bound="Selfie")

class Selfie:
    """
    класс Selfie, экземпляры которого запоминают свои предыдущие состояния и умеют восстанавливаться до тех состояний, в которых они были раньше. Под состоянием объекта понимается определенный набор атрибутов и соответствующих значений. 
    """
    
    def __init__(self) -> None:
        self.save_object = []

    
    def save_state(self) -> None:
        """Для фиксации текущего состояния экземпляра класса Selfie"""       
        new_instance = copy.deepcopy(self)
        self.save_object.append(new_instance)
        
    
    def recover_state(self, index: int) -> Self:
        """метод для возвращении к одному из предыдущих состояний"""               
        if self.save_object and abs(index) <= len(self.save_object) - 1:
            return self.save_object[index] 
        return self


    def n_states(self) -> int:
        """узнать количество зафиксированных состояний для экземпляра"""        
        return len(self.save_object)

# ==========альтернативное решение=======================
# import pickle
# class Selfie:
#     def __init__(self): self._states = []
#     def save_state(self): self._states.append(pickle.dumps(self))
#     def recover_state(self, n=0):
#         try: return pickle.loads(self._states[n])
#         except: return self
#     def n_states(self): return len(self._states)

# -----------тесты-------------------------------
print('------1 -------')
obj = Selfie()

obj.x = 1
obj.y = 2

print(obj.x)
print(obj.y)

obj.save_state()
obj.x = 0
obj.y = 0

print(obj.x)
print(obj.y)
obj = obj.recover_state(0)
print(obj.x)
print(obj.y)


print('------2 -------')
obj = Selfie()

print(obj.n_states())
obj.x = 0
obj.save_state()
obj.x = 1
obj.save_state()
obj.x = 2
obj.save_state()
print(obj.n_states())


print('------ 3-------')
from string import ascii_lowercase

obj = Selfie()
for char in ascii_lowercase:
    obj.__dict__[char] = ord(char)

print(*(obj.__dict__[char] for char in ascii_lowercase))
obj.save_state()

for char in ascii_lowercase:
    obj.__dict__[char] = ord(char) + 100

print(*(obj.__dict__[char] for char in ascii_lowercase))
obj = obj.recover_state(0)

print(*(obj.__dict__[char] for char in ascii_lowercase))


print('------ 4-------')
def sum_a_b(a, b):
    return a + b


def sub_a_b(a, b):
    return a - b


def mul_a_d(a, b):
    return a * b


def truediv_a_b(a, b):
    return a / b


obj = Selfie()
obj.sum_a_b = sum_a_b
print(obj.sum_a_b(1, 2))
obj.save_state()

obj.sub_a_b = sub_a_b
print(obj.sub_a_b(1, 2))
obj.save_state()

obj.mul_a_d = mul_a_d
print(obj.mul_a_d(1, 2))
obj.save_state()

obj.truediv_a_b = truediv_a_b
print(obj.truediv_a_b(1, 2))
obj.save_state()

print(obj.n_states())
obj = obj.recover_state(1)

print(obj.n_states())


print('------ 5-------')
obj = Selfie()

obj.x = 1
obj.y = 2

print(obj.x)
print(obj.y)

obj.x = 100
obj.y = 100

obj.save_state()
print(obj.x)
print(obj.y)

obj = obj.recover_state(7)
print(obj.x)
print(obj.y)