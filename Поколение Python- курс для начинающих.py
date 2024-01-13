import re
import random   # Подключите модуль
import random
from random import *
import math
num = int(input())
digit4 = (num % 10)
digit3 = (num % 100) // 10
digit2 = (num % 1000) // 100
digit1 = (num % 10000) // 1000
print('Цифра в позиции тысяч равна', digit1)
print('Цифра в позиции сотен равна', digit2)
print('Цифра в позиции десятков равна', digit3)
print('Цифра в позиции единиц равна', digit4)
print()


print('*****************')
print('*               *')
print('*               *')
print('*****************')


a, b = int(input()), int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a + b) * (a + b))
print('Сумма квадратов', a, 'и', b, 'равна', a * a + b * b)

#  ################

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(a**b+c**d)


#  ################
num = int(input())
digit3 = num
digit2 = num*10
digit1 = num*100

print(digit3 + (digit2 + digit3) + (digit1 + digit2 + digit3))


password1 = input()
password2 = input()

if password1 == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')


#####################
num = int(input())
n4 = num % 10
n3 = num % 100 // 10
n2 = num % 1000 // 100
n1 = num % 10000 // 1000


if (n1 + n4) == (n2 - n3):
    print('ДА')
else:
    print('НЕТ')

##########
age = int(input())
if age < 18:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')


##############
num1, num2, num3 = int(input()), int(input()), int(input())
if num2 - num1 == num3 - num2:
    print('YES')
else:
    print("NO")


################
num1, num2 = int(input()), int(input())
if num1 > num2:
    print(num2)
else:
    print(num1)


################
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())

if num1 / num2 >= 1:
    box1 = num2
else:
    box1 = num1


if num3 / num4 >= 1:
    box2 = num4
else:
    box2 = num3


if box1 / box2 >= 1:
    print(box2)
else:
    print(box1)


#######################
age = int(input())

if 0 <= age <= 13:
    print('детство')
else:
    if 13 < age <= 24:
        print('молодость')
    else:
        if 24 < age <= 59:
            print('зрелость')
        else:
            if age > 59:
                print('старость')

################
num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0
if num1 > 0:
    counter = counter + num1

if num2 > 0:
    counter = counter + num2

if num3 > 0:
    counter = counter + num3

print(counter)


##################
x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')


##################
x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

##################
x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

###############
x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')


# **********


num = int(input())
if (1000 <= num <= 9999) and ((num % 7 == 0) or (num % 17 == 0)):
    print('YES')
else:
    print('NO')

###################
a, b, c = int(input()), int(input()), int(input())
if (a + b > c) and (a + c > b) and (b + c > a):
    print('YES')
else:
    print('NO')

#################
year = int(input())
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('YES')
else:
    print('NO')


# ход ладья]
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 == x2) or (y1 == y2):
    print('YES')
else:
    print('NO')


# ************ход короля]

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (-1 <= (x2 - x1) <= 1) and (-1 <= (y2 - y1) <= 1):
    print('YES')
else:
    print('NO')


##############
n, k = int(input()), int(input())
if n < k:
    print('YES')
elif n > k:
    print('NO')
elif n == k:
    print("Don't know")


# стороны треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c or a == c != b or b == c != a:
    print('Равнобедренный')
else:
    print('Разносторонний')

# среднее число
a, b, c = int(input()), int(input()), int(input())
if a < b < c or c < b < a:
    print(b)
elif b < a < c or c < a < b:
    print(a)
elif b < c < a or a < c < b:
    print(c)

# количество дней
month = int(input())
if month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:
    print(28)
else:
    print(31)

# церемония взвешивания
weight = int(input())
if 0 < weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')

# Самописный калькулятор 🌶️
n, k = int(input()), int(input())
stroka = input()

if stroka == '+':
    print(n + k)
elif stroka == '-':
    print(n - k)
elif stroka == '*':
    print(n * k)
elif stroka == '/' and k == 0:
    print('На ноль делить нельзя!')
elif stroka == '/' and k != 0:
    print(n / k)
else:
    print('Неверная операция')


# Цветовой микшер 🌶️
# 125 666
st1, st2 = input(), input()

if st1 == st2 == 'красный':
    print('красный')
elif (st1 == 'красный' and st2 == 'синий') or (st2 == 'красный' and st1 == 'синий'):
    print('фиолетовый')
elif (st1 == 'красный' and st2 == 'желтый') or (st2 == 'красный' and st1 == 'желтый'):
    print('оранжевый')
elif (st1 == 'синий' and st2 == 'желтый') or (st2 == 'синий' and st1 == 'желтый'):
    print('зеленый')
elif st1 == st2 == 'синий':
    print('синий')
elif st1 == st2 == 'желтый':
    print('желтый')
elif st1 == st2 == 'фиолетовый':
    print('фиолетовый')
elif st1 == st2 == 'оранжевый':
    print('оранжевый')
else:
    print('ошибка цвета')


# Цвета колеса рулетки 🌶️
# Верно решили 123 264

el = int(input())

if el < 0 or el > 36:
    print('ошибка ввода')
elif el == 0:  # zero
    print('зеленый')
elif el % 2 != 0 and 1 <= el <= 10:  # неч КРАСНЫЙ
    print('красный')
elif el % 2 == 0 and 11 <= el <= 18:  # четн КРАСНЫЙ
    print('красный')
elif el % 2 != 0 and 19 <= el <= 28:  # неч КРАСНЫЙ
    print('красный')
elif el % 2 == 0 and 29 <= el <= 36:  # четн КРАСНЫЙ
    print('красный')

else:
    print('черный')


# Пересечение отрезков 🌶️🌶️
# Верно решили 111 136 учащихся


# ##################
# ##################
# #################

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 < a2:              # 1
    if a2 < b1:
        print(a2, b1)
    elif a2 == b1:
        print(a2)
    elif b1 < a2:
        print('пустое множество')
    elif b1 == b2:
        print(a2, b2)
    elif b2 < b1:
        print(a2, b2)

elif a2 < a1:               # 2
    if a1 < b2:
        print(a1, b2)
    elif a1 == b2:
        print(a1)
    elif b2 < a1:
        print('пустое множество')
    elif b1 == b2:
        print(a1, b1)
    elif b1 < b2:
        print(a1, b1)

elif a1 == a2:  # 3
    if b1 < b2:
        print(a1, b1)
    elif b1 > b2:
        print(a1, b2)
    elif b1 == b2:
        print(a1, b1)


###### #########
###### ############### ############### #########
###### #########

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 > a2:
    a1, b1, a2, b2 = a2, b2, a1, b1

if b1 < a2:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b1 <= b2:
    print(a2, b1)
else:
    print(a2, b2)


#  Начало столетия
#  Верно решили 104 711 учащихся
#  Из всех попыток 71% верных

year = int(input())
if year % 10 == 0 and year % 100 // 10 == 0:
    print('YES')
else:
    print('NO')


# Шахматная доска
# Верно решил 104 421 учащийся
#
#
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if ((x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0) or ((x1 + y1) % 2 == 1 and (x2 + y2) % 2 == 1):
    print('YES')
else:
    print('NO')


# Girls only
# dерно решили 104 379
#
age = int(input())
gender = input()
if 10 <= age <= 15 and gender == 'f':
    print('YES')
else:
    print('NO')


#  Римские цифры
#  Верно решили 103 927
#
num = int(input())
if 1 <= num <= 10:
    if num == 1:
        print('I')
    elif num == 2:
        print('II')
    elif num == 3:
        print('III')
    elif num == 4:
        print('IV')
    elif num == 5:
        print('V')
    elif num == 6:
        print('VI')
    elif num == 7:
        print('VII')
    elif num == 8:
        print('VIII')
    elif num == 9:
        print('IX')
    elif num == 10:
        print('X')
else:
    print('ошибка')


# YES or NO вот в чем вопрос
# Верно решили 103 893
#
#
n = int(input())
if (n % 2 == 1) or (n % 2 == 0 and 6 <= n <= 20):
    print('YES')
elif (n % 2 == 0 and 2 <= n <= 5) or (n % 2 == 0 and n > 20):
    print('NO')


# Ход слона 🌶️
# Верно решили 101 509 учащихся
#

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')

# Ход коня
# Верно решили 99 743 учащихся
#
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print('YES')
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print('YES')
else:
    print('NO')


# Ход ферзя
# Верно решили 98 768 учащихся
#
# добавить в условие перебор ходов ладьи слона и короля


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((x1 == x2) or (y1 == y2)) or ((-1 <= (x2 - x1) <= 1) and (-1 <= (y2 - y1) <= 1)) or ((x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2)):
    print('YES')
else:
    print('NO')

# Площадь треугольника
# 121 465
#
a, b = float(input()), float(input())
el = a * b / 2
print(el)


# Две старушки
# Верно решили 120 755
#
#
el, v1, v2 = float(input()), float(input()), float(input())
t = el / (v1 + v2)
print(t)

# Обратное число
# Верно решили 119 166
#
#
num = float(input())
if num != 0:
    num = 1 / num
    print(num)
else:
    print('Обратного числа не существует')


# 451 градус по Фаренгейту
# Верно решили 119 667
#
#
t_far = float(input())
c = 5 / 9 * (t_far - 32)
print(c)

# Dog age
# Верно решили 118 472
#
#
n = int(input())
if 0 <= n <= 2:
    print(n * 10.5)
elif n > 2:
    print(2 * 10.5 + (n - 2) * 4)


# Первая цифра после точки
# 117 383
#
#
r = float(input())
print((int(r * 10)) % 10)


# Дробная часть
# 117 494
#
#
r = float(input())
print(r - int(r))

# n = float(input())
# print(n % 1)

# Наибольшее и наименьшее
# Верно решили 116 654
#

a, b, c, d, e = int(input()), int(input()), int(
    input()), int(input()), int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))


# Сортировка трёх 🌶️
# Верно решили 116 048
#
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print((a + b + c) - min(a, b, c) - max(a, b, c))
print(min(a, b, c))
# print(max, a + b + c - min - max, min, sep = '\n') -----болеее короткая запись кода


# Интересное число
# Верно решили 113 373
#

num = int(input())
a = num % 10
b = num % 100 // 10
c = num % 1000 // 100
if max(a, b, c) - min(a, b, c) == (a + b + c) - min(a, b, c) - max(a, b, c):
    print('Число интересное')
else:
    print('Число неинтересное')


# Абсолютная сумма
# Верно решили 114 168
#
a, b, c, d, e = float(input()), float(input()), float(
    input()), float(input()), float(input())
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))


# Манхэттенское расстояние
# Верно решили 112 223
#
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))


#
#
print('"Python is a great language!", said Fred. ' +
      '"' + "I don'" + 't ever remember having this')


# What's Your Name?
# Верно решили 109 883
#
name = input()
lastname = input()
print('Hello ' + name + ' ' + lastname +
      '! ' + 'You have just delved into Python')


