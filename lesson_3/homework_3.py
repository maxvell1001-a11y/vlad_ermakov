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
a = input("Введите имя: ")
print(f"Привет, {a}!")
a = float(input("Первое число "))
b = float(input("Второе число "))
print(a + b)
a = int(input("Введите целое число: "))
print((a ** 2))
print(5 > 3, 10 < 2, 7 == 7, 6 != 8, 4 >= 4, 9 <= 3)
res = 8 > 12
print(type(res))
x = 15
print(x % 2 == 0)
print(x % 5 == 0)
print(x % 3 == 0 and x % 5 == 0)
y = 4.5
print(y >= 1 and y <= 10)
print(y >= 0 and y <= 5 or y >= 10 and y <= 15)
print(not(y < 5))
print(True or False and False)
print(not (False and True))
print(False or not (True and True))
print(not (10 > 5 or 3 < 1))
print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))
n = 21
print(n >= 0)
print(n % 2 == 0)
print(n % 3 == 0)
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2], s[-2])
print(s[len(s) - 1])
s = "Программирование"
p = s[0:6]
print(p)
o = s[11:]
print(o)
e = s[2:7]
print(e)
print(s[1::2])
print(s[::-1])
print(s[::3])
print(s[::-2])
s2 = 'п' + s[1:]
print(s2)
word = "abcdefgh"
print(word[2:5])
print(word[::-1])
print(word[1:-1])