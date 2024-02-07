
# Ваша задача создать следующие пустые классы
#     Vehicle     
#     Car     
#     Plane     
#     Boat     
#     RaceCar 
# Перечисленные класс должны находиться в следующей иерархии: 
# Класс Vehicle является базовым классом, от которого наследуются все остальные.
#-----------------------------------------------------------------------------------

class Vehicle():
    pass


class Car(Vehicle):
    pass


class Plane(Vehicle):
    pass


class Boat(Vehicle):
    pass


class RaceCar(Car):
    pass


# -------------код для проверки-------------------------
vehicle = Vehicle()
car = Car()
plane = Plane()
boat = Boat()
race_car = RaceCar()

assert isinstance(vehicle, Vehicle)
assert isinstance(car, Car)
assert isinstance(plane, Plane)
assert isinstance(boat, Boat)
assert isinstance(race_car, RaceCar)
assert vehicle.__dict__ == {}
assert car.__dict__ == {}

assert issubclass(Car, Vehicle), "Класс Car должен наследоваться от Venicle"
assert issubclass(
    Plane, Vehicle), "Класс Plane должен наследоваться от Venicle"
assert issubclass(Boat, Vehicle), "Класс Boat должен наследоваться от Venicle"
assert issubclass(
    RaceCar, Car), "Класс RaceCar должен наследоваться от Venicle"
assert issubclass(
    RaceCar, Vehicle), "Класс RaceCar должен наследоваться от Venicle"
print('Good')
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------



# Создайте базовый класс Vehicle, у которого есть:
#     конструктор __init__, принимающий название транспортного средства, его максимальную скорость и пробег. Их необходимо сохранить в атрибуты экземпляра name, max_speed и mileage соответственно
#     метод display_info , который печатает информацию в следующем виде:
#     Vehicle Name: {name}, Speed: {max_speed}, Mileage: {mileage}
# Затем создайте подкласс Bus , унаследованный от Vehicle. Оставьте его пустым
# bus_99 = Bus("Ikarus", 66, 124567)
# bus_99.display_info() #печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"
# 
# ---------------------------------------------------------------
    
class Vehicle():
    def __init__(self, name, max_speed, mileage) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')

class Bus(Vehicle):
    pass

bus_99 = Bus("Ikarus", 66, 124567)
bus_99.display_info() #печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"

# -------------код для проверки-------------------------
assert issubclass(Bus, Vehicle)
bus_99 = Bus("Ikarus", 66, 124567)
assert bus_99.name == 'Ikarus'
assert bus_99.max_speed == 66
assert bus_99.mileage == 124567
bus_99.display_info()

modelX = Vehicle('modelX', 240, 18)
assert modelX.__dict__ == {'max_speed': 240, 'mileage': 18, 'name': 'modelX'}
modelX.display_info()

audi = Bus('audi', 123, 43)
assert audi.__dict__ == {'max_speed': 123, 'mileage': 43, 'name': 'audi'}, 'Видимо забыли создать какой-то атрибут'
audi.display_info()
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Создайте базовый класс  Person, у которого есть:
#     конструктор __init__, который должен принимать на вход имя и записывать его в атрибут name
#  метод get_name, который возвращает атрибут name
# метод  is_employee, который возвращает  False
# Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:
#     метод  is_employee, который возвращает  True
# ---------------------------------------------------------------
 
     
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False

class    Employee(Person):
    def is_employee(self):
        return True

# -------------код для проверки-------------------------
assert issubclass(Employee, Person)

p = Person("just human")
assert p.name == 'just human'
assert p.get_name() == 'just human'
assert p.is_employee() is False

emp = Employee("Geek")
assert emp.name == 'Geek'
assert emp.get_name() == 'Geek'
assert emp.is_employee() is True
print('Good')
# ---------------------------------------------------------------

# ---------------------------------------------------------------


# Реализуйте следующую иерархию классов
# Напишите только определение классов, сами классы оставьте пустыми.
#  
# ---------------------------------------------------------------
class Shape():
    pass

class Polygon(Shape):
    pass
class Ellipse(Shape):
    pass

class Rectangle(Polygon):
    pass
class Triangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Circle(Ellipse):
    pass


# Ниже располагаются проверки

assert issubclass(Ellipse, Shape), "Класс Ellipse должен наследоваться от Shape"
assert issubclass(Polygon, Shape), "Класс Polygon должен наследоваться от Shape"

