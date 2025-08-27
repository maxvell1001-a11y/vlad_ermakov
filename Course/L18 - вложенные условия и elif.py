x = int(input("Введите оценку: "))
if x == 5:
    print("Отлично")
elif x == 4:
    print("Хорошо")
elif x == 3:
    print("Удовлетворительно")
elif x == 2 or x == 1:
    print("Неудовлетворительно")
else:
    print("Неверная оценка")

hour = int(input("Введите текущее время (0-23): "))
if 6 >= hour <= 11:
    print("Утро")
elif 12 >= hour <= 17:
    print("День")
elif 18 >= hour <= 21:
    print("Вечер")
elif 22 >= hour or hour <= 5:
    print("Ночь")
else:
    print("Некорректное время")

temp = int(input("Введите температуру: "))
if temp < -10:
    print("Очень холодно")
elif -10 >= temp <= 0:
    print("Холодно")
elif 1 >= temp <= 10:
    print("Прохладно")
elif 11 >= temp <= 25:
    print("Тепло")
else:
    print("Жарко")

year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

a = float(input("Введите первое число: "))
x = input("Введите операцию (+, -, *, /): ")
b = float(input("Введите второе число: "))
if x == "+":
    print(a + b)
elif x == "-":
    print(a - b)
elif x == "*":
    print(a * b)
elif x == "/" and b != 0:
    print(a / b)
elif b == 0:
    print("Ошибка: деление на ноль!")
else:
    print("Некорректная операция")