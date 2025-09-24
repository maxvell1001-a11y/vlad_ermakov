# 1. Создайте текстовый файл data.txt со следующим содержимым:

with open('data.txt', "r", encoding="utf-8") as f:
    print(f.read())

# 2. Напишите программу, которая считает и выведет только первую строку из файла data.txt.

with open('data.txt', "r", encoding="utf-8") as f:
    print(f.readline())

# 3. Откройте файл data.txt и прочитайте первые 10 символов.

with open('data.txt', "r", encoding="utf-8") as f:
    print(f.readline(10))

# 4. Прочитайте все строки файла и сохраните их в список. Затем выведите этот список.

with open('data.txt', "r", encoding="utf-8") as f:
    lst = list(f.readlines())
    print(lst)

# 5. Напишите программу, которая считает строки файла data.txt в цикле и выводит их по одной, убирая символ \n в конце.

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print("Строка:", line.rstrip('\n'))

# 6. Откройте файл data.txt, прочитайте 5 символов, затем переместите указатель в начало файла

with open('data.txt', "r", encoding="utf-8") as f:
    print(f.read(6))
    f.seek(0)
    print(f.read(6))

# 7. Напишите программу, которая откроет файл data.txt, определит его размер (в байтах) и выведет его.

with open('data.txt', "rb") as f:
    f.seek(0, 2)
    size = f.tell()
    print(f"Размер файла: {size} байт")

# 8. Используйте with open(), чтобы прочитать и вывести содержимое файла data.txt.

with open('data.txt', "r", encoding="utf-8") as f:
    print(f.read())

# 9. Напишите программу, которая пытается открыть файл data.txt, прочитать его содержимое и вывести его.
# Если файл не найден, программа должна вывести "Ошибка: Файл не найден".

try:
    f = open('data.txt', "r", encoding="utf-8")
    print(f.read())

except FileNotFoundError:
    print("Ошибка: Файл не найден")

f.close()

# 10. Модифицируйте программу из Задания 1, добавив гарантированное закрытие файла в блоке finally.

try:
    f = open('data.txt', "r", encoding="utf-8")
    print("Файл открыт")
    try:
        text = f.read()
        print(text)
    finally:
        f.close()
        print("Файл закрыт")

except FileNotFoundError:
    print("Ошибка: Файл не найден")

# 11. Используйте with open(), чтобы безопасно открыть файл data.txt и прочитать его построчно.

try:
    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.rstrip('\n'))
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# 12. Создайте файл numbers.txt, который содержит по одному числу в каждой строке.
# Напишите программу, которая читает файл, суммирует все числа и выводит их сумму.
# Если файл не найден, программа должна вывести "Ошибка: Файл не найден".

try:
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        sum = 0
        for line in file:
            sum += int(line)
        print(sum)
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# 13. Создайте файл log.txt.
# Программа должна добавлять в него текущую дату и время при каждом запуске.
# Используйте модуль datetime и режим "a".

from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a", encoding="utf-8") as file:
    file.write(f"{current_time}\n")