assert issubclass(Circle, Shape), "Класс Circle должен наследоваться от Shape"
assert issubclass(Circle, Ellipse), "Класс Circle должен наследоваться от Ellipse"
assert not issubclass(Circle, Polygon), "Класс Circle не должен наследоваться от Polygon"

assert issubclass(Triangle, Polygon), "Класс Triangle должен наследоваться от Polygon"
assert issubclass(Triangle, Shape), "Класс Triangle должен наследоваться от Shape"
assert not issubclass(Triangle, Ellipse), "Класс Triangle не должен наследоваться от Ellipse"

assert issubclass(Square, Rectangle), "Класс Square должен наследоваться от Rectangle"
assert issubclass(Square, Polygon), "Класс Square должен наследоваться от Polygon"
assert issubclass(Square, Shape), "Класс Square должен наследоваться от Shape"
assert not issubclass(Square, Ellipse), "Класс Square не должен наследоваться от Ellipse"
print('Good')
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Я создал для вас список shapes, которых хранит в себе экземпляры  различных фигур. Фигуры перемешаны, созданы в хаотичном порядке 
# Ваша задача найти и вывести 3 числа в разных строках:
#     на первой строке количество кружочков
#     на второй строке количество фигур, являющихся прямоугольниками
#     на последней строке количество фигур, являющихся многоугольниками.
# 
# ---------------------------------------------------------------

from collections import Counter


class Shape():
    pass

class Polygon(Shape):
    pass
class Ellipse(Shape):
    pass

class Rectangle(Polygon):
    pass
class Triangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Circle(Ellipse):
    pass

shapes = [
    Polygon(), Triangle(), Ellipse(), Polygon(), Triangle(), Ellipse(), Polygon(), Square(), Polygon(), Circle(),
    Shape(), Polygon(), Triangle(), Circle(), Ellipse(), Shape(), Circle(), Rectangle(), Circle(), Circle(),
    Square(), Square(), Circle(), Rectangle(), Rectangle(), Polygon(), Polygon(), Polygon(), Square(), Square(),
    Rectangle(), Square(), Rectangle(), Polygon(), Circle(), Triangle(), Rectangle(), Shape(), Rectangle(),
    Polygon(), Polygon(), Ellipse(), Square(), Circle(), Shape(), Polygon(), Ellipse(), Triangle(), Square(),
    Polygon(), Triangle(), Circle(), Rectangle(), Rectangle(), Ellipse(), Triangle(), Rectangle(), Polygon(),
    Shape(), Circle(), Rectangle(), Polygon(), Triangle(), Circle(), Polygon(), Rectangle(), Polygon(), Square(),
    Triangle(), Circle(), Ellipse(), Circle(), Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
    Triangle(), Polygon(), Square(), Polygon(), Circle(), Ellipse(), Polygon(), Shape(), Triangle(), Rectangle(),
    Circle(), Square(), Triangle(), Triangle(), Ellipse(), Square(), Circle(), Rectangle(), Ellipse(), Shape(),
    Triangle(), Ellipse(), Circle(), Shape(), Polygon(), Polygon(), Ellipse(), Rectangle(), Square(), Shape(),
    Circle(), Triangle(), Circle(), Circle(), Circle(), Triangle(), Ellipse(), Polygon(), Circle(), Ellipse(),
    Rectangle(), Circle(), Shape(), Polygon(), Polygon(), Triangle(), Rectangle(), Polygon(), Shape(), Circle(),
    Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
]

l1 = filter(lambda x: isinstance(x, Circle), shapes)
l2 = filter(lambda x: isinstance(x, Rectangle), shapes)
l3 = filter(lambda x: isinstance(x, Polygon), shapes)

print(len(tuple(l1)))
print(len(tuple(l2)))
print(len(tuple(l3)))
# -------------код для проверки-------------------------

# ---------------------------------------------------------------



# Давайте усовершенствуем наш класс MyList.
# У списков есть полезный метод .remove(value), который позволяет удалить значение value один раз из списка. Если value отсутствует в списке, происходит исключение ValueError.
# Ваша задача создать метод .remove_all(value), который будет удалять сразу все значения, которые равны value. Если value отсутствует в списке, ничего делать не нужно. Метод в конце своей работы должен вернуть None
# ---------------------------------------------------------------
class MyList(list):
    def remove_all(self, value):
        
        try:
            while True:
                self.remove(value)             
        
        except ValueError:
            pass


