# 1. Пройти по списку с помощью итератора

# list = [1, 2, 3, 4, 5]
# list_iterator = iter(list)
#
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))

# 2. Итератор для строки

# str = "Hello"
# str_iterator = iter(str)
#
# print(next(str_iterator))
# print(next(str_iterator))
# print(next(str_iterator))
# print(next(str_iterator))
# print(next(str_iterator))

# 1. Создайте список из квадратов чисел от 1 до N, используя list comprehension.

# N = int(input("Введите число: "))
#
# result = [i ** 2 for i in range(1, N + 1)]
# print(result)

# 2. Сформируйте список, содержащий только четные числа в диапазоне от -10 до 10.

# result = [i for i in range(-10,11) if i % 2 == 0]
# print(result)

# 3. Дан список слов. Создайте новый список, содержащий длины всех слов, используя генератор списков.

# words = ["hello", "world", "python"]
#
# result = [len(word) for word in words]
# print(result)

# 4. Создайте список из чисел от 1 до 20, где вместо четных чисел будет "четное",
# а вместо нечетных — "нечетное" (используйте тернарный оператор)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]
#
# result = ["четное" if i % 2 == 0 else "нечетное" for i in list]
#
# print(result)

# 5. Проверка, является ли объект итерируемым

objects = [1, 'привет', [2, 3]]

result = [
    True if isinstance(obj, (str, list, tuple, dict, set)) else False
    for obj in objects
]

print(result)