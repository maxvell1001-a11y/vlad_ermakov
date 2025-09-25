# Задание 1:

try:
    with open("data.txt", encoding="utf-8") as file:
        s = file.read()
        print(s)
except:
    print("Ошибка: Файл не найден")

# Задание 2:

try:
    file = open("data.txt", encoding="utf-8")
    print("Файл успешно открыт.")
    print(file.read())
except FileNotFoundError:
    print("Ошибка: Файл не найден")
finally:
    file.close()
    print("Файл закрыт?", file.closed)

# Задание 3:

try:
    with open("data.txt", encoding="utf-8") as file:
        s = file.readlines()
        print(s)
except:
    print("Ошибка: Файл не найден")

# Задание 4:

try:
    with open("data.txt", encoding="utf-8") as file:
        for line in file:
            print(int(line))
except:
    print("Ошибка при обработке файла")
finally:
    print("Файл закрыт?", file.closed)

# Задание 5:

import os

if os.path.exists("data.txt"):
    print("Файл найден!")
    with open("data.txt", encoding="utf-8") as file:
        print(file.read())
else:
    print("Файл не найден")

# Задание 6:

try:
    with open("numbers.txt", encoding="utf-8") as file:
        for line in file:
            total = sum(int(line.strip()) for line in file)
            print("Сумма чисел:", total)
except:
    print("Ошибка: Файл не найден")