# тесты
s = MyList([1, 2, 3, 2, 1, 2])
assert s == [1, 2, 3, 2, 1, 2]
s.remove_all(2)
assert s == [1, 3, 1]
s.remove_all(1)
assert s == [3]
s.remove_all(5)
assert s == [3]
s.remove_all(3)
assert s == []

k = MyList([0]*20)
assert k == [0]*20
k.remove_all(7)
assert k == [0]*20
k.append(8)
k.append(0)
k.append(2)
k.remove_all(0)
assert k == [8, 2]
print('Good')
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Создайте класс NewInt, который унаследован от целого типа int, то есть мы будем унаследовать поведение целых чисел и значит экземплярам нашего класса будут поддерживать те же операции, что и целые числа.
# Дополнительно в классе NewInt нужно создать:
#     метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2), обозначающее сколько раз нужно продублировать данное число. Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
#     метод to_bin, который возвращает двоичное представление числа в качестве целого числа (может пригодиться функция bin или форматирование)
# ---------------------------------------------------------------
class NewInt(int):
    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):        
        return int(f'{self:b}')


# код проверки
c1 = NewInt(9)
assert isinstance(c1, NewInt)
assert issubclass(NewInt, int)
assert c1 + 9 == 18
assert c1 * 9 == 81


c2 = NewInt(31)
assert c2.repeat() == 3131
assert c2.repeat(4) == 31313131
assert NewInt(16).to_bin() == 10000
assert NewInt(14).to_bin() == 1110    

print('Good')
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Определите дочерние классы Cube и Power4 (возведение в 4-ую степень) от класса Square так, чтобы они переопределяли метод get_value() и возвращали результат.
# ---------------------------------------------------------------
class Square:
    def get_value(self, a):
        return a * a  
    
class Cube(Square):
    def get_value(self, a):
        return a**3  

class Power4(Square):
    def get_value(self, a):
        return a**4  

# код проверки
assert issubclass(Cube, Square)
assert issubclass(Power4, Square)

cube = Cube()
assert cube.get_value(2) == 8
assert cube.get_value(-17) == -4913

power4 = Power4()
assert power4.get_value(5) == 625
assert power4.get_value(25) == 390625

print('Good')
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Ниже в программе определены два класса Employee и SalesEmployee
# Ваша задача определить и устранить избыточность кода при помощи делегирования
# 
# ---------------------------------------------------------------
class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)        
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive


#тесты
jack = Employee('Jack', 5000, 1000)
assert jack.name == 'Jack'
assert jack.base_pay == 5000
assert jack.bonus == 1000
assert jack.get_pay() == 6000


john = SalesEmployee('John', 5000, 1000, 2000)
assert john.name == 'John'
assert john.base_pay == 5000
assert john.bonus == 1000
assert john.sales_incentive == 2000
assert john.get_pay() == 8000

print('Good')
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Фигуры
# Имеется реализация класса Rectangle, который описывает поведение прямоугольников. При помощи класса Rectangle можно:
#     создавать прямоугольники с указанием длины и ширины (метод __init__)
#     находить площадь прямоугольника (метод area)
#     находить периметр прямоугольника (метод perimeter)
#     Квадрат представляет собой частный случай прямоугольника, у которого все стороны равны.
# Ваша задача применить все полученные знания о наследовании и создать дочерний класс Square, который позволит:
#     создавать квадраты с указанием размера его стороны  (метод __init__)
#     находить площадь квадрата (метод area)
#     находить периметр квадрата (метод perimeter)
# Постарайтесь минимально дублировать код. Обязательно посмотрите решения других студентов курса после прохождения задания
# ---------------------------------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):           
        self.length = length
        self.width = length
    

# тесты  

rect_1 = Rectangle(3, 2)
assert rect_1.area() == 6
assert rect_1.perimeter() == 10

rect_2 = Rectangle(10, 5)
assert rect_2.area() == 50
assert rect_2.perimeter() == 30

sq_1 = Square(4)
assert sq_1.area() == 16
assert sq_1.perimeter() == 16

