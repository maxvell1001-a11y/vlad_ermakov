print ("Привет, мир!")
print (5, 10, 15)
print (5 + 10)
print (1, 2, 3, sep = " | ")
print ("Python -", end = " ")
print ("лучший язык")
x = 3.14
y = -8
print(f"Координаты точки: х = {x}, y = {y}")
a = "Иван"
b = 25
print(f"Имя: {a}, Возраст: {b}")

a = input()
print(f"Привет, {a}!")

a = float(input("Первое число "))
b = float(input("Второе число "))
print(a + b)
print(a)
print(abs(b))

a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))
print("Периметр:", 2 * (a + b))

a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
print("Среднее значение:", (a + b + c) / 3)

import math
a = int(input("Радиус круга: "))
print("Площадь круга:", math.pi * a ** 2)