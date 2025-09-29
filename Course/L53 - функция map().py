# Задание 1:

lst = ["1", "2", "3", "5", "7"]

a = map(int, lst)
print(list(a))

# Задание 2:

lst = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]

a = map(len, lst)
print(list(a))

# Задание 3:

lst = ["Python", "Java", "C++"]

a = map(lambda x: list(x.lower()), lst)
print(list(a))

# Задание 4:

a = map(lambda x: int(x) ** 2, input("Введите числа через пробел: ").split())
print(list(a))

# Задание 5:

lst = ["Москва", "Санкт-Петербург", "Казань"]

a = map(str.upper, lst)
print(list(a))