sq_2 = Square(10)
assert sq_2.area() == 100
assert sq_2.perimeter() == 40
print('Good')
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Создайте базовый класс  Person, у которого есть:
#     конструктор __init__, который должен принимать на вход имя и номер паспорта и записывать их в атрибуты name, passport
# #     метод display, который печатает на экран сообщение «<имя>: <паспорт>»;
# Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:
#     метод  __init__, который принимает именно в таком порядке четыре значения: имя, паспорт, зарплату и отдел. Их нужно сохранить в атрибуты  name, passport, salary,department. При этом создание атрибутов name, passportнеобходимо делегировать базовому классу Person
# a = Employee('Raul', 886012, 200000, "QA")   
# a.display() # печатает "Raul: 886012"
# ---------------------------------------------------------------

class Person:
    def __init__(self, name, passport) -> None:
        self.name = name
        self.passport = passport

    def display(self):
        print(f'{self.name}: {self.passport}')


class Employee(Person):
    def __init__(self, name, passport, salary, department) -> None:
        super().__init__(name, passport)
        self.salary = salary
        self.department = department



# тесты 

assert issubclass(Employee, Person)

emp = Person("just human", 123456)
emp.display()
assert emp.__dict__ == {'name': 'just human', 'passport': 123456}

emp2 = Employee("Geek2", 534432, 321321, 'Roga & Koputa')
emp2.display()
assert emp2.__dict__ == {'salary': 321321, 'department': 'Roga & Koputa',
                         'name': 'Geek2', 'passport': 534432}
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Создайте базовый класс Vehicle, у которого есть:
#     метод __init__, принимающий название транспортного средства, пробег и вместимость. Их необходимо сохранить в атрибуты экземпляра name, mileage и  capacity соответственно
#     метод fare , который возвращает стоимость проезда из расчета  capacity * 100:
    #  метод display , который печатает строку следующего вида:
#     Total <name> fare is: <метод fare>
# Затем создайте подкласс Bus , унаследованный от Vehicle. В нем необходимо:
#     переопределить метод __init__. Он должен принимать два значения: название транспортного средства и пробег. Необходимо делегировать создание атрибутов name, mileage и  capacityбазовому классу, в качестве аргумента передайте capacity  значение 50
#     переопределить метод fare . Он должен получить стоимость проезда у родительского класса и увеличить ее на 10%. 
# После создайте подкласс Taxi , унаследованный от Vehicle. В нем необходимо:
#     переопределить метод __init__. Он должен принимать два значения: название транспортного средства и пробег. Необходимо делегировать создание атрибутов name, mileage и  capacityбазовому классу, в качестве аргумента передайте capacity  значение 4
#     переопределить метод fare . Он должен получить стоимость проезда у родительского класса и увеличить ее на 35%. 
# ---------------------------------------------------------------
# Напишите определение классов Vehicle Bus и Taxi
class Vehicle:
    def __init__(self, name, mileage, capacity) -> None:
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    
    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')



class Bus(Vehicle):
    def __init__(self, name, mileage) -> None:
        super().__init__(name, mileage, capacity=50)

    def fare(self):
        return super().fare() * 1.1



class Taxi(Vehicle):
    def __init__(self, name, mileage) -> None:
        super().__init__(name, mileage, capacity=4)
        

    def fare(self):
        return super().fare() * 1.35

# Ниже располагается код для проверки



sc = Vehicle('Scooter', 100, 2)
sc.display()

merc = Bus("Mercedes", 120000)
merc.display()

polo = Taxi("Volkswagen Polo", 15000)
polo.display()

t = Taxi('x', 111)
assert t.__dict__ == {'name': 'x', 'mileage': 111, 'capacity': 4}
t.display()
b = Bus('t', 123)