# Футбольная команда
# Верно решили 108 573
#

el = input()
print('Футбольная команда', el, 'имеет длину', len(el), 'символов')


# Три города
# Верно решили 105 999
#
s1, s2, s3 = input(), input(), input()
if len(s1) == min(len(s1), len(s2), len(s3)):
    print(s1)
elif len(s2) == min(len(s1), len(s2), len(s3)):
    print(s2)
elif len(s3) == min(len(s1), len(s2), len(s3)):
    print(s3)


if len(s1) == max(len(s1), len(s2), len(s3)):
    print(s1)
elif len(s2) == max(len(s1), len(s2), len(s3)):
    print(s2)
elif len(s3) == max(len(s1), len(s2), len(s3)):
    print(s3)


# Арифметические строки
# Верно решили 102 681
#
# s1 = len(input()) -----для сокращения преобразований
s1, s2, s3 = input(), input(), input()
l1 = min(len(s1), len(s2), len(s3))
l2 = (len(s1) + len(s2) + len(s3)) - min(len(s1),
                                         len(s2), len(s3)) - max(len(s1), len(s2), len(s3))
l3 = max(len(s1), len(s2), len(s3))

if l2 - l1 == l3 - l2:
    print('YES')
else:
    print('NO')


# Цвет настроения синий
# 107 124
#
el = input()
if 'синий' in el:
    print('YES')
else:
    print('NO')

# Отдыхаем ли?
#  106 485
#

el = input()
# неправильная структура## ('суббота' or 'воскресенье') in s:
if 'суббота' in el or 'воскресенье' in el:
    print('YES')
else:
    print('NO')

# Корректный email
#   105 561
#
email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')

# Евклидово расстояние
#   112 055
#
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


# Площадь и длина
#   112 001
#
r = float(input())
print(math.pi * r ** 2)
print(2 * math.pi * r)

# Средние значения
#   109 613
#
a, b = float(input()), float(input())
print((a + b) / 2)
print(math.sqrt(a * b))
print(2 * a * b / (a + b))
print(math.sqrt((a**2 + b ** 2)/2))


# Тригонометрическое выражение
#  108 934
#
x = float(input())
print(math.sin(x * math.pi / 180) + math.cos(x *
      math.pi / 180) + math.tan(x * math.pi / 180)**2)


# Пол и потолок
# 109 144

x = float(input())
print(math.floor(x) + math.ceil(x))


# Квадратное уравнение 🌶️🌶️
# 104 264
#
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    print(min((-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)))
    print(max((-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)))
elif d == 0:
    print((-1 * b) / (2 * a))
else:
    print('Нет корней')


# Правильный многоугольник
# 104 972
#

n, a = float(input()), float(input())
print(n * a ** 2 / (4 * math.tan(math.pi / n)))


# Python is awesome
# 103129

for i in range(9):
    print('Python is awesome!')

 # Повторяй за мной 1
# 103129

el, r = input(), int(input())
for i in range(r):
    print(el)


# Последовательность символов
#  104 546
#

for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')


#
# Звездный прямоугольник
#

n = int(input())
for i in range(n):
    print('*' * 19)

# Повторяй за мной 2
# 104 704
#

el = input()
for i in range(10):
    print(i, el)


# Квадрат числа
# 103 590
#
num = int(input())
for i in range(num + 1):
    print('Квадрат числа', i, 'равен', i ** 2)


# Звездный треугольник
# 102 104
#
n = int(input())
for i in range(n + 1):
    print('*' * (n - i))


# Популяция
# 96 539
#
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m + m * p / 100

# Последовательность чисел 1
# 101 890
#
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)

# Последовательность чисел 2 🌶️
# 100 679
m, n = int(input()), int(input())
if m <= n:
    for i in range(m, n + 1, 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)


# Последовательность чисел 3 🌶️
#  98 192
m, n = int(input()), int(input())
for i in range(m, n - 1, -1):
    if i % 2 == 1:
        print(i)

# m, n = int(input()), int(input())                        ##  без IF
# for i in range(m - 1 + m % 2, n - 1, -2):
#    print(i)

# Последовательность чисел 4
#  97 092
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == i % 5 == 0):
        print(i)


# Таблица умножения
# 97 736
#
n = int(input())
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)


# Количество чисел
# 95 654
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if (i ** 3 % 10) == 4 or (i ** 3 % 10) == 9:
        counter += 1
print(counter)


# Сумма чисел
# 94 979
#

n = int(input())
total = 0
for i in range(1, n + 1):
    m = int(input())
    total += m
print(total)

# Асимптотическое приближение
# 91 390
#
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total - math.log(n))


# Сумма чисел 2
# 91 690
#
n, total = int(input()), 0
for i in range(1, n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        total += i
print(total)


# Факториал
# 92 680
#
n = int(input())
print(math.factorial(n))


# Без нулей
# 91 577
#
total = 1
for i in range(1, 11):
    n = int(input())
    if n != 0:
        total *= n
print(total)

# Сумма делителей
# 90 549
#
n, total = int(input()), 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)


#
#
#
n, total = int(input()), 0
for i in range(1, n + 1):
    total += ((-1) ** (i + 1)) * i
print(total)


# Наибольшие числа 🌶️🌶️
# 84 725
#
n, largest1, largest2 = int(input()), 0, 0
for i in range(1, n + 1):  # for _ in range(n):  ---------укоротить код можно
    m = int(input())
    if m > largest2:
        largest2 = m
        if largest1 < largest2:
            largest1, largest2 = largest2, largest1
print(largest1, largest2, sep='\n')


# Only even numbers 🌶️
# 87 264
#
counter = 0
for _ in range(10):
    m = int(input())
    if m % 2 != 0:
        counter = 1
if counter == 0:
    print('YES')
else:
    print('NO')

# Последовательность Фибоначчи 🌶️
# 81 668
#
n, sum, m1, m2 = int(input()), 0, 1, 1
for _ in range(1, n + 1):
    sum = m1 + m2
    print(sum, end=' ')
    m1 = m2
    m2 = sum

# До КОНЦА 1
# 89 223
#
n = input()
while n != 'КОНЕЦ':
    print(n)
    n = input()

# До КОНЦА 2
# 87 826
#

n = input()
while (n != 'КОНЕЦ') and (n != 'конец'):
    print(n)
    n = input()


# Количество членов
# 86 805
#
n = input()
i = 0
while n not in ('стоп', 'хватит', 'достаточно'):
    n = input()
    i += 1
print(i)


# Пока делимся
# 87 180
#
n = int(input())
while n % 7 == 0:
    print(n)
    n = int(input())

# Сумма чисел
# 86 711
#

n, total = int(input()), 0
while n >= 0:
    total = total + n
    n = int(input())
print(total)


# Количество пятерок
# 85 577
#
n, counter = int(input()), 0
while 0 <= n <= 5:
    if n == 5:
        counter += 1
    n = int(input())
print(counter)


# Ведьмаку заплатите чеканной монетой ( подсчет минимального количества монет)
# 82 060
#
n = int(input())
counter = 0

while n >= 25:
    n -= 25
    counter += 1

while n >= 10:
    n -= 10
    counter += 1

while n >= 5:
    n -= 5
    counter += 1

while n >= 1:
    n -= 1
    counter += 1

print(counter)


# Обратный порядок 1
# 84 887
#

n = int(input())
while n != 0:
    print(n % 10)
    n = n // 10


# Обратный порядок 2
# 84 690
#
n = int(input())
while n != 0:
    last_digit = n % 10
    print(last_digit, end="")
    n = n // 10

# max и min
# 82 741
#
n = int(input())
mx = 0
mn = 9
while n != 0:
    last_digit = n % 10
    if last_digit > mx:
        mx = last_digit
    if last_digit < mn:
        mn = last_digit
    n = n // 10
print('Максимальная цифра равна', mx)
print('Минимальная цифра равна', mn)

# n, x, m = int(input()), -1, 10
# while n:
#    x = max(x, n % 10)
#    m = min(m, n % 10)
#    n //= 10
# print('Максимальная цифра равна', x)
# print('Минимальная цифра равна', m)

# ಠ_ಠ
# ಠ_ಠ
# ಠ_ಠ
# ಠ_ಠ
# ಠ_ಠ

# Все вместе
# 79 165
#
n = int(input())
temp = n
total = counter = 0
product = 1
while temp != 0:
    last_digit = temp % 10    # первая цифра
    total += last_digit    # сумма цифр в числе
    counter += 1           # количество цифр в числе
    product *= last_digit  # произведение цифр цисла
    temp //= 10               # удалить последнюю цифру из числа


mean = total / counter  # среднее арифметическое цифр числа
first_digit = n % (10 ** counter) // 10 ** (counter - 1)  # первая цифра числа
sum_digit = n % 10 + first_digit   # сумма первой и последней цифры

print(total, counter, product, mean, first_digit, sum_digit, sep='\n')


# Вторая цифра
# 80 867
#
m = int(input())
n = m
counter = 0
while m != 0:  # или   n > 0
    last_digit = m % 10    # первая цифра
    counter += 1           # количество цифр в числе
    m //= 10               # удалить последнюю цифру из числа
print(n % (10 ** (counter - 1)) // 10 ** (counter - 2))


# n = int(input())
# while n > 99:
#    n //= 10
# print(n % 10)

# 78 600
# Одинаковые цифры
#

n = int(input())
counter1, counter2 = 0, 0
while n > 0:
    counter1 += 1
    if n % 100 // 10 == n % 10:
        counter2 += 1
    n //= 10
if counter1 == counter2 + 1:
    print('YES')
else:
    print('NO')  # print("YES" if flag == True else "NO")


# Упорядоченные цифры 🌶️
# 75 582
#

n = int(input())
counter1, counter2 = 0, 0
while n > 0:
    counter1 += 1
    if (n % 100 // 10) >= (n % 10):
        counter2 += 1
    n //= 10
if counter1 == counter2 + 1:
    print('YES')
else:
    print('NO')    # print("YES" if flag == True else "NO")
#
#

n = int(input())
while n % 10 <= n % 100 // 10:
    n = n // 10
if n < 10:
    print('YES')
else:
    print('NO')


# Наименьший делитель
# 78 127
#
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break


# Следуй правилам
# 77 488
#
n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)

# Ревью кода-1 🌶️🌶️
# 76 080
#
count = 0
p = 1                   # 1
for i in range(1, 11):  # 2
    x = int(input())
    if x > 0:
        p *= x
        count += 1
if count > 0:
    print(count)        # 3
    print(p)
else:
    print('NO')

# Ревью кода-2 🌶️🌶️
# 73 180
#
mx = -10**6  # неверно задана переменная (сравнивать будет с минимальным)
el = 0
for _ in range(10):  # неверно задан диапозон (было 11), замена "i" на "_"
    x = int(input())
    if x < 0:
        el += x  # неверно задана формула (было равенство "=")
        if x > mx:  # смещен блок кода, чтобы условие работало только для x < 0
            mx = x
if el == 0:  # не был задано условие для вывода при отсутствии отрицательных чисел
    print('NO')
else:
    print(el)
    print(mx)

# Ревью кода-3
# 73 015
#
el = 0                  # 1
for i in range(1, 8):  # 2
    n = int(input())   # 3
    if n % 2 == 0:     # 4
        el += n
print(el)


# Ревью кода-4 🌶️🌶️
# 70 702
#

n = int(input())
counter = 0
max_digit = -1                # 1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:  # 2
            max_digit = digit  # 3
        counter += 1
    n //= 10                   # 4
if counter == 0:               # 5
    print('NO')
else:
    print(max_digit)


# Ревью кода-5 🌶️
# 72 471
# выводит на экран его первую (старшую) цифру

n = int(input())
# Ошибка - цикл имеет смысл только в случае если данное натурально число дву- и  более -значное.
while n > 9:
    # Ошибка - нам необходимо постепенно отбрасывать числа до первого, а не выяснять последние из них.
    n //= 10
print(n)

n = int(input())
while n//10:
    n //= 10
print(n)


# Ревью кода-6
# 71 996
#

# Таблица-1 вложеный цикл
# 74 658
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 4):
        print(n, end=' ')
    print()


