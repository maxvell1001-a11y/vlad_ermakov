x = float(input("1. Введите число: "))
if x > 0:
    print('Положительное число')
if x < 0:
    print('Отрицательное число')
else:
    print('Число равно нулю')

x = int(input("2. Введите число: "))
if x % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')

x = float(input("3. Введите число: "))
if 1 <= x <= 10:
    print('Число в диапазоне')
else:
    print('Число не в диапазоне')

a = float(input("Первое число: "))
b = float(input("Второе число: "))
if a < b:
    a , b = b, a
print(a, b)

a = float(input("Первое число: "))
b = float(input("Второе число: "))
if a < b:
    print(a)
else:
    print(b)

marks = [3, 4, 5, 2, 5, 4]
if 2 in marks:
    print("Есть неудовлетворительная оценка")
else:
    print("Все оценки положительные")

x = float(input("Введите число: "))
if x % 3 == 0 and x % 5 == 0:
    print("Число кратно 3 и 5")
if x % 3 == 0:
    print("Число кратно 3")
if x % 5 == 0:
    print("Число кратно 5")
if x % 3 != 0 and x % 5 != 0:
    print("Число не кратно 3 и 5")

x = str(input("Ввод пароля: "))
if x == "admin123":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

amount = int(input("Введите количество денег: "))
if amount >= 5000:
    print("Скидка 10%")
elif amount >= 1000:
    print("Скидка 5%")
else:
    print("Скидка 0%")

x = int(input("Введите год: "))
if x % 4 == 0 or x % 400 == 0 and x % 100 != 0:
    print("Високосный")
else:
    print("Не високосный")