assert b.__dict__ == {'name': 't', 'mileage': 123, 'capacity': 50}
b.display()
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# В этой задаче у нас будет один родительский класс Transport и три дочерних класса: Car, Boat, Plane.
# В классе Transport должны быть реализованы:
#     метод __init__, который создает атрибуты brand, max_speed и kind. Значения атрибутов brand, max_speed , kind поступают при вызове метода __init__. При этом значение kindне является обязательным и по умолчанию имеет значение None;
#     метод __str__, который будет возвращать строку формата: "Тип транспорта <kind> марки <brand> может развить скорость <максимальная скорость> км/ч".
# В классе Carдолжны быть реализованы:
#     метод __init__, создающий у экземпляра атрибуты brand, max_speed, mileage и приватный атрибут gasoline_residue. Все значения этих атрибутов передаются при вызове класса Car. Внутри инициализации делегируйте создание атрибутов brand, max_speed , kind родительскому классу Transport , при этом атрибуту kindпередайте значение "Car";
#     свойство-геттер gasoline, который будет возвращать строку: "Осталось бензина <gasoline_residue> л";
#     свойство-сеттер gasoline, которое должно принимать ТОЛЬКО целое число value, увеличивает уровень топлива gasoline_residue на переданное значение и затем вывести фразу 'Объем топлива увеличен на <value> л и составляет <gasoline_residue> л'. Если в значение value подается не целое число, вывести 'Ошибка заправки автомобиля'.
# В классе Boatдолжны быть реализованы:
#     метод __init__, принимающий три значения brand, max_speed, owners_name. Их нужно сохранить в соответствующие атрибуты. При этом внутри инициализации нужно делегировать создание атрибутов brand, max_speed , kind родительскому классу Transport , в атрибут kind при этом передайте значение "Boat";
#     метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет <owners_name>'.
# В классе Planeдолжны быть реализованы:
#     метод __init__, создающий у экземпляра атрибуты brand, max_speed, capacity. Внутри инициализации делегируйте создание атрибутов brand, max_speed , kind родительскому классу Transport , при этом атрибуту kind передайте значение "Plane";
#     метод __str__, который будет возвращать строку: 'Самолет марки <brand> вмещает в себя <capacity> людей'.
# ---------------------------------------------------------------
class Transport:
    def __init__(self, brand, max_speed, kind=None) -> None:
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self) -> str:
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"



class Car(Transport):
    def __init__(self, brand, max_speed,  mileage, gasoline_residue) -> None:
        super().__init__(brand, max_speed, kind=None)
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue
        self.kind = "Car"

    @property
    def gasoline(self):
        return f"Осталось бензина {self.__gasoline_residue} л"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')

class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name) -> None:
        super().__init__(brand, max_speed, kind=None)
        self.owners_name = owners_name
        self.kind = "Boat"

    def __str__(self) -> str:
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity) -> None:
        super().__init__(brand, max_speed, kind="Plane")
        self.capacity = capacity

    def __str__(self) -> str:
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'

# Ниже располагается код для проверки

p1 = Transport('Chuck', 50)
print(p1)
assert isinstance(p1, Transport)
assert p1.kind == None
assert p1.brand == 'Chuck'
assert p1.max_speed == 50
assert p1.__dict__ == {'kind': None, 'brand': 'Chuck', 'max_speed': 50}

c1 = Car('RRR', 50, 150, 999)
print(c1)

assert isinstance(c1, Car)
assert c1.kind == "Car"
assert c1.brand == 'RRR'
assert c1.max_speed == 50
assert c1.mileage == 150
assert c1.gasoline == 'Осталось бензина 999 л'
c1.gasoline = 100
assert c1.gasoline == 'Осталось бензина 1099 л'
assert c1.__dict__ == {'kind': 'Car', 'brand': 'RRR', 'max_speed': 50,
                       'mileage': 150, '_Car__gasoline_residue': 1099}

b1 = Boat('XXX', 1150, 'Arkasha')
print(b1)
assert isinstance(b1, Boat)
assert b1.kind == "Boat"
assert b1.brand == 'XXX'
assert b1.max_speed == 1150
assert b1.owners_name == 'Arkasha'

pla = Plane('www', 2150, 777)
print(pla)
assert isinstance(pla, Plane)
assert pla.kind == "Plane"
assert pla.brand == 'www'
assert pla.max_speed == 2150
assert pla.capacity == 777

transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic может вмещать в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Автомобиль успешно заправлен'
print(first_car.gasoline)  # Осталось бензина на 350 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# Давайте представим, что в 2020 году в Москве проводили опрос и выявили, к какому классу люди себя относят. По результатам опроса все люди разделились на сладкоежек, вегетарианцев и любителей мяса. Давайте напишем программу, которая поможет нам подвести итоги опроса. Для создания программы нужно:
# 1. Создать родительский класс Initialization, который состоит из:
#      метода инициализации, в который поступают аргументы: capacity - целое число, food - список из строковых названий еды. Если в значение capacity  передается не целое число, вывести надпись ‘Количество людей должно быть целым числом’ и не создавать для таких экземпляров атрибуты capacity и food.
# 2. Создать дочерний класс Vegetarian от класса Initialization, который состоит из: 
#     метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
# #     метода __str__, который возвращает строку формата "<capacity> людей предпочитают не есть мясо! Они предпочитают <food>"
# 3. Создать дочерний класс MeatEater от класса Initialization, который состоит из: 
#     метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
#     метода __str__, который возвращает строку формата "<capacity> мясоедов в Москве! Помимо мяса они едят еще и <food>"
# 4. Создать дочерний класс SweetTooth от класса Initialization, который состоит из: 
#     метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
    #  магического метода __str__, который возвращает строку формата ‘Сладкоежек в Москве <capacity>. Их самая любимая еда: <food>’; 