# Таблица-2
# 73 499
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 6):
        print(i, end=' ')
    print()

# Таблица-3
# 72 748
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j, end='\n')
    print()

# Звездный треугольник 🌶️🌶️
# 70 171
#
n = int(input())
for i in range(1, (n//2 + 1)):
    for j in range(1, i + 1):
        print('*', end='')
    print()

for i in range((n - n//2), 0, -1):
    for j in range(i + 1, 1, -1):
        print('*', end='')
    print()


# Численный треугольник 1
# 71 713
#
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()


# Старинная задача
# 69 262
# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?


total = 0
for n in range(101):
    for k in range(101):
        for m in range(101):
            if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
                total += 1
                print('n=', n, 'k=', k, 'm=', m)
print('Общее количество натуральных решений =', total)


# Гипотеза Эйлера о сумме степеней 🌶️🌶️
# 65 484
# __________________________________________________________


# Численный треугольник 3
# 68 249
#
n = int(input())
counter = 1
for i in range(1, n + 1):
    for j in range((n + 1)-i, n + 1):  # for _ in range(i + 1):
        print(counter, end=' ')
        counter += 1
    print()


# Численный треугольник 4
# 63 813
n = int(input())
for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end='')

    for j in range(i, 1, -1):
        print(j-1, end='')

    print()

# Делители-1 🌶️
# 60 280
# НЕ РЕШИЛ
a = int(input())
b = int(input())
total, counter, mx_total, mx_count = 0, 0, 0, 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:      # если есть делитель, то
            counter += 1    # считаем делители
            total += j      # суммируем делители
    if mx_count < counter:
        mx_count = counter
    if total > mx_total:
        mx_total = total

print(mx_count)
print(mx_total)


# Делители-2
# 61 920
#

n = int(input())

for i in range(1, n + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:      # если есть делитель, то
            counter += 1    # считаем делители
print(i, '+' * counter, sep='')


# Цифровой корень, вложеные циклы while
# 60 236

n = int(input())
while n > 9:
    total = 0
    while n > 0:               # пока в числе есть цифры
        last_digit = n % 10     # берем посдеднюю
        total += last_digit     # суммируем цифру
        n //= 10                # убрать последнюю
    # присваиваем сумму   и проверяем, если оно двухзначное, то повторяется суммация цифр заново
    n = total
print(n)


# Сумма факториалов
# 60 921

n = int(input())
factorial = 1
total = 0
for i in range(1, n + 1):
    #  print('i=', i)
    for j in range(1, i + 1):
        factorial *= j
        #  print( 'j =', j, 'Factorial =', factorial)
    total += factorial
    factorial = 1
    #  print('total =', total)
print(total)


# Простые числа
# 59 392
#
a = int(input())
b = int(input())
count_del = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            count_del += 1
    if count_del == 2:
        print('число', i, 'простое')


# Все вместе 2
# 52 745
#
n = int(input())
counter1 = 0
counter2 = 0
counter3 = 0
tolal_digit = 0
prod_digit = 1
count_prod = 0
last_digit2 = n % 10
counter6 = 0
while n > 0:
    last_digit = n % 10

    if last_digit == 3:   # 1
        counter1 += 1

    if last_digit == last_digit2:
        counter2 += 1

    if last_digit % 2 == 0:
        counter3 += 1

    if last_digit > 5:
        tolal_digit += last_digit

    if last_digit > 7:
        prod_digit *= last_digit
        count_prod += 1

    if last_digit == 0 or last_digit == 5:
        counter6 += 1

    n //= 10

print(counter1)
print(counter2)
print(counter3)
print(tolal_digit)
if count_prod == 0:
    print(1)
else:
    print(prod_digit)
print(counter6)


# Числа Рамануджана 🌶️
# 51 160
#
cnt = 0
dig = 1
cnt_2 = -1

while cnt < 5:
    dig += 1
    for i in range(1, int(dig**(1 / 3)) + 1):
        for j in range(i + 1, int(dig**(1 / 3)) + 1):
            if i**3 + j**3 == dig:
                cnt_2 += 1
            if cnt_2 == 1:
                break
        if cnt_2 == 1:
            print(dig)
            cnt += 1
            break
    cnt_2 = -1


# В столбик 1
#  64 558
#
el = input()
for i in range(0, len(el), 2):
    print(el[i], end='\n')


# В столбик 2
#  64 217
#
el = input()
for i in range(-1, -len(el) - 1, -1):
    print(el[i], end='\n')

# ФИО
# 64 239
#
el, s1, s2 = input(), input(), input()
print(s1[0], el[0], s2[0], sep='')

# Цифра 1
# 63 623
el = input()
total = 0
for i in range(len(el)):
    total += int(el[i])
print(total)

# Цифра 2
# 62315
s1 = input()
s2 = '0123456789'
counter = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if (s1[i]) == s2[j]:
            counter += 1

if counter > 0:
    print('Цифра')
else:
    print('Цифр нет')

## ###################################################################
el = input()
digits = '0123456789'

for i in el:
    if i in digits:
        print('Цифра')
        break
else:
    print('Цифр нет')


# Сколько раз?
# 62 317
el = input()
counter1, counter2 = 0, 0
# for i in range(len(s)):
for i in el:
    if i in '+':
        counter1 += 1
    if i in '*':
        counter2 += 1

print('Символ + встречается', counter1, 'раз')
print('Символ * встречается', counter2, 'раз')

# Одинаковые соседи
# 60 450
el = input()
counter1 = 0
for i in range(len(el) - 1):
    if el[i] == el[i + 1]:
        counter1 += 1
print(counter1)

# Гласные и согласные
# 59 520
s1 = input()
s2 = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
s3 = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
counter1, counter2 = 0, 0
for i in s1:
    if i in s2:
        counter1 += 1
    if i in s3:
        counter2 += 1
print('Количество гласных букв равно', counter1)
print('Количество согласных букв равно', counter2)


# Decimal to Binary
# 57 843
digit_dec = int(input())
digit_bin = ''
while digit_dec > 0:
    # число читается в обратном порядке остатков от деления, поэтому поменяны местами слагаемые, чтобы попорядку запись в строку производилась
    digit_bin = str(digit_dec % 2) + digit_bin
    digit_dec = digit_dec // 2
print(digit_bin)
# 19 = 10011

# Палиндром
# 60 895

el = input()
if el == el[::-1]:
    print('YES')
else:
    print('NO')


# Делаем срезы 1
# 60 004
el = input()
print(len(el))
print(el * 3)
print(el[0])
print(el[:3])
print(el[-3:])
print(el[::-1])
print(el[1:-1])


# Делаем срезы 2
# 58 742
el = input()
print(el[2])
print(el[-2])
print(el[:5])
print(el[:-2])
print(el[::2])
print(el[1::2])
print(el[::-1])
print(el[::-2])


# Две половинки
# 58 135

el = input()
n = len(el)

a = el[:(n + 1) // 2]
b = el[(n + 1) // 2:]

print(b + a)


# Заглавные буквы
# 59 799
el = input()
i = 0
counter1 = 0
while el[i] != ' ':
    counter1 += 1
    i += 1
name = el[:counter1]
print(name)
lastname = el[counter1 + 1:]
print(lastname)
if name == name.capitalize() and lastname == lastname.capitalize():
    print('YES')
else:
    print('NO')


# короткое решение
el = input()
if el == el.title():
    print("YES")
else:
    print("NO")


# sWAP cASE
# 60 011
el = input()
print(el. swapcase())

# Хороший оттенок
# 59 314
el = input()
if 'хорош' in el.lower():
    print('YES')
else:
    print("NO")


# Нижний регистр
# 57 635
el = input()
counter = 0

for simbol in el:
    if simbol != simbol.upper():
        counter += 1

# for i in range(len(s)):
  #  if s[i] in 'abcdefghijklmnopqrstuvwxyz':
   #     counter += 1
print(counter)


# Количество слов
# 58 413
el = input()
print(s1.count(' ') + 1)

# минутка генетики
# 57 960
el = input()
el = el.lower()                       # s = input().lower()
print('Аденин:', el.count('а'))
print('Гуанин:', el.count('г'))
print('Цитозин:', el.count('ц'))
print('Тимин:', el.count('т'))

# Очень странные дела
# 56 321
n = int(input())
counter = 0
for i in range(n):
    el = input()
    if el.count('11') >= 3:
        counter += 1
print(counter)

# Количество цифр
# 56 659
el = input()
counter_number = 0
str_number = '0123456789'
for i in range(len(el)):
    if str_number.count(el[i]) == 1:
        counter_number += 1
print(counter_number)

#
# второе решение
text = input()
cnt = 0
for i in range(10):
    cnt += text.count(str(i))
print(cnt)
#


# .com or .ru
# 56 243
text = input()
# ###  if (text.endswith(('.com','.ru'))):
if text.endswith('.com') or text.endswith('.ru'):
    print('YES')
else:
    print('NO')

# Самый частотный символ
# 53 222
#
text = input()
alphabet = ' 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
letter_mx = ''
mx = 0
for letter in alphabet:
    if text.count(letter) >= mx:
        letter_mx = letter
        mx = text.count(letter)
print(letter_mx)
###
#
# короткое решение
el = input()

most_common = el[0]
for el in el:
    if el.count(el) >= el.count(most_common):
        most_common = el

print(most_common)

#
#  Первое и последнее вхождение
# 54 619

text = input()
if text.count('f') == 1:
    print(text.find('f'))
if text.count('f') >= 2:
    print(text.find('f'), text.rfind('f'))
if text.count('f') == 0:
    print('NO')

# второе решение через find
el = input()
if el.find('f') == -1:
    print('NO')
elif el.find('f') == el.rfind('f'):
    print(el.find('f'))
else:
    print(el.find('f'), el.rfind('f'))


# Удаление фрагмента
# 53 975
#
text = input()
print(text[:text.find('h')] + text[text.rfind('h'):])

#
year = '2010'
sum = '10k'
currency = 'Bitcoin'

el = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, sum, currency)
print(el)


#
#
year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


# Символы в диапазоне
# 55 089
a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')

# Простой шифр
#  54 402
text = input()
for c in text:
    print(ord(c), end=' ')


# Шифр Цезаря 🌶️
# 49 970
n = int(input())
text = input()
for c in text:
    if ord(c) - n < 96:
        print(chr(ord(c) - n + 26), end='')
    else:
        print(chr(ord(c) - n), end='')

# Каждый третий
# 46 693
text = input()
el = ""
for i in range(len(text)):
    el += text[i]

    if i == 0 or i % 3 == 0:
        el = el[:-1]

print(el)


# Замени меня полностью
# 46 824
text = input()
print(text.replace('1', 'one'))

# Удали меня полностью
# 46 941
text = input()
print(text.replace('@', ''))

# Второе вхождение
# 45 537
text = input()
el = ""
i = 0
if text.count('f') >= 2:
    text = text[(text.find('f') + 1):]
    print(text.find('f'))

elif text.count('f') == 1:
    print(-1)

elif text.count('f') == 0:
    print(-2)

#
# правильное решение методами
el = input()

if el.count("f") == 0:
    print(-2)
elif el.count("f") == 1:
    print(-1)
else:
    # s = s.replace('f', 'k' , 1)   # можно так тоже
    res = el.replace("f", ".", 1).find("f")
    #  print(s.find('f'))
    print(res)


#
#
text = input()
a = text.find('h')
b = text.rfind('h')

# print(s.replace(s[a+1:b], s[b-1:a:-1]))  # можно так тоже
print(text[:a + 1] + text[b:a:-1] + text[b:])


# Список чисел
# 54 864

n = int(input())
print(list(range(1, n + 1)))

# Список букв
#  53 820
n = int(input())
str1 = list(range(n))
for i in range(n):
    str1[i] = chr(96 + i)
print(str1)

# второе решение
n = int(input())

el = ""
for i in range(n):
    el += chr(ord("a") + i)

print(list(el))

#
#
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
for i in range(len(rainbow)):
    print(i)
    print(rainbow[i])
    if rainbow[i] == 'Green':
        rainbow[i] = 'Зеленый'
    elif rainbow[i] == 'Violet':
        rainbow[i] = 'Фиолетовый'

print(rainbow)

#
#
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic',
             'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

print(languages[::-1])

# Все сразу 1 🌶️
# 53 091
umbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10,
          10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
counter1, counter2 = 0, 0
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
for i in range(len(numbers)):
    if numbers[i] == 5:
        counter1 += 1
    if numbers[i] == 17:
        counter2 += 1

if counter1 > 0 and counter2 > 0:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

# второе решение
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10,
           10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

# список строк
# 53413
n = int(input())
list_str = list(range(n))
for i in range(n):
    list_str[i] = input()
print(list_str)


# второе решeyие
n = int(input())
seq = []
for _ in range(n):
    seq.append(input())
print(seq)

# третье решение
print([input() for _ in range(int(input()))])


# Алфавит
# 52 030

l = []
for i in range(1, 27):
    l.append(chr(96 + i) * i)    # chr(ord("a") + i)
print(l)

# dnjhjt решение
res = []
for i in range(26):
    cur = ""
    for j in range(i + 1):
        cur += chr(ord("a") + i)

    res.append(cur)

print(res)


# Список кубов
# 52 481

n = int(input())
l = []
for i in range(1, n + 1):
    l.append((int(input())) ** 3)
print(l)


# Список делителей
# 52 442
n = int(input())
l = []

for i in range(1, n + 1):    # Можно ускорить, если сделать так: range(1, n//2+1)
    if n % i == 0:
        l.append(i)

print(l)


# Суммы двух
# 50 171
n = int(input())
l1 = []
l2 = []

for i in range(n):
    l1.append(int(input()))
for i in range(n - 1):
    l2.append(l1[i] + l1[i + 1])

print(l2)


# Удалите нечетные индексы
# 51 152
n = int(input())
l1 = []
l2 = []
for i in range(n):
    l1.append(int(input()))
for i in range(0, n, 2):
    l2.append(l1[i])
print(l2)

# второе решение
n = int(input())
seq = []

for _ in range(n):
    cur = int(input())
    seq.append(cur)

print(seq[::2])


# k-ая буква слова 🌶️🌶️
# 48 314
n = int(input())
l1 = []


str1 = ''
for _ in range(n):
    l1.append(input())

k = int(input())

for i in range(n):
    if len(l1[i]) >= k:
        str1 += l1[i][k-1]

print(str1)


# Символы всех строк
# 50 663
l = []
for _ in range(int(input())):
    l.extend(input())
print(l)

#
#
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(*numbers)

# Значение функции
# 50 131
# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая для каждого введенного числа xx выводит значение функции f(x)=x2+2x+1f(x)=x2+2x+1, каждое на отдельной строке.
n = int(input())
l = []

for _ in range(n):
    x = int(input())
    l.append((x + 1) ** 2)
    print(x)

print()
print(*l, sep='\n')

# Remove outliers
# 49 807
# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
n = int(input())
l1 = []
l2 = []
mx, mn = 0, 0

for _ in range(n):
    l1.append(int(input()))

# метод index - возвращает индекс первого вхождения минимума в списке l1
del l1[l1.index(min(l1))]
del l1[l1.index(max(l1))]   # del - удаляем элт с индексом

print(*l1, sep='\n')

# Без дубликатов
# 49 222
# На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
n = int(input())
l1 = []

for i in range(n):
    el = input()
    if el not in l1:   # если в списке l1 нет элемента s, переносим его
        l1.append(el)

print(*l1, sep='\n')


# Google search - 1
# 48 232
# На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
n = int(input())
l1 = []

for i in range(n):
    el = input()
    l1.append(el)

search = input()

for i in range(n):
    if search.lower() in l1[i].lower():
        print(l1[i])

# Google search - 2 🌶️🌶️
# 44 458
# На вход программе подается натуральное число nn, затем nn строк, затем число kk — количество поисковых запросов, затем kk строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.

n = int(input())
l1 = []
for _ in range(n):  # создали список n строк
    el = input()
    l1.append(el)

k = int(input())
l2 = []
for _ in range(k):  # создали список k строк поисковых запросов
    s1 = input()
    l2.append(s1)

for i in range(n):   # проверяем совпадения
    counter = 0
    for j in range(k):
        if l2[j].lower() in l1[i].lower():
            counter += 1                     # если насчитал к совпадений

    print('cnt=', counter)     # выводим эту строку
    if counter == k:
        print(l1[i])
# ______________________________________________________________
# второе решение от препода
n = int(input())

strings = []
for _ in range(n):
    el = input()
    strings.append(el)

k = int(input())

search_queries = []
for _ in range(k):
    search_query = input()
    search_queries.append(search_query)

for el in strings:
    for search_query in search_queries:
        if search_query.lower() not in el.lower():
            break
    else:
        print(el)


# Negatives, Zeros and Positives
# 47 754
# На вход программе подается натуральное число n, а затем nn целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
n = int(input())
l1 = []

for i in range(n):  # создаем список чисел
    el = int(input())
    l1.append(el)

for i in range(n):  # выводим отрицательные числа
    if l1[i] < 0:
        print(l1[i])

for i in range(n):  # выводим нули
    if l1[i] == 0:
        print(l1[i])

for i in range(n):  # выводим положительные числа
    if l1[i] > 0:
        print(l1[i])

# ____________________________правильное(рациональное) решение_____________________
# т.к. создавать лишние переменные ИЛИ крутить 4 цикла затратно

a, b, c = [], [], list()       # создаём 3 списка , для - 0 +
for _ in range(int(input())):          # цикл n чисел
    n = int(input())            # вводим числа
    if n < 0:                   # если число больше нуля
        # то записываем его в список положительных чисел
        a.append(n)
    elif n == 0:
        b.append(n)
    elif n > 0:
        c.append(n)
print(*a, sep='\n')   # выводим списки попорядку
print(*b, sep='\n')
print(*c, sep='\n')
# _________________________________________________________________________________

# Построчный вывод
# 49 627
# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

el = input()          # ввод строки
words = el.split()    # создаем список, где каждое слово строки - элемент списка
print(*words, sep='\n')  # выводим элементы списка, каждый с новой строки


print(*input().split(), sep='\n')   # тоже самое, ТОЛЬКО КОРОЧЕ!!

# или
print('\n'.join(input().split()))   # тоже самое

print(input().replace(' ', '\n'))   # тоже самое
# _________________________________________________________________________


# Инициалы
# 48 955
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.
el = input()
l1 = el.split()

l2 = []
for i in range(len(l1)):
    l2.append(l1[i][0])

print('.'.join(l2) + '.')
# ------------------правильный вариант---------------------------
full_name = input().split()
print(full_name[0][0], full_name[1][0], full_name[2][0], sep=".", end=".")
# ___________________________________________________________________________

# Windows OS
# 48 417
# В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  "\",  затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).
print(*input().split('\\'), sep='\n')

# Диаграмма
# 48 198
# На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.
str_num = input().split()  # создаём список с вводимыми числами (в формате str)

for i in range(int(len(str_num))):
    print('+' * int(str_num[i]), sep='\n')
# ----------------------------------------------
seq = input().split()

for el in seq:              # перебираем каждый символ
    print("+" * int(el))    # и выводим плюсы
# ______________________________________________

# Корректный ip-адрес
# 47 345
# На вход программе подается строка текста, содержащая 4 целых положительных числа, разделенных точкой. Напишите программу, которая определяет, является ли введенная строка текста корректным ip-адресом.
ip = input().split('.')
cnt = 0
for el in ip:
    if 0 <= int(el) <= 225:
        cnt += 1
if cnt == len(ip):
    print('ДА')
else:
    print('НЕТ')
# --------------------------------------------
seq = input().split(".")

for el in seq:
    if not (0 <= int(el) <= 255):
        print("НЕТ")
        break
else:                               # будет выполняться только тогда, когда цикл завершится штатным образом
    print("ДА")                     # т.е. без остановки от BREAK
# ________________________________________


# Добавь разделитель
# 47 471
# На вход программе подается строка текста и строка-разделитель. Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.

el = list(input())           # переводим элементы строки в список
simbol = input()            # вводим символы разделитель
# с помощью f-строки склеиваем строку с разделителями
print(f'{simbol}'.join(el))
# --------------------------------
el = input()
simbol = input()

res = simbol.join(el)
print(res)
# ________________________________________

# Количество совпадающих пар
# 44 202
# На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

el = input().split()  # Из данной строки формируется список чисел
cnt = 0
for i in range(len(el)):
    for j in range(i + 1, len(el)):
        if el[i] == el[j]:
            cnt += 1

print(cnt)


# Все сразу 2 🌶️
# 46 655
#

numbers = [8, 9, 10, 11]
# print(*numbers)

numbers[1] = 17
# print(*numbers)

numbers.extend([4, 5, 6])
# print(*numbers)

del numbers[0]
# print(*numbers)

numbers *= 2
# print(*numbers)

numbers.insert(3, 25)
print(numbers)

# Переставить min и max
# 44 109
# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

str_num1 = input().split()
str_num2 = []

for i in range(len(str_num1)):
    # print('i=', i, end=' ')
    str_num2.append(int(str_num1[i]))
    # print('str_num2=', str_num2)
# print(*str_num2)
mn = str_num2.index(min(str_num2))
# print(mn)
mx = str_num2.index(max(str_num2))
# print(mx)
str_num2[mn], str_num2[mx] = str_num2[mx], str_num2[mn]
print(*str_num2)
# ---------------------------------------
seq = []
for el in input().split():
    seq.append(int(el))

mx_ind = seq.index(max(seq))
mn_ind = seq.index(min(seq))
seq[mx_ind], seq[mn_ind] = seq[mn_ind], seq[mx_ind]

print(*seq)
# ____________________________________________________


# Количество артиклей
# 44 494
# На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'
text1 = input().split()
text2 = []

for i in range(len(text1)):
    text2.append(text1[i].lower())

cnt_article = text2.count('a') + text2.count('an') + text2.count('the')
print('Общее количество артиклей:', cnt_article)
# -----------------------------------------------------------
seq = input().lower().split()
res = seq.count("a") + seq.count("an") + seq.count("the")

print(f"Общее количество артиклей: {res}")
# _____________________________________________________________

# Взлом Братства Стали 🌶️
# 40 353
# Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали и любезно соглашается помочь им в решении их проблем. Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. Известно, что программисты Братства никогда не оставляют комментарии к коду и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. Помогите писцу Ибсену удалить все комментарии из программы.


n = input()
n = n[1:]

for i in range(int(n)):
    t = input().split('#')
    el = t[0]
    x = el.rstrip()
    print(x)

# Сортировка чисел
# На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. #
# 43 765
el = input().split()  # создаем список из строки
s1 = []
for i in range(len(el)):
    s1.append(int(el[i]))
s1.sort()
print(*s1)
s1.sort(reverse=True)  # используем параметр revers
# -------------------------------------------------
seq = []
for el in input().split():
    seq.append(int(el))

seq.sort()
print(*seq)

seq.reverse()
print(*seq)
# ________________________________________________


# Дополните приведенный код, используя списочное выражение так, чтобы получить новый список, содержащий строки исходного списка с удаленным первым символом.
# 44 866
#
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
            'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# удаляем первый символ в каждом элементе списка
new_keywords = [el[1:] for el in keywords]
print(new_keywords)

# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк исходного списка.
# 44 795
#
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
            'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# формируем список lengths, в котором каждому элементу списка присваивается значение len(el) - длины строки(эл-та списка keywords). перебирая циклом список keywords
lengths = [len(el) for el in keywords]
print(lengths)

#
# 44 434
# Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
            'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [el for el in keywords if len(el) >= 5]
print(new_keywords)

#
# 43 724
# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел-палиндромов от 100100 до 10001000.
palindromes = [str(i) for i in range(1000) if str(i) == str(i)[::-1]]
print(palindromes)

# Списочное выражение 1
#  44 252
# На вход программе подается натуральное число nn. Напишите программу, использующую списочное выражение, которая создает список, содержащий квадраты чисел от 11 до nn (включительно), а затем выводит его элементы построчно, то есть каждый на отдельной строке.
n = int(input())
quad = [i**2 for i in range(1, n + 1)]
print(*quad, sep='\n')


# Списочное выражение 2
# 43 095
# На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел также на одной строке.
#
el = input().split()
cubes = [(int(el[i]))**3 for i in range(0, len(el))]
print(*cubes)
# --------------------------------------------------------------
seq = [int(el) for el in input().split()]    # сoздаем список сичитаных чисел
cubes = [el ** 3 for el in seq]              # создаем список кубов тех чисел

for el in cubes:                 # Для вывода элементов списка используйте цикл for
    print(el, end=' ')             # выводим числа в одну строчку
# ______________________________________________________

# В одну строку 1
# 43 542
# На вход программе подается строка текста, содержащая слова. Напишите программу, которая выводит слова введенной строки в столбик.
# Примечание. Программу можно написать в одну строку кода.
print(*[el for el in input().split()], sep='\n')
# ---------------------
print(*input().split(), sep='\n')
#
[print(s) for s in input().split()]
# _____________________________________________

# В одну строку 2
# 42 466
# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.
# Примечание. Программу можно написать в одну строку кода.

print(*[el for el in input() if el in '1234567890'], sep='')
# --------------------------------------------------------------
digits = [el for el in input() if el.isdigit()]
print(*digits, sep="")
# --------------------------------------------------------------
# строковый метод - isdigit(). если с состоит только из цифровых символов
print(*[c for c in input() if c.isdigit()], sep='')
# ______________________________________________________________


# В одну строку 3
# 41 868
# На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выводит не оканчивающиеся на цифру 44 квадраты четных чисел.
# Программу можно написать в одну строку кода.

print(*[int(el)**2 for el in input().split() if int(el) %
      2 == 0 and int(el) ** 2 % 10 != 4])

#
# 42 843
# Оптимизируйте приведенный код, реализующий алгоритм пузырьковой сортировки.
a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97,
     0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)
flag = False
for i in range(n - 1):

    if flag:                   # условие остановки
        break
    flag = True
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = False                            # флаг для остановки

print(a)

# Сортировка выбором
# 38 845
# Отсортируйте список по возрастанию, реализовав алгоритм сортировки выбором.

# Сортировка выбором улучшает пузырьковую сортировку, совершая всего один обмен за каждый проход
# по списку. Для этого алгоритм ищет максимальный элемент и помещает его на соответствующую позицию.
# Как и для пузырьковой сортировки, после первого прохода самый большой элемент находится
# на правильном месте. После второго прохода на своё место становится следующий максимальный элемент.
# Проходы по списку повторяются n−1 раз, где n – длина списка, поскольку последний из них
# автоматически оказывается на своем месте.

# не выполнил это задание
# ________________________________________________________________

# Список четных
# 36 662
# На вход программе подается четное число n, n≥2n,n≥2. Напишите программу, которая выводит список четных чисел
# [2, 4, 6, ..., n].

n = int(input())
nums = [i for i in range(1, n + 1) if i % 2 == 0]
print(nums)
# --------------------------------------
n = int(input())
seq = list(range(2, n + 1, 2))

print(seq)
# __________________________________________

# Сумма двух списков
#
# На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.

l1 = input().split()
l2 = input().split()
l3 = []
for i in range(len(l1)):
    l3.append(int(l1[i]) + int(l2[i]))

print(*l3)
# -----------------------------------
a = input().split()
b = input().split()
n = len(a)

seq = [int(a[i]) + int(b[i]) for i in range(n)]
print(*seq)
# _________________________________________

# Сумма чисел
# 36 452
# На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

l1 = input().split()
total = 0
print(*l1, sep='+', end='')
print('=', end='')
for el in l1:
    total += int(el)
print(total)
# ----------------------------------
seq = input().split()
expression = "+".join(seq)

sm = 0
for el in seq:
    sm += int(el)
expression += f"={sm}"

print(expression)
# ___________________________________________

# Валидный номер 🌶️🌶️
# 34 803
# На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером. Строка текста является корректным телефонным номером, если она имеет формат:
#    abc-def-hijk или
#    7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

t = input().split('-')
# 7-301-447-5820
if len(t) == 3:
    if (t[0].isdigit() == True and len(t[0]) == 3) and (t[1].isdigit() == True and len(t[1]) == 3) and (t[2].isdigit() == True and len(t[2]) == 4):
        print('YES')
    else:
        print('NO')
elif len(t) == 4:
    if (t[0].isdigit() == True and len(t[0]) == 1 and t[0] == '7') and (t[1].isdigit() == True and len(t[1]) == 3) and (t[2].isdigit() == True and len(t[2]) == 3) and (t[3].isdigit() == True and len(t[3]) == 4):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
# ---------------------------------------------------
seq = input().split("-")
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and "".join(seq).isdigit() and seq[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(seq).isdigit():
    print("YES")
else:
    print("NO")
# _____________________________________________________


# Самый длинный
# 36 239
# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.

l1 = input().split()
# проспал почти всю ночь
lens = [len(el) for el in l1]
print(max(lens))
# --------------------------------------------
lens = [len(el) for el in input().split()]
print(max(lens))
# ____________________________________________

# Молодежный жаргон
# 35 555
# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая преобразует каждое слово введенного текста в "молодежный жаргон" по следующему правилу:
# первая буква каждого слова удаляется и ставится в конец слова;
# затем в конец слова добавляется слог "ки".
l1 = input().split()
cod = []
# проспал почти всю ночь
# роспалпки очтипки сювки очьнки
# cod = [el[0], el[-1] = el[-1], el[0] for el in l1]

for el in l1:
    # el[0], el[-1] = el[-1], el[0]
    # el = el + 'ки'
    el = el[1:] + el[0] + 'ки'
    cod.append(el)
print(*cod)
# ----------------------------------------------------
print(*[el[1:] + el[0] + 'ки' for el in input().split()])
# ___________________________________________________________

# Звездный прямоугольник 1
# 42 651
# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×1014×10 в соответствии с образцом:

# объявление функции


def draw_box():
    print('*' * 10)
    for i in range(12):
        print("*", "*", sep=" " * 8)
    print('*' * 10)


# основная программа
draw_box()  # вызов функции
# ______________________________________________


# Звездный треугольник 1
# 42 455
# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 1010 в соответствии с образцом:

# объявление функции
def draw_triangle():
    l1 = ['*' * i for i in range(1, 11)]
    print(*l1, sep='\n')


# основная программа
draw_triangle()  # вызов функции
# _________________________________________________

# Звездный треугольник
# 41 207
# Напишите функцию

# объявление функции


def draw_triangle(fill, base):
    for i in range(1, base // 2 + 1):
        print(fill * i)
    for i in range(base // 2 + 1, 0,  -1):
        print(fill * i)


# основная программа
fill = input()
base = int(input())
draw_triangle(fill, base)  # вызов функции


# ФИО
# 41 700
# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра: а затем выводит на печать ФИО человека.

# объявление функции
def print_fio(name, surname, patronymic):
    fio = [surname[0].upper(), name[0].upper(), patronymic[0].upper()]
    print(*fio, sep='')


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
# ------------------------------------------------------------------------------
# объявление функции


def print_fio(name, surname, patronymic):
    full_name = (surname[0] + name[0] + patronymic[0]).upper()
    print(full_name)


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
# ________________________________________________________________________________

# Сумма цифр
# 41 123
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

# объявление функции


def print_digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    print(total)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
# ________________________________________________________________

#
#
# Напишите функцию, которая возвращает длину гипотенузы прямоугольного треугольника по известным значениям его катетов.


def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c
#
#
#


def do_something(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result


# Что будет выведено в результате выполнения следующего программного кода?
print(do_something([2, 2, 2, 2]))
# ответ = 16
# __________________________________________________________________________
# Конвертер километров
# 40 858
# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.
# объявление функции


def convert_to_miles(km):
    ml = km * 0.6214
    return ml


# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))
# __________________________________________________________________________

# Количество дней
# 40 495
# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

# объявление функции


def get_days(month):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = month[num - 1]
    return day


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
# __________________________________________________________________________

# Делители 1
# 40 304
# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

# объявление функции


def get_factors(num):
    div = []
    for i in range(1, n // 2 + 1):  # Делители находятся до половины числа (для быстроты выполнения)
        if n % i == 0:
            div.append(i)
    # также добавляем делитель числа на самого себя, в список
    div.append(num)
    return div


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
# __________________________________________________________________________


# Делители 2
# 40 032
# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

def get_factors(num):
    div = []
    for i in range(1, n // 2 + 1):  # Делители находятся до половины числа (для быстроты выполнения)
        if n % i == 0:
            div.append(i)
    # также добавляем делитель числа на самого себя, в список
    div.append(num)

    return len(div)


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
# __________________________________________________________________________


# Найти всех
# 38 743
# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

# объявление функции
def find_all(target, symbol):
    l1 = []
    for i in range(len(target)):
        if target[i] == symbol:
            l1.append(i)
    return l1


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
# -----------------------второе решение-----------------------------------------


def find_all(target, symbol):
    cur = 0
    res = []

    for i in target:
        if i == symbol:
            res.append(cur)

        cur += 1

    return res


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
# __________________________________________________________


# Merge lists 1
# 38 901
# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.


# print(merge([1, 2, 3], [5, 6, 7, 8]))
# print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
# объявление функции
def merge(list1, list2):
    list3 = []
    list3 = list1 + list2    # формируем общий список
    list3.sort()
    return list3


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
# __________________________________________________________


# Слияние двух отсортированных списков
#
# Merge lists 2
# На вход программе подается число nn, а затем nn строк, содержащих целые числа в порядке возрастания. Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.
# 34 987

# объявление функции
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]

    return result


# кол-во строк
n = int(input())
# Заводим новый список, в котором будет окончательный результат
total_list = []
# Указываем количество списков, которые нужно отсортировать в единый список
for i in range(n):
    #  Вводим отсортированные списки, которые нужно отсортировать в единый
    num = [int(el) for el in input().split()]

    # Вызываем функцию сортировки и передаем сначала пустой список и первый веденый, будем сравнивать "два списка". Сначала пустой и первый отсортированный, после первого сравнения сохраниться результат в наш пустой список "total_list". После будет сортироваться новоиспеченный сохраненный список "total_list" и новый введенный пользователем.
    total_list = quick_merge(total_list, num)


# выводим результат через " * ". Ложитесь спать и не разносите квартиру)))))))))
print(*total_list)
# ___________________________________

#
#
# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.

# объявление функции


def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
# __________________________________________________________

# Is a Number Prime? 🌶️
# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.
#


def is_prime(num):
    cnt_div = 0
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                cnt_div += 1
                break
        if cnt_div == 0:
            return True
        else:
            return False

    else:
        return False


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
# -----------------------решение автора--------------------------------
# объявление функции


def is_prime(num):
    if num == 1:
        return False  # число 1 не является простым

    # можно идти до корня из числа, чтобы проверить его на простоту.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель

    return True


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

# __________________________________________________________


# Next Prime 🌶️🌶️
#
# 36 067

# объявление функции проверки на простое число.
def is_prime(num):
    if num == 1:
        return False  # т.к. число 1 не является простым.

    # можно идти до корня из числа, чтобы проверить его на простоту.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель.

    return True

# объявление функции поиска следующего за введенным числом простого числа.


def get_next_prime(num):
    cur_num = num + 1  # начинаем искать следующее простое число
    while not is_prime(cur_num):  # cur_num - текущее число
        cur_num += 1              # # если следующее число непростое, то увеличиваем на 1
    return cur_num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
# __________________________________________________________


# Good password 🌶️
# 35 878
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является надежным и False - в противном случае.
# Пароль является надежным если:

#    его длина не менее 88 символов;
#    он содержит как минимум одну заглавную букву (верхний регистр);
#    он содержит как минимум одну строчную букву (нижний регистр);
#    он содержит хотя бы одну цифру.

# функция проверки пароля
def is_password_good(password):
    if len(password) >= 8 and password.isalnum() and not (password.isalpha()) and not (password.isdigit()) and not password.islower() and not password.isupper():
        return True
    else:
        return False


# ввод пароля
s = input()


# вызов функции
print(is_password_good(s))
# -------------------------------решение учителя-----------------------


def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
# __________________________________________________________


# Ровно в одном
# 35 592
#

# функция проверки
def is_one_away(word1, word2):

    if len(word1) == len(word2) and word1 != word2:

        cnt_symbol = 0
        for i in range(len(word1)):

            if word1[i] != word2[i]:
                cnt_symbol += 1
            if cnt_symbol > 1:  # останавливаем перебор если есть вТорое различие букв
                break
        else:
            return True         # блок при штатном завершении цикла
        return False          # если сработал break

    else:
        return False            # если слова не одинаковой длины или одинаковые по написанию


# ввод слов
s1, s2 = input(), input()

# вызов функции
print(is_one_away(s1, s2))
# -----------------------------решение от препода-------------------------------------
# объявление функции


def is_one_away(word1, word2):
    mismatches = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatches += 1

        # возвращаем результат логического выражения, что эта переменная равна 1
        return mismatches == 1
        # тут логическое выражение. Функция возвращает уже результат, либо True, либо False.
    return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
# __________________________________________________________


# Палиндром 🌶️
# 35 153
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.

# palindromes = [str(i) for i in range(1000) if str(i) == str(i)[::-1]]
# print(palindromes)

# объявление функции
def is_palindrome(text):

    # text = text.lower()
    # перебираем посимвольно строку text.
    # если el состоит только из буквенных символов, то
    # склеиваем без пробелов стороку (конвертируя el в нижний регистр)
    text1 = "".join(el.lower() for el in text if el.isalpha())

    # если если строка text равна этой строке только в обратном порядке, то
    # функция вернёт True, а если нет - False
    return text1 == text1[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
# --------------------------от препода--------------------
#
# Сначала удаляем ненужные символы, затем строим срез, переворачивающий строку и проверяем на равенство:
# объявление функции


def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
# __________________________________________________________


# BEEGEEK
# 32 991
# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#  число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка и False - в противном случае.

# ======================================================
# ======================================================
def is_palindrome(text):

    # text = text.lower()
    # перебираем посимвольно строку text.
    # если el состоит только из буквенных символов, то
    # склеиваем без пробелов стороку (конвертируя el в нижний регистр)
    text1 = "".join(el.lower() for el in text if el.isdigit())

    # если если строка text равна этой строке только в обратном порядке, то
    # функция вернёт True, а если нет - False
    return text1 == text1[::-1]
# ======================================================
# ======================================================
# объявление функции проверки на простое число.


def is_prime(num):
    if num == 1:
        return False  # т.к. число 1 не является простым.

    # можно идти до корня из числа, чтобы проверить его на простоту.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель.

    return True
# ======================================================
# ======================================================
# функция проверки на четное число


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# объявление функции
def is_valid_password(password):
    pass1 = password.split(':')
    if len(pass1) == 3:
        return is_palindrome(pass1[0]) and is_prime(int(pass1[1])) and is_even(int(pass1[2]))
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
# __________________________________________________________


# Правильная скобочная последовательность 🌶️
# 32 828
# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента
# непустую строку text, состоящую из символов ( и ) и возвращает значение True если
# поступившая на вход строка является правильной скобочной последовательностью и
# False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка,
# состоящая только из символов ( и ), где каждой открывающей скобке найдется
# парная закрывающая скобка (при этом каждая открывающая скобка должна быть левее
# соответствующей ей закрывающей скобки).


# объявление функции
def is_correct_bracket(text):
    # text1 = list(text)
    # text1 = "".join(el.lower() for el in text if el == chr(40) or el == chr(41)) # склеиваем строку только с символом скобок

    cnt = 0
    for el in text:
        if cnt < 0:
            break
        elif el == '(':
            cnt += 1
        elif el == ')':
            cnt -= 1

    return cnt == 0     # если пусто в остатке, то возвращаем  True, иначе вернется False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
# --------------------------------jn препода-----------------------


def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")    # удаляем символы ()

    return text == ""  # если пусто в остатке, то возвращаем  True, иначе вернется False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
# __________________________________________________________

# Змеиный регистр
# 32 106
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
# Примечание 1. Почитать подробнее о стилях именования можно тут.

# объявление функции


def convert_to_python_case(text):
    pass


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
# __________________________________________________________


# Змеиный регистр
# 32 106
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
# Примечание 1. Почитать подробнее о стилях именования можно тут.
# объявление функции

# 1) Создаем пустой список, например s

# 2) Далее в диапазоне его длины начинаем перебирать:
# если text[i].isupper() (если буква заглавная),
# то к списку добавляем '_' (s.append('_')).
# Если буква не заглавная то переходим к строке, в которой пишем прибавление к списку
#  маленькой буквы (s.append(text[i].lower()) ).
# В конце под for возвращаем ''.join(s[1:])


# Не благодарите !


def convert_to_python_case(text):
    l1 = list(text)
    l2 = []
    for i in range(len(l1)):

        if i == 0 and l1[i].isupper():
            l2.append(l1[i].lower())
        elif i > 0 and l1[i].isupper():
            l2.append('_')
            l2.append(l1[i].lower())

        else:
            l2.append(l1[i])

    return "".join(l2)


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
# ---------------------------------------------------------------
# объявление функции


def convert_to_python_case(text):
    new_text = ""
    for el in text:
        if not el == el.lower():  # проверяем, что элемент в верхнем регистре (пропускаем цифры)
            new_text += "_" + el.lower()
        else:
            new_text += el

    return new_text[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
# ___________________________________________________________

# Середина отрезка
# 35 245
# Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка (x1; y1)(x1​;y1​) и (x2; y2)(x2​;y2​) и возвращает координаты точки являющейся серединой данного отрезка.
# функция возвращает два значения

# объявление функции


def get_middle_point(x1, y1, x2, y2):
    x_middle = (x1 + x2) / 2
    y_middle = (y1 + y2) / 2
    return x_middle, y_middle


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
# __________________________________________________________


# Площадь и длина
# 34 912
# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.


# объявление функции

def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * radius ** 2
    return c, s


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
# __________________________________________________________


# Корни уравнения 🌶️🌶️
# 34 088
# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения ax2+bx+c=0ax2+bx+c=0 и возвращает его корни в порядке возрастания.
# Примечание 2. Гарантируется, что квадратное уравнение имеет хотя бы один корень.

# объявление функции


def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = (-b - math.sqrt(d)) / (2 * a)
        x_2 = (-b + math.sqrt(d)) / (2 * a)

    elif d == 0:
        x_1 = (-1 * b) / (2 * a)
        x_2 = (-1 * b) / (2 * a)
    # else:
        # print('Нет корней')

    return min(x1, x2), max(x1, x2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
# -----------------------------от препода--------------------


def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)

    return min(x1, x2), max(x1, x2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
# __________________________________________________________


# Звездный треугольник 🌶️
#  29 322
# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой равными 1515 и 88 соответственно:

def draw_triangle(osn, h_triangl):

    j = 1
    for i in range(h_triangl - 1, -1, -1):

        print(' ' * i, j * '*', sep='')
        j += 2


# данные
a = 15
h = 8

# вызов функции
draw_triangle(a, h)
# __________________________________________________________

# Калькулятор доставки
#  29 703
# Интернет магазин осуществляет экспресс доставку для своих товаров по цене 10001000 рублей за первый товар и 120120 рублей за каждый последующий товар. Напишите функцию get_shipping_cost(quantity), которая принимает в качестве аргумента натуральное число quantity – количество товаров в заказе и возвращает стоимость доставки.

# объявление функции


def get_shipping_cost(quantity):
    price = 1000
    if quantity == 1:
        price = 1000
    if quantity > 1:
        price = 1000 + (n - 1) * 120
    return price


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

# __________________________________________________________


# Биномиальный коэффициент 🌶️
# 29 336
# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает значение биномиального коэффициента, равного n!k!(n−k)!k!(n−k)!n!​.

# Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 11 до nn, то есть
# n!=1⋅2⋅3⋅…⋅n

# Примечание 2. Реализуйте вспомогательную функцию factorial(n), вычисляющую факториал числа, или воспользуйтесь уже готовой функцией из модуля math. Обратите внимание, что функция compute_binom(n, k) должна возвращать целое число.


# объявление функции

def compute_binom(n, k):
    fakt = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(fakt)


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))

# __________________________________________________________


# Число словами 🌶️
# 29 108
# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке.
# Примечание 1. Считайте, что число 1≤num ≤991≤num ≤99.

# объявление функции
def number_to_words(num):

    number = ''
    l1 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
          'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    l3 = ['ноль', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
          'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if 1 <= num <= 19:

        number = l1[num]

    elif 20 <= num <= 99:

        num_digit1 = num % 10
        num_digit2 = num // 10

        # если не целые десятки (21,31,41...)
        if num_digit1 != 0:
            number = l3[num_digit2] + ' ' + l1[num_digit1]
        else:
            # если только целые десятки (20,30,40...)
            number = l3[num_digit2]

    return number


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
# -------------------от препода---------------------------
# объявление функции


def number_to_words(num):
    before_twenty = [
        '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать',
        'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
    ]
    after_twenty = [
        'двадцать', 'тридцать', 'сорок', 'пятьдесят',
        'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'
    ]

    if num < 20:
        res = before_twenty[num]
    else:
        res = after_twenty[num // 10 - 2] + " " + before_twenty[num % 10]

    return res.strip()


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
# _____________________________________________________________________________

# Искомый месяц
# 29 170
# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.

# объявление функции
# объявление функции


def get_month(language, number):

    l_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
            'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    l_en = ['january', 'february', 'march', 'april', 'may', 'june',
            'july', 'august', 'september', 'october', 'november', 'december']

    if language == 'ru':
        mounth = l_ru[number - 1]
    elif lan == 'en':
        mounth = l_en[number - 1]
    return mounth


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
# __________________________________________________________


# Магические даты
# 28 835
# Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.
# Напишите функцию is_magic(date), которая принимает в качестве аргумента строковое представление корректной даты и возвращает значение True, если дата является магической и False - в противном случае.

# объявление функции
def is_magic(date):

    l1 = date.split('.')
    return int(l1[0]) * int(l1[1]) == int(l1[2][-2:])

    # или так можно решить
    # seq = date.split(".")
    # day, month, year = int(seq[0]), int(seq[1]), int(seq[2])
    # return day * month == year % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
# __________________________________________________________


# Панграммы
# 28 443
# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.
# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True если текст является панграммой и False в противном случае.
# Примечание 1. Гарантируется, что введенная строка содержит только буквы английского алфавита и пробелы.

# объявление функции
def is_pangram(text):
    text = text.lower()
    chars = list(text)
    chars.sort()
    sorted_string = ''.join(chars)
    sorted_string = sorted_string.lstrip()

    chars = []
    prev = None

    for c in sorted_string:
        if prev != c:
            chars.append(c)
            prev = c

    sort_no_dubl = ''.join(chars)

    return sort_no_dubl == 'abcdefghijklmnopqrstuvwxyz'

# 'Jackdaws love my big sphinx of quartz'


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
# ---------------------от препода-----------------------------
# объявление функции


def is_pangram(text):
    text = text.lower()
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in text:
            return False

    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
# __________________________________________________________

#
#
#
# Функция удаления соседних повторяющихся символов из строки


def removeDuplicates(s):
    chars = []
    prev = None

    for c in s:
        if prev != c:
            chars.append(c)
            prev = c

    return ''.join(chars)


if __name__ == '__main__':

    s = 'AAABBCDDD'
    print(removeDuplicates(s))


# ---------------------------------------------------------------
#  функция чтобы повторения случайных чисел стали невозможными:
#


def generate_random_int_list(items, from_number, to_number):
    rl = []

    while len(rl) < items:
        n = randint(from_number, to_number)
        if n in rl:
            continue
        else:
            rl.append(n)

    return rl


print(*generate_random_int_list(10, 1, 100), sep='\n')
# __________________________________________________________


#
#
#

num_rand = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

# защита от дурака


def is_valid(num_str):
    # isdigit() определяет, состоит ли исходная строка только из цифровых символов.
    # Метод возвращает значение True если исходная строка является непустой и состоит
    # только из цифровых символов и False в противном случае.

    # необходимо,  чтобы проверка isdigit(), стояла в условии первой,
    # т.к. Python лениво оценивает логические условия и если условия поменять местами,
    # то при введении строки будет выдаваться ошибка из-за применения int() к ней

    return s.isdigit() and 1 <= int(num_str) <= 100


# проверка корректности ввода
while True:
    n = input()    # вводим число

    if not (is_valid(n)):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        n = int(n)
        break


left = 1
right = n
middle = (left + right) // 2


i = 1

while middle != n:

    if middle < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        left = middle + 1
    elif middle > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        right = middle - 1

    middle = (left + right) // 2

    i += 1
print('Вы угадали, поздравляем!')
print('количество попыток =', i)
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
# __________________________________________________________

# Тимур и его числа
#
#


# генерируем случайное число от 1 до 100
num_rand = random.randint(1, 101)
print(num_rand)
print('Добро пожаловать в числовую угадайку')


# защита от дурака
def is_valid(num_str):
    # isdigit() определяет, состоит ли исходная строка только из цифровых символов.
    # Метод возвращает значение True если исходная строка является непустой и состоит
    # только из цифровых символов и False в противном случае.

    # необходимо,  чтобы проверка isdigit(), стояла в условии первой,
    # т.к. Python лениво оценивает логические условия и если условия поменять местами,
    # то при введении строки будет выдаваться ошибка из-за применения int() к ней

    return num_str.isdigit() and 1 <= int(num_str) <= 100


# проверка корректности ввода
while True:
    answer = input('введите число от 1 до 100: ')    # вводим число
    if not (is_valid(answer)):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    answer = int(answer)

    if answer < int(num_rand):
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif answer > int(num_rand):
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break


print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
# __________________________________________________________

# __________________________________________________________


# Магический шар 8
# 29 600
#
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да',  'Да',
           'Пока неясно, попробуй снова', 'Спроси позже',  'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
           'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

print()
print()
print('---------------------------------------------')
print('ПРИВЕТ МОЙ ДОРОГОЙ ДРУГ, Я МАГИЧЕСКИЙ ШАР, И Я ЗНАЮ ОТВЕТ НА ЛЮБОЙ ТВОЙ ВОПРОС.')
print('---------------------------------------------')
name = input('Представьтесь, пожалуйста! ---> __')
print('\"Привет, ', name, '\"', sep='')
print()

# функция корректного ввода вопроса


def is_valid(val_str):
    return val_str.isalpha()


# цикл, который будет запрашивать у пользователя данные
while True:
    input('ВВЕДИТЕ ВАШ ВОПРОС:  ')
    print()
    print(random.choice(answers))
    print()
    # Уточните у пользователя, хочет ли он задать еще один вопрос, если да, то вернитесь в основной цикл программы, если нет выведите сообщение 'Возвращайся если возникнут вопросы!' и завершите программу.
    restart = input('Хотите задать еще вопрас? (yes(Y)/no(N): __')
    print()
    if restart in 'yYнН':
        continue
    else:
        print()
        print('---------------------------------------------')
        print("    'Возвращайся если возникнут вопросы!'")
        print('---------------------------------------------')
        print()
        print()
        print()
        print('-         __$$$$$$$$_____$$$$$$______$$$$$$')
        print('-__$$_____$_____$$____$$___$$___$$')
        print('-__$$_____$______$$____$$_$$___$$')
        print('-__$$_____$_$$$$$$$$____$$$___$$')
        print('-__$$_____$$$$$$$$$$$________$$_$$$$$$$$_')
        print('-__$$_____$$$$$__$$$$$______$$$$_______$$')
        print('-__$$_____$$$$$__$$$$$$____$$$$_____$$__$$')
        print('-__$$_____$$$$$$$$$$$_$$__$$_$$_____$$$$$$')
        print('-__$$_____$_$$$$$$$$____$$___$$______$$___')
        print('-__$$_____$____________________$$______$$$')
        print('-__$$_____$$$$$$$$$$_____________$$$$$$$$')
        print('-__$$_____________$$')
        print('-__$$$$$$$$$$$$$$$$$')

        break


# __________________________________________________________

# _______________________________________________________________________________

# Генератор безопасных паролей
#
# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.


def generate_symbols_list(is_numbers=False, is_letters=False, is_specials=False):
    numbers = [chr(i) for i in range(48, 58)]

    letters = [chr(i) for i in range(65, 91)] + \
              [chr(i) for i in range(97, 123)]

    special = [chr(i) for i in range(33, 48)] + \
              [chr(i) for i in range(58, 65)] + \
              [chr(i) for i in range(91, 97)] + \
              [chr(i) for i in range(123, 127)]

    symbols = []
    if is_numbers:
        symbols.extend(numbers)
    if is_letters:
        symbols.extend(letters)
    if is_specials:
        symbols.extend(special)

    return symbols


def generate_password(length, is_numbers=False, is_letters=False, is_specials=False):
    symbols = generate_symbols_list(is_numbers, is_letters, is_specials)
    return ''.join(choice(symbols) for _ in range(length))


def request_number(message):
    while True:
        result = input(message)

        if result.isdigit():
            result = int(result)
            break
        else:
            print('Вы должны ввести число!')

    return result


print('Приветствую вас в генераторе паролей!')

length = request_number('Введите длину пароля: ')

is_numbers = input('Нужны ли цифры? [да/нет] ').lower() == 'да'
is_letters = input('Нужны ли буквы? [да/нет] ').lower() == 'да'
is_specials = input('Нужны ли специальные символы? [да/нет] ').lower() == 'да'

print('Ваш пароль готов!')
print(generate_password(length, is_numbers, is_letters, is_specials))
# __________________________________________________________


# шифр цезаря
#
#

# Блажен, кто верует, тепло ему на свете!

const_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'


# put your python code here
n = int(input())
s = input()
s = 'Блажен, кто верует, тепло ему на свете!'
s = s.lower()
# s ='Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!'


g = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
g1 = 'abcdefghijklmnopqrstuvwxyz'
for j in range(len(s)):
    if s[j] not in g and s[j] not in g1:
        print(s[j], end='')
    else:
        v = ord(s[j])
        v = v - n
        if v > 1103:
            v1 = 1072 + v - 1104
            print(chr(v1), end="")
        elif v < 1072:
            v1 = 1104 - 1072 + v
            print(chr(v1), end="")
        elif 1072 <= v <= 1104:
            v1 = v
            print(chr(v1), end="")
# __________________________________________________________


# __________________________________________________________


# BOH   = Binary, Octal, Hex
# 21 145
# На вход программе подается натуральное число в десятичной системе счисления.
# Напишите программу, которая переводит его в двоичную,
# восьмеричную и шестнадцатеричную системы счисления.

num = int(input())

# Если нам требуется избавиться от приставок 0b, 0o, 0x, то мы можем воспользоваться строковым срезом:
print(bin(num)[2:])
print(oct(num)[2:])
# Примечание 2. Для шестнадцатеричной системы счисления используйте заглавные буквы A, B, C, D, E, F
print(hex(num)[2:].upper())


# __________________________________________________________

# Угадайка слов (Hangman)
# Описание проекта: программа загадывает слово, а пользователь должен его угадать.
# Изначально все буквы слова неизвестны. Также рисуется виселица с петлей.
# Пользователь предлагает букву, которая может входить в это слово.
# Если такая буква есть в слове, то программа ставит букву столько раз, сколько она
# встречается в слове. Если такой буквы нет, к виселице добавляется круг в петле,
# изображающий голову. Пользователь продолжает отгадывать буквы до тех пор, пока не
# отгадает всё слово. За каждую неудачную попытку добавляется еще одна часть туловища
# висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги.

word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
             'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 'доллар',
             'территория', 'изменение', 'направление', 'рисунок', 'течение', 'церковь', 'население', 'большинство',
             'музыка', 'правда', 'свобода', 'память', 'команда', 'договор', 'дерево', 'хозяин', 'природа', 'телефон',
             'позиция', 'писатель', 'самолет', 'солнце', 'спектакль', 'способ', 'журнал', 'руководитель', 'специалист',
             'оценка', 'регион', 'процент', 'родитель', 'требование', 'основание', 'половина', 'анализ', 'автомобиль',
             'экономика', 'литература', 'бумага', 'степень', 'господин', 'надежда', 'предмет', 'вариант', 'министр',
             'граница', 'модель', 'операция', 'название', 'старик', 'миллион', 'счастье', 'ребята', 'кабинет',
             'магазин', 'пространство', 'знание', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник',
             'участок', 'желание', 'доктор', 'председатель', 'представление', 'солдат', 'художник', 'оружие',
             'соответствие', 'парень', 'зрение', 'генерал', 'понятие', 'строительство', 'услуга', 'содержание',
             'радость', 'безопасность', 'продукт', 'комплекс', 'бизнес', 'сотрудник', 'предложение', 'технология',
             'реформа', 'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль', 'продукция', 'техника',
             'здание', 'необходимость', 'подготовка', 'республика', 'хозяйство', 'бюджет', 'деревня', 'элемент',
             'обстоятельство', 'победа', 'источник', 'звезда', 'сестра', 'практика', 'проведение', 'карман',
             'определение', 'функция', 'войско', 'комиссия', 'применение', 'капитан', 'работник', 'обеспечение',
             'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка', 'теория', 'разработка', 'личность',
             'праздник', 'влияние', 'читатель', 'удовольствие', 'ответственность', 'учитель', 'множество',
             'особенность', 'показатель', 'корабль', 'впечатление', 'частность', 'детство', 'профессор', 'прошлое',
             'командир', 'коридор', 'поддержка', 'собрание', 'болезнь', 'клетка', 'заявление', 'попытка', 'сравнение',
             'расчет', 'депутат', 'комитет', 'выражение', 'здоровье', 'десяток', 'глубина', 'студент', 'секунда',
             'скорость', 'ошибка', 'режиссер', 'поверхность', 'ощущение', 'станция', 'революция', 'колено',
             'министерство', 'стекло', 'высота', 'бабушка', 'трубка', 'мастер', 'поведение', 'столица', 'механизм',
             'передача', 'способность', 'подход', 'энергия', 'существование', 'исполнение', 'сожаление', 'заместитель',
             'ресурс', 'рождение', 'администрация', 'стоимость', 'улыбка', 'артист', 'фигура', 'субъект', 'реакция',
             'список', 'фотография', 'журналист', 'нарушение', 'заседание', 'больница', 'существо', 'свойство',
             'поколение', 'животное', 'усилие', 'отличие', 'остров', 'противник', 'реализация', 'страница',
             'формирование', 'житель', 'красота', 'растение', 'явление', 'наличие', 'одежда', 'кресло', 'больной',
             'университет', 'традиция', 'декабрь', 'ладонь', 'сведение', 'цветок', 'октябрь', 'занятие', 'сентябрь',
             'помещение', 'январь', 'зритель', 'редакция', 'фактор', 'август', 'известие', 'зависимость', 'охрана',
             'оборудование', 'концерт', 'отделение', 'расход', 'выставка', 'милиция', 'переход', 'произведение',
             'родина', 'собственность', 'лагерь', 'имущество', 'кровать', 'аппарат', 'середина', 'клиент', 'отрасль',
             'беседа', 'законодательство', 'продажа', 'повышение', 'полковник', 'сомнение', 'понимание', 'апрель',
             'кодекс', 'настроение', 'должность', 'преступление', 'лестница', 'установка', 'появление', 'получение',
             'образец', 'главное', 'костюм', 'ценность', 'обязанность', 'таблица', 'воспоминание', 'лошадь', 'коллега',
             'организм', 'ученик', 'учреждение', 'открытие', 'характеристика', 'выполнение', 'оборона', 'выступление',
             'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан', 'километр', 'признак',
             'промышленность', 'американец', 'заключение', 'восток', 'исключение', 'постановление', 'перевод',
             'секретарь', 'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина',
             'зарплата', 'подарок', 'тюрьма', 'конкурс', 'книжка', 'изучение', 'просьба', 'публика', 'сообщение',
             'угроза', 'достижение', 'назначение', 'реклама', 'портрет', 'стакан', 'творчество', 'телевизор',
             'инструмент', 'концепция', 'лейтенант', 'реальность', 'знакомый', 'конфликт', 'переговоры', 'запись',
             'площадка', 'последствие', 'сотрудничество', 'зеркало', 'академия', 'палата', 'потребность', 'ноябрь',
             'увеличение', 'поездка', 'потеря', 'февраль', 'мероприятие', 'принятие', 'устройство', 'вещество',
             'категория', 'гостиница', 'издание', 'объединение', 'темнота', 'человечество', 'колесо', 'опасность',
             'разрешение', 'воздействие', 'коллектив', 'камера', 'следствие', 'кандидат', 'родственник', 'давление',
             'присутствие', 'взаимодействие', 'партнер', 'двигатель', 'достоинство', 'страсть', 'испытание', 'оплата',
             'разница', 'водитель', 'снижение', 'формула', 'капитал', 'новость', 'эффект', 'губернатор', 'доклад',
             'убийство', 'эксперт', 'автобус', 'платье', 'общение', 'психология', 'проверка', 'процедура', 'рабочий',
             'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение', 'доказательство',
             'признание', 'постель', 'владелец', 'компьютер', 'инженер', 'старуха', 'ракета', 'вершина', 'выпуск',
             'торговля', 'молодежь', 'корпус', 'недостаток', 'сущность', 'талант', 'эффективность', 'полоса',
             'основное', 'рассмотрение', 'следователь', 'описание', 'редактор', 'дворец', 'забота', 'столик',
             'эксперимент', 'печать', 'кольцо', 'пистолет', 'воспитание', 'начальство', 'профессия', 'ворота', 'дружба',
             'окончание', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кредит', 'господь',
             'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'металл', 'молоко', 'прокурор',
             'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние', 'подразделение', 'сигнал', 'атмосфера',
             'контакт', 'сигарета', 'восторг', 'золото', 'премия', 'король', 'подъезд', 'автомат', 'мальчишка',
             'чтение', 'поселок', 'свидетель', 'ставка', 'удивление', 'поворот', 'возвращение', 'мгновение', 'статус',
             'параметр', 'сказка', 'тенденция', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'эксплуатация',
             'коммунист', 'пенсия', 'приятель', 'объяснение', 'производитель', 'философия', 'мощность', 'обязательство',
             'кризис', 'указание', 'яблоко', 'препарат', 'действительность', 'москвич', 'остаток', 'изображение',
             'сделка', 'сочинение', 'покупатель', 'затрата', 'строка', 'единица', 'обработка', 'чемпионат']

# ф-я возвращает случайное слово из списка word_list в верхнем регистре.


def get_word(l_words):
    return random.choice(l_words).upper()


print(get_word(word_list))


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

# Напишите функцию play(), в которой будет осуществляться основная логика игры.
# Функция play() принимает в качестве аргумента слово word,
# сгенерированное функцией  get_word().


def play(word):
    # тело функции
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = '_' * len(word)
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)


# __________________________________________________________


# __________________________________________________________
