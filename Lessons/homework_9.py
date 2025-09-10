# 1.Создайте словарь, в котором хранятся названия фруктов и их цены за 1 кг.
# Добавьте в словарь еще один фрукт и выведите итоговый словарь.

# dict_ex = {"appple": 10, "banana": 20, "orange": 30}
#
# dict_ex.setdefault("pear", 40)
# print(dict_ex)

# 2. Дан словарь с оценками студентов:

# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
#
# for key, value in grades.items():
#     if value <4:
#         print(key, end=" ")

# 3. Создайте словарь, содержащий название стран в качестве ключей и их столицы в качестве значений.

# countries = {"Russia": "Moscow", "France": "Paris", "Germany": "Berlin"}
#
# for key, value in countries.items():
#     input_country = input("Введите страну: ")
#     if input_country == key:
#         print(value)
#     else: print("Страна не найдена")

# 4. Дан список студентов и их курсов:

# students = [
#     ("Анна", "Python"),
#     ("Борис", "Java"),
#     ("Виктор", "Python"),
#     ("Галина", "C++"),
#     ("Дмитрий", "Python")
# ]
#
# courses = {}
#
# for name, course in students:
#     if course not in courses:
#         courses[course] = []
#     courses[course].append(name)
#
# print(courses)

# 5. Создайте словарь, содержащий оценки студентов:

# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
#
# min_student = min(grades, key=grades.get)
# grades.pop(min_student)
# print(grades)

# 6. Дан список студентов:

# students = ["Анна", "Борис", "Виктор", "Галина"]
# ages = [21, 22, 23, 24]
#
# dict_students = dict.fromkeys(students)
# dict_students.update(zip(students, ages))
# print(dict_students)

# 7. Дан словарь с курсами валют:

# exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
#
# input_currency = input("Введите валюту: ")
#
# if input_currency in exchange_rates:
#     print(f"Курс: {exchange_rates[input_currency]}")
# else:
#     print("Неизвестная валюта")
#     exchange_rates.setdefault(input_currency, "None")
#     print(exchange_rates)

# 8. Создайте два словаря:

# dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
# dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
#
# dict1.update(dict2)
# print(dict1)

# 1. Создайте кортеж из пяти элементов (разных типов данных).
# Выведите на экран второй элемент и последний элемент этого кортежа.

# tuple_ex = (1, 2, 3, 4, 5)
# print(tuple_ex[1], tuple_ex[-1])

# 2. Дан кортеж чисел:

# nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
#
# print(nums.count(4))
# print(nums.index(7))

# 3. Преобразуйте следующий список в кортеж:

# lst = ["Python", "Java", "C++", "JavaScript"]
#
# t = tuple(lst)
# print("C++" in t)
# print(t)

# 4. Создайте кортеж с числами от 1 до 10.

# t = tuple(range(1, 11))
#
# print(t)
# print(t[:3])
# print(t[7:])
# print(t[::2])

# 5. Создайте кортеж, содержащий вложенные список и словарь.

t = ([1, 2, 3], {"a": 4, "b": 5})

t[0][1] = 10
print(t)