#     магического  метода __eq__, который будет позволять сравнивать экземпляры класса SweetTooth  с числами и другими нашими классами. Если сравнение происходит с целым числом и атрибут capacity с ним совпадает, то необходимо вернуть True, в противном случае - False. Если же сравнение идет с другим нашим классом(Vegetarian или MeatEater) и значения атрибутов capacity равны, то возвращается True, в противном случае - False. А если же сравнивается с другим типом данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’;
#     магического  метода __lt__. Если сравнение происходит с целым числом и количество сладкоежек (атрибут capacity) меньше, необходимо вернуть True, в противном случае - False. Если сравнение происходит с экземпляром одного из наших классов Vegetarian или MeatEater и сладкоежек меньше, то верните True, в противном случае верните False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’
#     магического  метода __gt__. Если сравнение происходит с целым числом и количество сладкоежек больше, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит с другим нашим классом Vegetarian или MeatEater и сладкоежек больше, то верните True, в противном случае - False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’
# ---------------------------------------------------------------

# Напишите определение классов Initialization Vegetarian MeatEater и SweetTooth
from functools import total_ordering

class Initialization:
    def __init__(self, capacity, food) -> None:
        if type(capacity) == int:
            self.capacity = capacity
            self.food = food
        else:
            print(f'Количество людей должно быть целым числом')


class Vegetarian(Initialization):
    def __init__(self, capacity, food) -> None:
        super().__init__(capacity, food)    

    def __str__(self) -> str:
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater (Initialization):
    def __init__(self, capacity, food) -> None:
        super().__init__(capacity, food)

    def __str__(self) -> str:
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"

@total_ordering
class SweetTooth(Initialization):
    def __init__(self, capacity, food) -> None:
        super().__init__(capacity, food)

    def __str__(self) -> str:
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            return other == self.capacity
        elif isinstance(other, (Vegetarian, MeatEater)):
            return other.capacity == self.capacity
        else:
            return(f'Невозможно сравнить количество сладкоежек с {other}')  
       

    def __gt__(self, other: object) -> bool:
        if isinstance(other, int):
            return other < self.capacity
        elif isinstance(other, (Vegetarian, MeatEater)):
            return other.capacity < self.capacity
        else:
            return(f'Невозможно сравнить количество сладкоежек с {other}')  
        

# Ниже располагается код для проверки

p1 = Initialization('Chuck', [])
assert isinstance(p1, Initialization)
assert not hasattr(p1, 'capacity'), 'Не нужно создавать атрибут "capacity", если передается не целое число'
assert not hasattr(p1, 'food'), 'Не нужно создавать атрибут "food", если передается не целое число'

c1 = Vegetarian(100, [1, 2, 3])
print(c1)
assert isinstance(c1, Vegetarian)
assert c1.capacity == 100
assert c1.food == [1, 2, 3]

b1 = MeatEater(1000, ['Arkasha'])
print(b1)
assert isinstance(b1, MeatEater)
assert b1.capacity == 1000
assert b1.food == ['Arkasha']

pla = SweetTooth(444, [2150, 777])
print(pla)
assert isinstance(pla, SweetTooth)
assert pla.capacity == 444
assert pla.food == [2150, 777]
assert pla > 100
assert not pla < 80
assert not pla == 90
assert pla > c1
assert not pla < c1
assert not pla == c1
assert not pla > b1
assert pla < b1
assert not pla == b1

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(30000 == s_first)  # Количество сладкоежек из опрошенных людей совпадает с 30000
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100
# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------



# 
# 
# 
# ---------------------------------------------------------------

# ---------------------------------------------------------------

# ---------------------------------------------------------------

