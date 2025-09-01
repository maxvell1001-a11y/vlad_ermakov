# 1. Работа с регистром

s = "Python для автоматизации"
print(s.upper())
print(s.lower())

# 2. Подсчет вхождений подстроки

msg = "абракадабра"
print(msg.count("ра"))
print(msg.count("а", 2))

# 3. Поиск подстроки

s = "абракадабра"
print(s.find("ка"))
print(s.rfind("а"))
print(s.find('xyz')) # Ошибка

# 4. Замена подстроки

text = "Я изучаю Java"
print(text.replace("Java", "Python"))
print(text.replace(' ', ''))

# 5. Проверка содержимого строки

s = "Python"
s2 = "12345"
s3 = "123abc"

print(s.isalpha())
print(s2.isdigit())
print(s3.isdigit())

# 6. Дополнение строк

code = "42"
print(code.rjust(7, '0'))
code2 = "text"
print(code2.ljust(10, '*'))

# 7. Разбиение строк

text = "яблоко, груша, банан"
print(text.split())
text2 = "Python;Java;C++"
print(text2.split(";"))

# 8. Объединение списка в строку

c = "Привет", "мир", "!"
print(' '.join(c))
c2 = ["apple", "banana", "cherry"]
print(", ".join(c2))

# 9. Удаление пробелов

a = "Python "
print(a.rstrip())
b = " Python"
print(b.lstrip())
c = " Python "
print(c.strip())

# 10. Дополнительное задание

text = "программирование"
print(text.capitalize())
print(text.count("р"))
print(text.find("и"))

# 1. Перевод строки

text = "Hello\nPython"
print(text) # Присутствие переноса строки

# 2. Горизонтальная табуляция

t = "Python\tAutomation"
print(t) # Присутствие табуляции, табуляция - отступ в 4 пробела

# 3. Экранирование символов

path = "C:\new\test.txt"
print(path) # Не отобразилось часть символов без экранирования
path = "C:\\new\\test.txt"
print(path) # Исправленная версия с экранированием символов
print("Марка вина \"Ягодка\"")

# 4. Сырые (raw) строки

path = r"C:\new\test.txt"
print(path) # Используется raw строка

# 5. Использование разных спецсимволов

s = "Hello\b World"
print(s) # Hell World
s = "Hello\fPython"
print(s) # используется в качестве символа новой страницы

# 1. Формирование строк через конкатенацию

age = 25
name = "Steven"

result = "Меня зовут " + name + ", мне " + str(age) + " лет."
print(result)

# 2. Форматирование строк с .format()

name = "Steven"
age = 25

result = "Привет, меня зовут {}, мне {} лет.".format(name, age)
print(result)
result = "Привет, меня зовут {}, мне {} лет.".format(age, name)
print(result)

# 3. Использование F-строк

city = "Москва"
age = 2005
print(f"Сегодня {age} год, и я живу в {city.replace('а', 'е')}.")
print(f"Через 5 лет будет {age + 5} год.")

# 4. Операции внутри F-строк

age = 20
print(f"Дважды мой возраст: {age * 2} лет.")
age = 'Двадцать'
print(f"Дважды мой возраст: {str(age.upper())} лет.")

# 5. Дополнительное задание

rub = 92.5
dol = 1

result = "Курс валют: 1 доллар = 92.5 рубля.".format(dol, rub)
print(result)

a = 7
print(f"Квадрат числа {a} равен {a ** 2}.")
