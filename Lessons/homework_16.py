# 1. Создайте генератор, который возвращает только строки из списка:
# Выведите все строки в одну строку через пробел.

lst = ["Python", 123, "Java", 456, "C++", 789]

result = filter(lambda x: isinstance(x, str), lst)

print(' '.join(result))

# 2. Создайте генератор случайных чисел от 1 до 100 (10 чисел),
# используя модуль random (попробуйте сами найти как использовать), и найдите максимальное число.

import random

random_numbers = (random.randint(1, 100) for _ in range(10))

max_number = max(random_numbers)

print("Максимальное число:", max_number)

# 3. Создайте генератор, который возвращает слова из файла words.txt,
# но только те, которые длиннее 5 символов.

gen = (word.strip() for line in open('words.txt', 'r', encoding='utf-8')
       for word in line.split() if len(word) > 5)

print(' '.join(gen))

# 4. Напишите функцию-генератор, которая перебирает строки файла text.txt,
# # возвращая только те, которые содержат слово "Python".

def find_python_lines():
    with open('text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if 'Python' in line:
                yield line.strip()

for line in find_python_lines():
    print(line)

# 5. Создайте бесконечный генератор, который возвращает случайные числа от 1 до 100.
# Остановите выполнение, как только сгенерируется число 50.

# def infinite_random_generator():
#     while True:
#         num = random.randint(1, 100)
#         yield num
#         if num == 50:
#             break
#
# for number in infinite_random_generator():
#     print(number)

# 6. Создайте функцию-генератор, которая возвращает первые N простых чисел.
# Выведите первые 10 простых чисел.

def is_prime(num):
    """Проверяет, является ли число простым."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(N):
    """Генератор первых N простых чисел."""
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            yield num
            count += 1
        num += 1

for prime in prime_generator(10):
    print(prime)

# 7. Создайте функцию-генератор, которая имитирует загрузку данных из API.
# Генератор должен возвращать строки "Получены данные 1", "Получены данные 2", …
# Остановите генерацию после 5 вызовов next().

# gen = (f"Получены данные {i}" for i in range(1, 6))
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 8. Используйте map() вместе с лямбда-функцией, чтобы для каждого числа из пользовательского ввода
# (числа, разделённые пробелами) вычислить его квадрат.
# Результатом должно быть преобразование входной строки в список квадратов.

# in_int = input("Введите числа через пробел: ")
# result = map(lambda x: x ** 2, map(int, in_int.split()))
#
# print(list(result))

# 9. Напишите программу, которая с помощью map() и метода строк upper
# преобразует список названий городов к верхнему регистру.

cities = ["Москва", "Санкт-Петербург", "Казань"]

result = map(lambda x: x.upper(), cities)

print(list(result))

# 10. Используя filter(), оставьте в списке только те числа, которые делятся на 3 и на 5 одновременно.

lst = [15, 30, 45, 22, 60, 77, 90, 100]

res = filter(lambda x: x % 3 == 0 and x % 5 == 0, lst)

print(list(res))

# 11. Используя filter(), получите из списка только строки, содержащие хотя бы одну цифру.

lst = ["hello", "world42", "python3", "abc", "123", "data1science"]

res = filter(lambda x: any(char.isdigit() for char in x), lst)

print(list(res))

# 12. Используйте zip() и dict(), чтобы создать словарь, в котором:

countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]

zipped = zip(countries, capitals)

res = dict(zipped)

print(res)

# 13. Используйте zip(*iterable), чтобы выполнить обратное преобразование списка кортежей:

data = [(1, 'a'), (2, 'b'), (3, 'c')]

a, b = zip(*data)

print(a)
print(b)

# 14. Дан список имен names.
# Отсортируйте его так, чтобы сначала шли имена с заглавной буквы, а затем – с маленькой.

names = ["петр", "Иван", "мария", "Анна"]

res = sorted(names, key=lambda name: name.upper())
print(res)

# 15. Дан список кортежей products, где первый элемент – название товара, второй – цена.
# Отсортируйте его по цене (по возрастанию).

products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]

sorted_products = sorted(products, key=lambda x: x[1])

print(sorted_products)